# -*- coding: utf-8 -*-
"""نظام التصميم (Design System) لكتاب نظام الطيبات — طبعة معاد بناؤها."""

CSS = r"""
/* ============ الخطوط ============ */
@font-face { font-family: 'naskh'; src: url(book/fonts/naskh-400.ttf); font-weight: 400; }
@font-face { font-family: 'naskh'; src: url(book/fonts/naskh-500.ttf); font-weight: 500; }
@font-face { font-family: 'naskh'; src: url(book/fonts/naskh-600.ttf); font-weight: 600; }
@font-face { font-family: 'naskh'; src: url(book/fonts/naskh-700.ttf); font-weight: 700; }
@font-face { font-family: 'kufi';  src: url(book/fonts/kufi-400.ttf); font-weight: 400; }
@font-face { font-family: 'kufi';  src: url(book/fonts/kufi-500.ttf); font-weight: 500; }
@font-face { font-family: 'kufi';  src: url(book/fonts/kufi-600.ttf); font-weight: 600; }
@font-face { font-family: 'kufi';  src: url(book/fonts/kufi-700.ttf); font-weight: 700; }
@font-face { font-family: 'kufi';  src: url(book/fonts/kufi-800.ttf); font-weight: 800; }
@font-face { font-family: 'kufi';  src: url(book/fonts/kufi-900.ttf); font-weight: 900; }
@font-face { font-family: 'amiri'; src: url(book/fonts/amiri-400.ttf); font-weight: 400; }
@font-face { font-family: 'amiri'; src: url(book/fonts/amiri-700.ttf); font-weight: 700; }

/* ============ الصفحة ============ */
@page { size: A5; margin: 20mm 15mm 18mm 15mm; }

* { box-sizing: border-box; }

html, body {
  font-family: 'naskh';
  font-size: 10pt;
  line-height: 1.66;
  color: #25302a;
  direction: rtl;
  text-align: right;
}

p { margin: 0 0 5.5pt 0; text-align: justify; text-align-last: right; }

/* ============ العناوين ============ */
h1, h2, h3, h4 { font-family: 'kufi'; color: #133320; direction: rtl; line-height: 1.35; }

/* عنوان افتتاحية القسم (Part opener) — يُرسم في صفحة مستقلة */
.partpage { background: #123822; color: #f4efe4; padding: 40pt 20pt 34pt 20pt;
  text-align: center; direction: rtl; margin: 0; }
.partpage .partno { font-family: 'kufi'; font-weight: 600; font-size: 12pt; color: #c9a25e;
  letter-spacing: 2pt; margin-bottom: 16pt; }
.partpage .partrule { width: 56pt; height: 2.2pt; background: #c9a25e; margin: 0 auto 20pt auto; }
.partpage h1 { font-family: 'kufi'; font-weight: 900; font-size: 30pt; color: #f7f2e7; margin: 0 0 14pt 0; line-height: 1.25; }
.partpage .partsub { font-family: 'naskh'; font-size: 11.5pt; color: #d8e4d6; margin: 0 auto; max-width: 88%; line-height: 1.8; }
.partpage .partverse { font-family: 'amiri'; font-size: 13pt; color: #e8d9b6; margin-top: 26pt; line-height: 1.9; }
.partpage .partverseref { font-family: 'kufi'; font-weight: 400; font-size: 9pt; color: #9db49f; margin-top: 8pt; }

/* عنوان الفصل */
h2.chap { font-size: 17pt; font-weight: 800; color: #133320; margin: 16pt 0 3pt 0;
  padding-bottom: 6pt; border-bottom: 2.4pt solid #c9a25e; page-break-after: avoid; }
h2.chap .cno { color: #c9a25e; font-weight: 800; margin-left: 6pt; }

/* عنوان فرعي */
h3.sec { font-size: 12.6pt; font-weight: 700; color: #1d5b38; margin: 10pt 0 3pt 0; page-break-after: avoid; }
h3.sec::before { content: " "; color: #c9a25e; }

h4.subsec { font-size: 10.6pt; font-weight: 700; color: #35633f; margin: 9pt 0 3pt 0; font-family: 'naskh'; page-break-after: avoid; }

/* أهداف الفصل */
.objectives { background: #f2f6f1; border: 0.7pt solid #d6e2d4; border-right: 3.2pt solid #2f6b43;
  padding: 9pt 12pt; margin: 8pt 0 12pt 0; border-radius: 3pt; page-break-inside: avoid; }
.objectives .otitle { font-family: 'kufi'; font-weight: 700; font-size: 9.6pt; color: #2f6b43; margin-bottom: 4pt; }
.objectives p { margin: 0 0 2pt 0; font-size: 9.6pt; }

/* ============ صناديق التنبيه ============ */
.box { padding: 8pt 11pt; margin: 7pt 0; border-radius: 3pt; page-break-inside: avoid; font-size: 9.7pt; }
.box .btitle { font-family: 'kufi'; font-weight: 700; font-size: 9.8pt; margin-bottom: 3pt; display: block; }
.box p { margin: 0 0 3pt 0; font-size: 9.7pt; }
.box p:last-child { margin-bottom: 0; }

.box.key { background: #f1f7f2; border: 0.7pt solid #cfe3d3; border-right: 3.2pt solid #2f6b43; }
.box.key .btitle { color: #1f5b36; }
.box.warn { background: #fdf3ee; border: 0.7pt solid #f2d6c8; border-right: 3.2pt solid #c05a2c; }
.box.warn .btitle { color: #b34a22; }
.box.tip { background: #f8f5ec; border: 0.7pt solid #e6dcc2; border-right: 3.2pt solid #c9a25e; }
.box.tip .btitle { color: #9a7d34; }
.box.med { background: #fdeeea; border: 1pt solid #e0a995; border-right: 3.6pt solid #c0392b; }
.box.med .btitle { color: #b3322a; }
.box.note { background: #eef4f6; border: 0.7pt solid #cfe0e6; border-right: 3.2pt solid #3d7d8c; }
.box.note .btitle { color: #2f6471; }

/* اقتباس */
.quote { margin: 9pt 0; padding: 10pt 14pt; background: #f6f4ee; border-right: 3.2pt solid #c9a25e;
  border-radius: 2pt; page-break-inside: avoid; }
.quote .qtext { font-family: 'amiri'; font-size: 12pt; color: #1d3a28; line-height: 1.9; }
.quote .qattr { font-family: 'kufi'; font-weight: 600; font-size: 8.8pt; color: #8a7a52; margin-top: 6pt; text-align: left; }

/* آية قرآنية */
.verse { text-align: center; margin: 12pt 0; padding: 6pt; direction: rtl; }
.verse .vtext { font-family: 'amiri'; font-size: 15pt; color: #143723; line-height: 2.1; }
.verse .vref { font-family: 'kufi'; font-weight: 500; font-size: 8.8pt; color: #c9a25e; margin-top: 4pt; }

/* ============ الجداول ============ */
table { width: 100%; border-collapse: collapse; direction: rtl; margin: 7pt 0 10pt 0;
  font-size: 9.3pt; line-height: 1.5; page-break-inside: avoid; }
thead { display: table-header-group; }
tr { page-break-inside: avoid; }
th { font-family: 'kufi'; font-weight: 700; font-size: 8.8pt; color: #f4efe4; background: #1d5b38;
  padding: 5pt 6pt; text-align: right; border: 0.6pt solid #1d5b38; }
td { padding: 4.6pt 6pt; border: 0.6pt solid #d8e0d6; vertical-align: middle; text-align: right; }
tbody tr:nth-child(even) { background: #f4f8f3; }
td.c, th.c { text-align: center; }
.tblcap { font-family: 'kufi'; font-weight: 700; font-size: 10pt; color: #1d5b38; margin: 10pt 0 2pt 0; }

/* جداول القوائم الغذائية (مدمجة لتحتل صفحة واحدة) */
table.food { font-size: 8.5pt; margin: 4pt 0 5pt 0; line-height: 1.35; }
table.food th { padding: 3.6pt 5pt; font-size: 8.2pt; }
table.food td { padding: 2.9pt 5pt; line-height: 1.35; }
table.food td.small { font-size: 8.1pt; line-height: 1.35; }
h2.chap.foodcat { font-size: 13.5pt; margin: 6pt 0 1pt 0; padding-bottom: 3pt; }

/* خلايا التكرار والحالة الملوّنة */
td.freq { text-align: center; font-family: 'kufi'; font-weight: 700; font-size: 8pt; color: #fff;
  white-space: nowrap; padding: 4.6pt 3pt; }
td.f-daily2 { background: #1e7a46; }
td.f-daily  { background: #3a9d5d; }
td.f-week   { background: #b78b2f; }
td.f-some   { background: #6f5ba5; }
td.f-alt    { background: #2f6f9e; }
td.f-ban    { background: #b3322a; }
td.f-ok     { background: #1e7a46; }

/* جدول البدائل */
table.alt td.from { width: 42%; color: #8a3b30; font-weight: 600; background: #fbf3f1; }
table.alt td.to   { color: #2c5b39; font-weight: 600; }

/* ============ القوائم ============ */
ul, ol { margin: 4pt 0 7pt 0; padding-right: 16pt; direction: rtl; }
li { margin: 0 0 2.8pt 0; padding-right: 2pt; }
ul.tick { list-style: none; padding-right: 4pt; }
ul.tick li { padding-right: 16pt; position: relative; }
ul.tick li::before { content: "\2022"; color: #2f7a48; font-weight: 900; font-size: 13pt; position: absolute; right: 0; top: -2pt; font-family: 'kufi'; }
ul.cross { list-style: none; padding-right: 4pt; }
ul.cross li { padding-right: 16pt; position: relative; }
ul.cross li::before { content: "\00D7"; color: #c0392b; font-weight: 700; font-size: 13pt; position: absolute; right: 0; top: -1pt; font-family: 'kufi'; }
ul.dot li::marker { color: #c9a25e; }
ol.steps { padding-right: 20pt; }
ol.steps li { margin-bottom: 3.5pt; }
ol.steps li::marker { color: #1d5b38; font-weight: 700; font-family: 'kufi'; }

/* خطوات مرقّمة داخل صندوق */
.stepgrid { width: 100%; direction: rtl; margin: 4pt 0; }
.stepnum { font-family: 'kufi'; font-weight: 800; color: #fff; background: #2f6b43; width: 16pt; height: 16pt;
  border-radius: 50%; text-align: center; font-size: 9pt; padding-top: 1.4pt; }

/* ملخص الفصل */
.summary { background: #123822; color: #e7eee6; padding: 11pt 14pt; margin: 14pt 0 6pt 0;
  border-radius: 3pt; page-break-inside: avoid; }
.summary .stitle { font-family: 'kufi'; font-weight: 800; font-size: 10.5pt; color: #e8cf9a; margin-bottom: 5pt; }
.summary p { color: #dfe8dd; font-size: 9.5pt; margin-bottom: 3pt; }
.summary ul { margin: 2pt 0 0 0; }
.summary li { color: #dfe8dd; font-size: 9.5pt; }

/* تمرين / تطبيق */
.apply { border: 1pt dashed #c9a25e; background: #fbf8f0; padding: 10pt 13pt; margin: 10pt 0; border-radius: 3pt; page-break-inside: avoid; }
.apply .atitle { font-family: 'kufi'; font-weight: 700; color: #9a7d34; font-size: 10pt; margin-bottom: 4pt; }
.apply p, .apply li { font-size: 9.6pt; }

.small { font-size: 8.6pt; color: #5c6b60; }
.src { font-family: 'kufi'; font-weight: 500; font-size: 8.2pt; color: #7a8a7e; margin: 4pt 0 10pt 0; }
.hr-gold { width: 100%; height: 1pt; background: #e2d7bb; border: none; margin: 12pt 0; }
.pagebreak { page-break-before: always; }
.avoid { page-break-inside: avoid; }
.lead { font-size: 10.8pt; color: #33403a; }
.kicker { font-family: 'kufi'; font-weight: 700; font-size: 9pt; color: #c9a25e; letter-spacing: 1pt; margin-bottom: 2pt; }
.center { text-align: center; }
"""
