# -*- coding: utf-8 -*-
"""رسم الغلاف الأمامي والخلفي والصفحات الخاصة باستخدام PyMuPDF مباشرة."""
import pymupdf

GREEN = (0.07, 0.22, 0.13)      # #123822
GREEN_D = (0.045, 0.15, 0.09)
GOLD  = (0.79, 0.64, 0.37)      # #c9a25e
CREAM = (0.96, 0.94, 0.89)      # #f4efe4
WHITE = (1, 1, 1)

F_KUFI_B = "fonts/kufi-900.ttf"
F_KUFI   = "fonts/kufi-700.ttf"
F_KUFI_M = "fonts/kufi-500.ttf"
F_NASKH  = "fonts/naskh-500.ttf"
F_AMIRI  = "fonts/amiri-400.ttf"

def _tb(page, rect, html, arch):
    page.insert_htmlbox(rect, html, archive=arch, css="*{}")

def cover_front(path, arch):
    doc = pymupdf.open()
    page = doc.new_page(width=420, height=595)  # A5
    r = page.rect
    # خلفية
    page.draw_rect(r, color=None, fill=GREEN)
    # إطار ذهبي
    page.draw_rect(pymupdf.Rect(20,20,r.width-20,r.height-20), color=GOLD, width=1.4, fill=None)
    page.draw_rect(pymupdf.Rect(26,26,r.width-26,r.height-26), color=GOLD, width=0.4, fill=None)
    # شريط زخرفي علوي وسفلي
    page.draw_rect(pymupdf.Rect(26, 26, r.width-26, 30), color=None, fill=GOLD)
    page.draw_rect(pymupdf.Rect(26, r.height-30, r.width-26, r.height-26), color=None, fill=GOLD)

    cx = r.width/2
    # البسملة
    _tb(page, pymupdf.Rect(40, 60, r.width-40, 110),
        f'<div style="text-align:center;font-family:amiri;font-size:15pt;color:rgb(232,217,182);direction:rtl;">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>', arch)

    # خط فاصل ذهبي صغير
    page.draw_rect(pymupdf.Rect(cx-30, 135, cx+30, 137), color=GOLD, fill=GOLD)

    # العنوان الرئيسي
    _tb(page, pymupdf.Rect(34, 150, r.width-34, 250),
        '<div style="text-align:center;font-family:kufib;font-size:46pt;color:rgb(247,242,231);line-height:1.2;direction:rtl;">نِظَام<br>الطَّيِّبَات</div>', arch)

    # العنوان الفرعي
    _tb(page, pymupdf.Rect(44, 262, r.width-44, 310),
        '<div style="text-align:center;font-family:kufi;font-size:13.5pt;color:rgb(201,162,94);direction:rtl;line-height:1.6;">الدليل الشامل للغذاء الصحّي الطبيعي</div>', arch)

    # آية
    _tb(page, pymupdf.Rect(48, 330, r.width-48, 400),
        '<div style="text-align:center;font-family:amiri;font-size:13pt;color:rgb(216,228,214);direction:rtl;line-height:2;">﴿ كُلُوا مِن طَيِّبَاتِ مَا رَزَقْنَاكُمْ ﴾</div>', arch)

    # شارة العددين
    badge = pymupdf.Rect(cx-120, 430, cx+120, 478)
    page.draw_rect(badge, color=GOLD, width=1.0, fill=None)
    _tb(page, badge,
        '<div style="text-align:center;font-family:kufim;font-size:10.5pt;color:rgb(240,230,210);direction:rtl;line-height:1.7;">89+ صنفاً مسموحاً &nbsp;•&nbsp; 81+ صنفاً ممنوعاً<br>مع البدائل وخطة التطبيق</div>', arch)

    # المؤلف
    _tb(page, pymupdf.Rect(40, 500, r.width-40, 545),
        '<div style="text-align:center;font-family:kufi;font-size:11pt;color:rgb(247,242,231);direction:rtl;line-height:1.7;">عن رؤى الدكتور<br><b>ضياء العوضي</b> (1980 – 2026)</div>', arch)
    doc.save(path)
    doc.close()

