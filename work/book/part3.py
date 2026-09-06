# -*- coding: utf-8 -*-
"""الباب الثالث: قائمة الممنوعات الكاملة."""
from helpers import *
from helpers import freq_td
from data import (BANNED, BANNED_BREAD_KINDS, BANNED_PASTRY, BANNED_BISCUITS, BAN)

def _simple_ban_table(items):
    x = ['<table class="food"><thead><tr><th>المنتج</th><th class="c" style="width:24%">الحالة</th></tr></thead><tbody>']
    for it in items:
        x.append(f'<tr><td>{it}</td>{freq_td(BAN)}</tr>')
    x.append('</tbody></table>')
    return "\n".join(x)

def part3():
    h = []
    h.append(part_opener("الباب الثالث", "قائمة الممنوعات الكاملة",
        "أكثر من 81 صنفاً موزعة على 16 فئة رئيسية، مع أسباب المنع كما ذكرها الدكتور",
        "﴿ وَيُحَرِّمُ عَلَيْهِمُ الْخَبَائِثَ ﴾",
        "سورة الأعراف — آية 157"))

    # نظرة عامة
    h.append('<section>')
    h.append(chap_title("", "نظرة عامة على الممنوعات"))
    h.append("""
<p class="lead">يقسّم النظام الأطعمة الممنوعة إلى 16 فئة أساسية. الفئة الأكبر هي الدقيق والمخبوزات، وتليها المشروبات الصناعية. والأصل الحاكم واحد: كل ما خرج عن القائمة البيضاء ممنوع حتى يثبت طيبُه.</p>
""")
    overview = [
      ("دقيق ومخبوزات ومعجنات", 35), ("مياه غازية ومشروبات صناعية", 10),
      ("خضروات ورقية ممنوعة", 12), ("خضروات ممنوعة", 7), ("ألبان ومشتقات", 4),
      ("نشويات مصنّعة", 4), ("بذور طبيعية", 3), ("أجبان ممنوعة", 3),
      ("دواجن وبيض", 2), ("طيور وبروتينات ممنوعة", 2),
      ("أسماك ومأكولات بحرية ممنوعة", 2), ("فواكه ممنوعة", 2),
      ("أدوية ومكمّلات صناعية", 2), ("عصائر طبيعية طازجة", 1), ("بقوليات", 1),
    ]
    h.append(overview_table(overview, "#b3322a"))
    h.append(box("key", "المبدأ الأساسي",
      "<p>Whitelist Only — كل ما هو خارج قائمة المسموحات ممنوع تلقائياً.</p>"))
    h.append('<p class="src">المصدر: altayebaat.com/articles — قائمة الممنوعات الكاملة (محدَّثة 1 مايو 2026).</p>')
    h.append('</section>')

    for num, title, kind, items, note in BANNED:
        # الدقيق والمخبوزات: 32 صنفاً تُقسَّم على ثلاث صفحات
        if kind == "flour":
            h.append('<section class="pagebreak">')
            h.append(chap_title(num, title, foodcat=True))
            h.append(f"<p class='small'>{note}</p>")
            h.append(subsec("أنواع الخبز الممنوعة"))
            h.append('<table class="food"><thead><tr><th>النوع</th><th style="width:55%">السبب</th></tr></thead><tbody>')
            for bread, reason in BANNED_BREAD_KINDS:
                h.append(f'<tr><td><strong>{bread}</strong></td><td class="small">{reason}</td></tr>')
            h.append('</tbody></table>')
            h.append('</section>')

            h.append('<section class="pagebreak">')
            h.append(chap_title(num, "المعجنات والمخبوزات", foodcat=True))
            h.append(_simple_ban_table(BANNED_PASTRY))
            h.append('</section>')

            h.append('<section class="pagebreak">')
            h.append(chap_title(num, "البسكويت والكوكيز", foodcat=True))
            h.append(_simple_ban_table(BANNED_BISCUITS))
            h.append(box("tip", "ما البديل؟",
              "<p>توست الحبة الكاملة (Whole Grain) فقط، وبحدود معتدلة.</p>"))
            h.append('</section>')
            continue

        h.append('<section class="pagebreak">')
        h.append(chap_title(num, title, foodcat=True))

        if kind == "dairy":
            h.append('<table class="food"><thead><tr><th>المنتج</th><th style="width:52%">السبب</th></tr></thead><tbody>')
            for p, r in [("لبن (حليب) بكل أنواعه","الكازين يتحول إلى أسيد كازينات"),
                         ("لبنة","منتج حليب"),("لبن بودرة","حتى المسحوق ممنوع"),
                         ("الزبادي بكل أنواعه","يسبب الانتفاخ")]:
                h.append(f'<tr><td><strong>{p}</strong></td><td class="small">{r}</td></tr>')
            h.append('</tbody></table>')
            h.append(box("warn", "السبب الجوهري", f"<p>{note}</p>"))

        elif kind == "cheese":
            h.append('<table class="food"><thead><tr><th>المنتج</th><th class="c" style="width:24%">الحالة</th></tr></thead><tbody>')
            for p in ["كل الأجبان البيضاء","جبنة بيضاء","جبنة قريش"]:
                h.append(f'<tr><td><strong>{p}</strong></td>{freq_td(BAN)}</tr>')
            h.append('</tbody></table>')
            h.append(box("tip", "التمييز المهم", f"<p>{note}</p>"))

        elif kind == "poultry":
            h.append('<table class="food"><thead><tr><th>المنتج</th><th style="width:52%">السبب</th></tr></thead><tbody>')
            for p, r in [("الدجاج والفراخ","يأكل من الأرض وفضلاتها، إضافة إلى الهرمونات والمضادات الحيوية"),
                         ("البيض (جميع الأنواع)","حتى البلدي والمطبوخ ممنوع")]:
                h.append(f'<tr><td><strong>{p}</strong></td><td class="small">{r}</td></tr>')
            h.append('</tbody></table>')
            h.append(box("warn", "لاحظ", f"<p>{note}</p>"))

        elif kind == "birds":
            h.append('<table class="food"><thead><tr><th>المنتج</th><th style="width:52%">السبب</th></tr></thead><tbody>')
            for p, r in [("البط / الإوز","طيور داجنة تأكل من الأرض"),
                         ("الديك الرومي","السبب نفسه")]:
                h.append(f'<tr><td><strong>{p}</strong></td><td class="small">{r}</td></tr>')
            h.append('</tbody></table>')

        elif kind == "seafood":
            h.append('<table class="food"><thead><tr><th>المنتج</th><th style="width:52%">السبب</th></tr></thead><tbody>')
            for p, r in [("الجمبري والسبيط والقشريات","ممنوعة تماماً"),
                         ("أسماك المزارع (البلطي، البوري)","تربية صناعية")]:
                h.append(f'<tr><td><strong>{p}</strong></td><td class="small">{r}</td></tr>')
            h.append('</tbody></table>')
            h.append(box("key", "المسموح", f"<p>{note}</p>"))

        elif kind == "leafy":
            h.append(_simple_ban_table(items))

        elif kind == "veggies":
            h.append('<table class="food"><thead><tr><th>المنتج</th><th style="width:52%">ملاحظة</th></tr></thead><tbody>')
            for p, r in items:
                h.append(f'<tr><td><strong>{p}</strong></td><td class="small">{r}</td></tr>')
            h.append('</tbody></table>')
            h.append(box("tip", "ملاحظة الكوسة", f"<p>{note}</p>"))

        elif kind == "fruits":
            h.append('<table class="food"><thead><tr><th>المنتج</th><th style="width:52%">السبب</th></tr></thead><tbody>')
            for p, r in [("البطيخ والشمام","محتوى ماء عالٍ يربك الجهاز الهضمي"),
                         ("البرتقال والكيوي والليمون والأفوكادو والبابايا","ممنوعة طازجة")]:
                h.append(f'<tr><td><strong>{p}</strong></td><td class="small">{r}</td></tr>')
            h.append('</tbody></table>')
            h.append(box("tip", "ملاحظة", f"<p>{note}</p>"))

        elif kind == "legumes":
            h.append('<table class="food"><thead><tr><th>المنتج</th><th class="c" style="width:24%">الحالة</th></tr></thead><tbody>')
            h.append(f'<tr><td><strong>الفول / العدس / الحمص / الفاصوليا / اللوبيا</strong></td>{freq_td(BAN)}</tr>')
            h.append('</tbody></table>')
            h.append(box("warn", "السبب", f"<p>{note}</p>"))

        elif kind == "starch":
            h.append('<table class="food"><thead><tr><th>المنتج</th><th style="width:52%">السبب</th></tr></thead><tbody>')
            for p, r in [("الحلويات الشرقية (كنافة، زلابيا)","دقيق أبيض + مواد صناعية"),
                         ("معكرونة الشوفان / العدس / القمح","حتى البديلة ممنوعة"),
                         ("الكسكسي","ممنوع"),("الكينوا","ممنوعة")]:
                h.append(f'<tr><td><strong>{p}</strong></td><td class="small">{r}</td></tr>')
            h.append('</tbody></table>')

        elif kind == "drinks":
            h.append(_simple_ban_table(items))
            h.append(box("warn", "مفاجأة كبيرة", f"<p>{note}</p>"))

        elif kind == "freshjuice":
            h.append('<table class="food"><thead><tr><th>المنتج</th><th style="width:52%">السبب</th></tr></thead><tbody>')
            h.append('<tr><td><strong>العصائر الطبيعية الفريش</strong></td><td class="small">تربك الجهاز الهضمي</td></tr>')
            h.append('</tbody></table>')
            h.append(box("key", "البديل", f"<p>{note}</p>"))

        elif kind == "seeds":
            h.append(_simple_ban_table(items))

        elif kind == "meds":
            h.append('<table class="food"><thead><tr><th>المنتج</th><th style="width:52%">الحالة / ملاحظة</th></tr></thead><tbody>')
            for p, r in [("الأدوية الكيميائية (خافض حرارة، مسكنات، فيتامينات، مكمّلات)","ممنوعة في رؤية الدكتور"),
                         ("المضادات الحيوية وأدوية الضغط والسكري والإنسولين","ممنوعة في رؤية الدكتور")]:
                h.append(f'<tr><td><strong>{p}</strong></td><td class="small">{r}</td></tr>')
            h.append('</tbody></table>')
            h.append(box("med", "تنبيه طبي حاسم",
              "<p>هذه رؤية الدكتور ضياء العوضي. <strong>لا توقف أدويتك المزمنة أبداً دون استشارة طبيبك</strong>؛ فإيقاف أدوية الضغط أو السكري فجأة قد يكون مهدداً للحياة.</p>"))

        h.append('</section>')

    h.append('<section class="pagebreak">')
    h.append(summary("خلاصة الباب الثالث",
      '<p>تضم قائمة الممنوعات أكثر من 81 صنفاً في 16 فئة، تتصدرها المخبوزات (35) ثم المشروبات الصناعية (10). الرسالة الأخيرة:</p>'
      '<p style="text-align:center;font-family:kufi;font-weight:700;color:#e8cf9a;">«الطعام الفطري النقي يبني الجسم، والمصنّع يهدمه»</p>'))
    h.append('</section>')

    return "\n".join(h)
