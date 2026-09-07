# -*- coding: utf-8 -*-
"""بناء الكتاب كاملاً وتجميعه مع الترويسات وأرقام الصفحات والفهرس."""
import os, sys, re
sys.path.insert(0, "book")
import pymupdf
from css import CSS
from front import front_matter
from back import back_matter
from parts import PARTS, opener_html
import cover as covermod

A5 = pymupdf.paper_rect("a5")
MARGIN = (44, 47, -44, -52)
ARCH = pymupdf.Archive(".")

def strip_opener(html):
    # يزيل كتلة <section class="partpage">...</section> الأولى
    return re.sub(r'<section class="partpage">.*?</section>\s*', '', html, count=1, flags=re.S)

_CSS_NO_BREAK = CSS.replace("page-break-before: always;", "page-break-before: avoid;")

def _render_one(html, cap=60):
    """يرسم جزءاً واحداً (بلا فواصل صفحات صريحة) ويعيد عدّاد الصفحات."""
    story = pymupdf.Story(html=html, user_css=_CSS_NO_BREAK, archive=ARCH)
    writer = pymupdf.DocumentWriter("seg/_chunk.pdf")
    where = A5 + MARGIN
    pages = 0
    while True:
        dev = writer.begin_page(A5)
        more, _ = story.place(where)
        story.draw(dev)
        writer.end_page()
        pages += 1
        if not more or pages >= cap:
            break
    writer.close()
    return pages, (pages >= cap)

def run_story(html, out_path, cap=400, return_chunks=False):
    """يقسّم المحتوى عند كل فاصل صفحة صريح ويدمج النتاج.
    يعيد (إجمالي الصفحات، [عدد صفحات كل chunk])."""
    chunks = re.split(r'<section class="pagebreak">', html)
    merged = pymupdf.open()
    total = 0
    chunk_sizes = []
    for ci, ch in enumerate(chunks):
        ch = ch.strip()
        if not ch:
            continue
        n, hitcap = _render_one(ch)
        if hitcap:
            print(f"  !! WARN cap in chunk {ci} of {out_path}", flush=True)
        c = pymupdf.open("seg/_chunk.pdf")
        merged.insert_pdf(c)
        total += n
        chunk_sizes.append(n)
    merged.save(out_path)
    merged.close()
    if return_chunks:
        return total, chunk_sizes
    return total

def toc_html(entries):
    rows = []
    for label, num, lvl in entries:
        pad = 8 + lvl*15
        if lvl == 0:
            rows.append(
              f'<tr><td style="padding-right:{pad}pt;color:#133320;font-family:kufi;font-weight:700;font-size:10pt;">{label}</td>'
              f'<td class="c" style="width:32pt;color:#c9a25e;font-family:kufi;font-weight:700;">{num if num is not None else ""}</td></tr>')
        else:
            rows.append(
              f'<tr><td style="padding-right:{pad}pt;color:#3a4a40;font-size:9.2pt;">{label}</td>'
              f'<td class="c" style="width:32pt;color:#1d5b38;font-family:kufi;font-weight:700;font-size:9pt;">{num if num is not None else ""}</td></tr>')
    return """
<section>
<div class="kicker">محتويات الكتاب</div>
<h2 class="chap">الفهرس</h2>
<table class="food" style="margin-top:10pt;">
<thead><tr><th>الموضوع</th><th class="c" style="width:30pt;">ص</th></tr></thead>
<tbody>
""" + "\n".join(rows) + """
</tbody></table>
</section>
"""

# مدخلات الفهرس: (نص البحث، التسمية، المستوى، باب؟)
TOC_SPEC = [
  ("مدخل إلى هذا الكتاب", "مدخل إلى هذا الكتاب", 1, "front"),
  ("ضياء العوضي: الطبيب", "سيرة الدكتور ضياء العوضي", 1, "front"),
  (None, "الباب الأول: فلسفة نظام الطيبات", 0, "part:0"),
  ("الجسم سيّد نفسه", "الجسم سيّد نفسه", 2, "part:0"),
  ("القاعدة الذهبية: القائمة البيضاء", "القاعدة الذهبية: القائمة البيضاء وحدها", 2, "part:0"),
  ("مؤشرات التكرار الخمسة", "مؤشرات التكرار الخمسة", 2, "part:0"),
  ("الأساسيات الخمسة", "الأساسيات الخمسة", 2, "part:0"),
  ("قاعدة «يوم آه ويوم لأ»", "قاعدة «يوم آه ويوم لأ»", 2, "part:0"),
  ("خمسة مبادئ لتحديد الممنوعات", "مبادئ تحديد الممنوعات الخمسة", 2, "part:0"),
  (None, "الباب الثاني: قائمة المسموحات الكاملة", 0, "part:1"),
  (None, "الباب الثالث: قائمة الممنوعات الكاملة", 0, "part:2"),
  (None, "الباب الرابع: البدائل المسموحة", 0, "part:3"),
  (None, "الباب الخامس: التطبيق العملي", 0, "part:4"),
  (None, "الباب السادس: النظريات العلمية (25 نظرية)", 0, "part:5"),
  (None, "الباب السابع: نظام الطيبات للأمراض", 0, "part:6"),
  ("الخاتمة: رحلة العمر", "الخاتمة والمصادر", 0, "back"),
]