def back_cover(path, arch):
    doc = pymupdf.open()
    page = doc.new_page(width=420, height=595)
    r = page.rect
    page.draw_rect(r, color=None, fill=GREEN_D)
    page.draw_rect(pymupdf.Rect(20,20,r.width-20,r.height-20), color=GOLD, width=1.2, fill=None)

    _tb(page, pymupdf.Rect(48, 70, r.width-48, 120),
        '<div style="text-align:center;font-family:kufib;font-size:20pt;color:rgb(232,207,154);direction:rtl;">كلمة أخيرة</div>', arch)
    _tb(page, pymupdf.Rect(52, 145, r.width-52, 300),
        '<div style="text-align:center;font-family:naskh;font-size:11.5pt;color:rgb(223,232,221);direction:rtl;line-height:2;">'
        'هذا الكتاب صدقةٌ جارية على روح الدكتور ضياء العوضي، رحمه الله. '
        'محتواه مستخرج من قاعدة البيانات الرسمية، ويُصرَّح بمشاركته ونشره دون تعديل '
        'ابتغاءَ الأجر وخدمةً للناس. والموقع الرسمي هو المرجع المحدَّث دائماً.</div>', arch)

    # فاصل ذهبي زخرفي بدل اسم الموقع
    cx = r.width/2
    page.draw_rect(pymupdf.Rect(cx-36, 350, cx+36, 352.4), color=GOLD, fill=GOLD)
    page.draw_rect(pymupdf.Rect(cx-4, 348, cx+4, 354.4), color=GOLD, fill=GOLD)

    _tb(page, pymupdf.Rect(52, 420, r.width-52, 480),
        '<div style="text-align:center;font-family:naskh;font-size:9.5pt;color:rgb(180,195,182);direction:rtl;line-height:1.9;">'
        'محتوى تثقيفي يعرض رؤية الدكتور ضياء العوضي، ولا يُعدّ بديلاً عن الاستشارة الطبية. '
        'لا توقف أي دواء مزمن دون إشراف طبيبك المعالج.</div>', arch)

    _tb(page, pymupdf.Rect(48, 520, r.width-48, 550),
        '<div style="text-align:center;font-family:kufim;font-size:9pt;color:rgb(160,180,165);direction:rtl;">الطبعة الإلكترونية الثانية — 1447 هـ / 2026 م</div>', arch)
    doc.save(path)
    doc.close()

def title_page(path, arch):
    doc = pymupdf.open()
    page = doc.new_page(width=420, height=595)
    r = page.rect
    cx = r.width/2
    page.draw_rect(pymupdf.Rect(0,0,r.width,8), color=None, fill=GOLD)
    page.draw_rect(pymupdf.Rect(0,r.height-8,r.width,r.height), color=None, fill=GOLD)
    _tb(page, pymupdf.Rect(40, 150, r.width-40, 250),
        '<div style="text-align:center;font-family:kufib;font-size:40pt;color:rgb(18,56,34);direction:rtl;line-height:1.25;">نِظَام الطَّيِّبَات</div>', arch)
    _tb(page, pymupdf.Rect(44, 268, r.width-44, 310),
        '<div style="text-align:center;font-family:kufi;font-size:13pt;color:rgb(154,125,52);direction:rtl;">الدليل الشامل للغذاء الصحّي الطبيعي</div>', arch)
    page.draw_rect(pymupdf.Rect(cx-34, 330, cx+34, 332), color=GOLD, fill=GOLD)
    _tb(page, pymupdf.Rect(44, 350, r.width-44, 420),
        '<div style="text-align:center;font-family:naskh;font-size:11pt;color:rgb(40,55,46);direction:rtl;line-height:2;">إعداد وتوثيق<br><b>من القوائم الرسمية لنظام الطيبات</b><br>تخليداً لعلم الدكتور ضياء العوضي (رحمه الله)</div>', arch)
    _tb(page, pymupdf.Rect(44, 500, r.width-44, 530),
        '<div style="text-align:center;font-family:kufim;font-size:10pt;color:rgb(90,105,96);direction:rtl;">الطبعة الإلكترونية الثانية — 1447 هـ / 2026 م</div>', arch)
    doc.save(path)
    doc.close()

def copyright_page(path, arch):
    doc = pymupdf.open()
    page = doc.new_page(width=420, height=595)
    r = page.rect
    html = (
      '<div style="font-family:naskh;font-size:9.5pt;color:rgb(60,72,64);direction:rtl;line-height:2.1;">'
      '<p style="text-align:center;font-family:kufi;font-size:11pt;color:rgb(18,56,34);"><b>حقوق النشر والمشاركة</b></p>'
      '<p>هذا الكتاب مُستخرَج بالكامل من القوائم الرسمية الموثّقة لنظام الطيبات، '
      'وليس من تأليف أو اجتهاد شخصي. وهو توثيقٌ لعلم الدكتور ضياء العوضي (رحمه الله).</p>'
      '<p><b>يُصرَّح بمشاركة هذا الكتاب ونشره بحرية تامة دون تعديل</b>، ابتغاءَ الأجر للدكتور رحمه الله وخدمةً للناس. '
      'جميع المحتويات مأخوذة من المصادر الرسمية الموثّقة، ويُنصَح بمراجعتها للاطلاع على التحديثات المستمرة.</p>'
      '<p style="color:rgb(179,50,42);"><b>تنبيه طبي:</b> هذا الدليل تعريفي تثقيفي يعرض رؤية الدكتور ضياء العوضي، '
      'ولا يُعدّ بديلاً عن مراجعة الطبيب المختص. علم التغذية الحديث يختلف مع النظام في بعض نقاطه. '
      'لا توقف أي دواء مزمن ولا تعدّل جرعاته دون استشارة طبيبك.</p>'
      '<p style="text-align:center;color:rgb(120,135,124);font-size:8.5pt;margin-top:18pt;">'
      'الطبعة الإلكترونية الثانية — 1447 هـ / 2026 م</p>'
      '</div>'
    )
    _tb(page, pymupdf.Rect(56, 150, r.width-56, 430), html, arch)
    doc.save(path)
    doc.close()
