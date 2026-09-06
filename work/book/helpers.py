# -*- coding: utf-8 -*-
"""دوال بناء HTML المشتركة."""

def part_opener(num, title, sub, verse=None, verseref=None):
    v = ""
    if verse:
        v = f'<div class="partverse">{verse}</div><div class="partverseref">{verseref or ""}</div>'
    return f"""
<section class="partpage">
  <div class="partno">{num}</div>
  <div class="partrule"></div>
  <h1>{title}</h1>
  <div class="partsub">{sub}</div>
  {v}
</section>
"""

def chap_title(num, title, foodcat=False):
    n = f'<span class="cno">{num}</span>' if num else ""
    cls = "chap foodcat" if foodcat else "chap"
    return f'<h2 class="{cls}">{n}{title}</h2>'

def sec(title):
    return f'<h3 class="sec">{title}</h3>'

def subsec(title):
    return f'<h4 class="subsec">{title}</h4>'

def box(kind, title, body):
    return f'<div class="box {kind}"><span class="btitle">{title}</span>{body}</div>'

def quote(text, attr):
    return f'<div class="quote"><div class="qtext">{text}</div><div class="qattr">{attr}</div></div>'

def verse(text, ref):
    return f'<div class="verse"><div class="vtext">{text}</div><div class="vref">{ref}</div></div>'

def objectives(items_html):
    return f'<div class="objectives"><div class="otitle">أهداف هذا الفصل</div>{items_html}</div>'

def summary(title, body):
    return f'<div class="summary"><div class="stitle">{title}</div>{body}</div>'

def apply_box(title, body):
    return f'<div class="apply"><div class="atitle">{title}</div>{body}</div>'

def li(items):
    return "<ul class='dot'>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def tick(items):
    return "<ul class='tick'>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def cross(items):
    return "<ul class='cross'>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def steps(items):
    return "<ol class='steps'>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

# خلايا التكرار/الحالة الملوّنة (بلا inline-block تفادياً لخلل التصفح)
_FREQ = {
  "daily2": ("f-daily2", "يومي بلا حدود"),
  "daily":  ("f-daily",  "يومي"),
  "week":   ("f-week",   "أسبوعي"),
  "some":   ("f-some",   "أحياناً"),
  "alt":    ("f-alt",    "يوم آه ويوم لأ"),
  "ban":    ("f-ban",    "ممنوع"),
  "ok":     ("f-ok",     "مسموح"),
}
def freq_td(key):
    cls, txt = _FREQ[key]
    return f'<td class="freq {cls}">{txt}</td>'

def overview_table(items, count_color="#1d5b38"):
    """جدول نظرة عامة بعمودين (فئة/عدد) مزدوجين لتوفير المساحة."""
    n = len(items)
    half = (n + 1) // 2
    x = ['<table class="food"><thead><tr><th>الفئة</th><th class="c" style="width:12%">العدد</th>'
         '<th style="width:40%">الفئة</th><th class="c" style="width:12%">العدد</th></tr></thead><tbody>']
    for i in range(half):
        r = items[i]
        l = items[i+half] if i+half < n else ("", "")
        rcell = f'<td><strong>{r[0]}</strong></td><td class="c"><strong style="color:{count_color};">{r[1]}</strong></td>'
        if l[0]:
            lcell = f'<td><strong>{l[0]}</strong></td><td class="c"><strong style="color:{count_color};">{l[1]}</strong></td>'
        else:
            lcell = '<td></td><td></td>'
        x.append(f'<tr>{rcell}{lcell}</tr>')
    x.append('</tbody></table>')
    return "\n".join(x)