def find_page(doc, text, start=0):
    for i in range(start, len(doc)):
        if text in doc[i].get_text():
            return i
    return None

def _np(path):
    return len(pymupdf.open(path))

def build(entries):
    os.makedirs("seg", exist_ok=True)
    counts = {}
    covermod.cover_front("seg/00_cover.pdf", ARCH); counts["cover"] = 1
    covermod.title_page("seg/01_title.pdf", ARCH);  counts["title"] = 1
    covermod.copyright_page("seg/02_copyright.pdf", ARCH); counts["copy"] = 1
    covermod.back_cover("seg/07_backcover.pdf", ARCH); counts["backcover"] = 1
    counts["front"], counts["front_chunks"] = run_story(front_matter(), "seg/03_front.pdf", return_chunks=True)
    counts["toc"]   = run_story(toc_html(entries), "seg/04_toc.pdf")
    counts["body_chunks"] = {}
    for i, p in enumerate(PARTS):
        counts[f"open{i}"] = run_story(opener_html(p), f"seg/05_open{i}.pdf", cap=3)
        body = strip_opener(p[6]())
        n, chs = run_story(body, f"seg/05_body{i}.pdf", return_chunks=True)
        counts[f"body{i}"] = n
        counts["body_chunks"][i] = chs
    counts["back"] = run_story(back_matter(), "seg/06_back.pdf")
    print("  كل المقاطع بُنيت. counts:", counts, flush=True)
    return counts

def assemble(do_heads=True):
    order = ["seg/00_cover.pdf","seg/01_title.pdf","seg/02_copyright.pdf",
             "seg/03_front.pdf","seg/04_toc.pdf"]
    opener_idx = []
    for i in range(len(PARTS)):
        opener_idx.append(len(order))   # الصفحة التي سيُدرج عندها الفاتح
        order.append(f"seg/05_open{i}.pdf")
        order.append(f"seg/05_body{i}.pdf")
    order.append("seg/06_back.pdf")
    order.append("seg/07_backcover.pdf")
    out = pymupdf.open()
    seg_pages = {}
    for pth in order:
        d = pymupdf.open(pth)
        seg_pages[pth] = (len(out), len(d))
        out.insert_pdf(d)
    # بداية المتن (أول فاتح باب)
    first_open = seg_pages["seg/05_open0.pdf"][0]
    body_start = first_open
    # صفحات فواتح الأبواب (لا ترويسة ولا رقم)
    opener_pages = set(seg_pages[f"seg/05_open{i}.pdf"][0] for i in range(len(PARTS)))
    if do_heads:
        add_running(out, body_start, opener_pages)
    out.save("نظام-الطيبات-النسخة-الجديدة.pdf", garbage=4, deflate=True)
    return out, body_start, opener_pages

def _tb(page, rect, html):
    css = ("""
    @font-face{font-family:'kufi';src:url(book/fonts/kufi-900.ttf);font-weight:900;}
    @font-face{font-family:'kufi';src:url(book/fonts/kufi-700.ttf);font-weight:700;}
    @font-face{font-family:'kufim';src:url(book/fonts/kufi-500.ttf);font-weight:500;}
    @font-face{font-family:'naskh';src:url(book/fonts/naskh-500.ttf);font-weight:500;}
    @font-face{font-family:'amiri';src:url(book/fonts/amiri-400.ttf);font-weight:400;}
    *{margin:0;padding:0;}
    """)
    page.insert_htmlbox(rect, html, archive=ARCH, css=css)

def add_running(doc, body_start, opener_pages):
    gold = (0.79,0.64,0.37)
    last = len(doc) - 1  # الغلاف الخلفي بلا ترويسة ولا رقم
    for pno in range(body_start, len(doc)):
        if pno == last:
            continue
        page = doc[pno]
        W = page.rect.width
        logical = pno - body_start + 1
        if pno in opener_pages:
            continue
        page.draw_line(pymupdf.Point(44, 33), pymupdf.Point(W-44, 33), color=gold, width=0.6)
        _tb(page, pymupdf.Rect(44, 19, W-44, 32),
             '<div style="text-align:center;font-family:kufim;font-size:7.5pt;color:rgb(120,135,124);direction:rtl;">نظام الطيبات — الدليل الشامل للغذاء الصحّي الطبيعي</div>')
        _tb(page, pymupdf.Rect(44, page.rect.height-40, W-44, page.rect.height-26),
             f'<div style="text-align:center;font-family:kufi;font-size:10pt;color:rgb(29,91,56);">{logical}</div>')

