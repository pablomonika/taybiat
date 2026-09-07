# -*- coding: utf-8 -*-
import http.server, os, urllib.parse, socketserver
BASE = os.path.dirname(os.path.abspath(__file__)); PDF="book.pdf"
AR_NAME="نظام-الطيبات-النسخة-المعاد-بناؤها.pdf"
LANDING="""<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>تحميل الكتاب</title><style>
 body{font-family:system-ui,Tahoma,sans-serif;background:#123822;color:#f4efe4;display:flex;min-height:100vh;
 align-items:center;justify-content:center;margin:0;text-align:center}
 .card{background:#0e2c1b;border:2px solid #c9a25e;border-radius:14px;padding:40px 34px;max-width:460px}
 h1{font-size:21px;margin-bottom:6px} p{color:#bcd0c0;font-size:14px;line-height:1.9}
 a.btn{display:inline-block;margin-top:18px;background:#c9a25e;color:#241a05;font-weight:800;text-decoration:none;
 font-size:19px;padding:16px 30px;border-radius:10px}
 a.sec{display:inline-block;margin-top:14px;color:#c9a25e;font-size:14px}
</style></head><body><div class="card">
 <h1>نظام الطيبات — النسخة المعاد بناؤها</h1>
 <p>102 صفحة · A5 · PDF جاهز للطباعة</p>
 <a class="btn" href="/download">⬇ اضغط هنا لتحميل الكتاب (PDF)</a><br>
 <a class="sec" href="/read">أو افتح المعاينة بالصور ←</a>
</div><script>setTimeout(function(){window.location='/download';},900);</script></body></html>"""
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s,*a,**k): super().__init__(*a,directory=BASE,**k)
    def _pdf(s):
        data=open(os.path.join(BASE,PDF),"rb").read(); s.send_response(200)
        s.send_header("Content-Type","application/pdf")
        s.send_header("Content-Disposition",'attachment; filename="Tayyibat-Book.pdf"; filename*=UTF-8\'\''+urllib.parse.quote(AR_NAME))
        s.send_header("Content-Length",str(len(data))); s.send_header("Cache-Control","no-store"); s.end_headers(); s.wfile.write(data)
    def do_GET(s):
        p=urllib.parse.urlparse(s.path).path
        if p in ("/download","/book.pdf"): return s._pdf()
        if p in ("/","/index.html"):
            b=LANDING.encode(); s.send_response(200); s.send_header("Content-Type","text/html; charset=utf-8")
            s.send_header("Content-Length",str(len(b))); s.end_headers(); s.wfile.write(b); return
        if p in ("/read","/read/"): s.path="/reader.html"
        return super().do_GET()
    def log_message(s,*a): pass
with socketserver.TCPServer(("0.0.0.0",8000),H) as hd:
    print("Serving on 8000"); hd.serve_forever()
