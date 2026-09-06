# -*- coding: utf-8 -*-
"""الباب الثاني: قائمة المسموحات الكاملة."""
from helpers import *
from helpers import freq_td
from data import ALLOWED

def part2():
    h = []
    h.append(part_opener("الباب الثاني", "قائمة المسموحات الكاملة",
        "أكثر من 89 صنفاً موزعة على 18 فئة رئيسية — بالنص الحرفي من قاعدة البيانات الرسمية",
        "﴿ كُلُوا مِن طَيِّبَاتِ مَا رَزَقْنَاكُمْ ﴾",
        "سورة طه — آية 81"))

    h.append('<section>')
    h.append(chap_title("", "نظرة عامة على المسموحات"))
    h.append("""
<p class="lead">يقسّم النظام الأطعمة المسموحة إلى 18 فئة أساسية يزيد مجموع أصنافها على التسعة والثمانين. الجدول الآتي يلخّص الفئات وعدد الأصناف.</p>
""")
    overview = [
      ("فواكه وعصائر طبيعية", 15), ("لحوم وبروتينات", 11), ("أجبان مسموحة (معتّقة)", 9),
      ("حلويات ومربّيات", 8), ("نشويات وحبوب", 7), ("أساسيات وبهارات طبيعية", 6),
      ("مكسرات وبذور وزيوت", 6), ("مشروبات ساخنة وأعشاب", 3), ("زيوت طبيعية وخل", 3),
      ("علاجات طبيعية", 3), ("طيور مسموحة", 3), ("خضروات", 3), ("نشويات مصنّعة", 3),
      ("أسماك وبروتين بحري", 2), ("عسل ومنتجات نحل", 2), ("عصائر مسموحة", 2),
      ("دهون طبيعية", 2), ("التمور والفواكه المجففة", 1),
    ]
    h.append(overview_table(overview, "#1d5b38"))
    h.append('<p class="src">المصدر: altayebaat.com/articles — قائمة المسموحات الكاملة (محدَّثة 1 مايو 2026).</p>')
    h.append(box("tip", "كيف تقرأ القوائم",
      tick([
        "كل صنف مرفوق بوسم لوني يحدد تكرار تناوله (راجع مؤشرات التكرار في الباب الأول).",
        "الأساسيات الخمسة تُؤكل يومياً بلا حدود؛ وما عداها بحسب وسمه، والبروتين الحيواني يخضع لقاعدة «يوم آه ويوم لأ».",
      ])))
    h.append('</section>')

    for num, title, rows, note in ALLOWED:
        h.append('<section class="pagebreak">')
        h.append(chap_title(num, title, foodcat=True))
        h.append('<table class="food"><thead><tr><th>المنتج</th><th class="c" style="width:24%">التكرار</th><th style="width:42%">ملاحظات</th></tr></thead><tbody>')
        for prod, tag, note_txt in rows:
            h.append(f'<tr><td><strong>{prod}</strong></td>{freq_td(tag)}<td class="small">{note_txt}</td></tr>')
        h.append('</tbody></table>')
        if note:
            h.append(box("tip", "ملاحظة مهمة", f"<p>{note}</p>"))
        h.append('</section>')

    h.append('<section class="pagebreak">')
    h.append(summary("خلاصة الباب الثاني",
      "<p>تقدّم المسموحات غذاءً متنوعاً يزيد على 89 صنفاً في 18 فئة. بالالتزام بالأساسيات الخمسة يومياً، وقاعدة «يوم آه ويوم لأ»، ومؤشرات التكرار — يكتمل نظام متكامل ومغذٍّ بلا حرمان.</p>"))
    h.append('</section>')

    return "\n".join(h)