def compute_toc(c):
    """حساب أرقام الصفحات المنطقية من بنية المقاطع (بدء الترقيم من أول فاتح باب)."""
    body_start = c["cover"]+c["title"]+c["copy"]+c["front"]+c["toc"]  # فهرس (0-based) لأول فاتح
    # إزاحات بداية كل باب (الفاتح) بالصفحات المنطقية (تبدأ 1)
    part_start = {}
    acc = body_start
    for i in range(len(PARTS)):
        part_start[i] = acc - body_start + 1
        acc += c[f"open{i}"] + c[f"body{i}"]
    back_start = acc - body_start + 1

    # صفحات فصول الباب الأول: chunk0 = نظرة/الفصل الأول، ثم كل pagebreak = فصل
    ch0 = c["body_chunks"].get(0, [])
    # ch0[k] = عدد صفحات الكتلة k؛ الفصول تبدأ عند المجاميع التراكمية
    cum = []
    acc = 0
    for sz in ch0:
        cum.append(acc); acc += sz
    # فصول الباب الأول (6) تقابل المجاميع cum[0..5]
    p1_page = {}
    for k in range(min(6, len(cum))):
        p1_page[k] = part_start[0] + c["open0"] + cum[k]

    entries = []
    p1_idx = 0
    for search, label, lvl, loc in TOC_SPEC:
        num = None
        if loc.startswith("part:"):
            num = part_start[int(loc.split(":")[1])]
        elif loc == "back":
            num = back_start
        elif loc == "front":
            num = None
        if lvl == 2 and loc == "part:0":
            num = p1_page.get(p1_idx)
            p1_idx += 1
        entries.append((label, num, lvl))
    return entries, body_start

def toc_entries_with_p1(entries, counts):
    """يضيف أرقام فصول الباب الأول داخل المقطع body0."""
    p1_chaps = ["الجسم سيّد نفسه", "القاعدة الذهبية", "مؤشرات التكرار",
                "الأساسيات الخمسة", "يوم آه ويوم لأ", "مبادئ لتحديد الممنوعات"]
    # رقم صفحة فاتح الباب الأول منطقياً = 1
    opener0_logical = 1
    body0_abs = (counts["cover"]+counts["title"]+counts["copy"]+counts["front"]
                 +counts["toc"]+counts["open0"])
    def _norm(s):
        import unicodedata
        s = unicodedata.normalize("NFKD", s)
        out = "".join(ch for ch in s if not unicodedata.combining(ch))
        for ch in "ـ\u064b-\u065f﴿﴾«»\"' ":
            out = out.replace(ch, "")
        return out
    d = pymupdf.open("seg/05_body0.pdf")
    page_of = {}
    ti = 0
    for pg in range(len(d)):
        if ti >= len(p1_chaps): break
        if _norm(p1_chaps[ti]) in _norm(d[pg].get_text()):
            page_of[ti] = pg; ti += 1
    out = []
    for (label, num, lvl) in entries:
        if lvl == 2 and any(_norm(c) in _norm(label) for c in p1_chaps):
            # طابق الفصل المناسب
            for k, t in enumerate(p1_chaps):
                if _norm(t) in _norm(label) and k in page_of:
                    num = opener0_logical + counts["open0"] + page_of[k]
        out.append((label, num, lvl))
    return out

def add_outline_and_meta(doc, entries, body_start):
    """يضيف شارات تنقل (Bookmarks) وبيانات تعريفية للملف."""
    toc = []
    toc.append([1, "مدخل إلى هذا الكتاب", body_start - 2])   # 1-based صفحة المدخل
    toc.append([1, "سيرة الدكتور ضياء العوضي", body_start - 1])
    for label, num, lvl in entries:
        if num is None:
            continue
        page = body_start + num          # 1-based
        level = 1 if lvl == 0 else 2
        toc.append([level, label, page])
    doc.set_toc(toc)
    doc.set_metadata({
        "title": "نظام الطيبات — الدليل الشامل للغذاء الصحّي الطبيعي",
        "author": "عن رؤى الدكتور ضياء العوضي (1980–2026)",
        "subject": "نظام غذائي فلسفي علمي — نسخة معاد بناؤها تحريرياً وتصميمياً",
        "keywords": "نظام الطيبات, ضياء العوضي, تغذية, غذاء صحي",
        "creator": "نظام الطيبات",
    })
    print("outline entries:", len(toc), flush=True)

if __name__ == "__main__":
    print("== تمريرة 1 ==", flush=True)
    counts = build([(l,None,lv) for _s,l,lv,_loc in TOC_SPEC])
    doc, bs, op = assemble(do_heads=False)
    print("pages:", len(doc), "body_start:", bs, flush=True)
    entries, body_start = compute_toc(counts)
    for e in entries: print("   ", e, flush=True)
    print("== تمريرة 2 ==", flush=True)
    counts = build(entries)
    final, bs2, op2 = assemble(do_heads=True)
    add_outline_and_meta(final, entries, bs2)
    final.save("نظام-الطيبات-النسخة-الجديدة.pdf", garbage=4, deflate=True)
    print("FINAL PAGES:", len(final), flush=True)
