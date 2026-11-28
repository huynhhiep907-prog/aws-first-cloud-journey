from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread
import asyncio
import os

from playwright.async_api import async_playwright
from pypdf import PdfMerger

ROOT = Path("public").resolve()
OUTPUT = Path("output/Smart-Kitchen-AWS-Workshop.pdf")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

# Hugo creates one index.html for each Workshop page and language.
pages = sorted(
    p for p in ROOT.rglob("index.html")
    if "5-workshop" in p.relative_to(ROOT).as_posix().lower()
)
if not pages:
    raise SystemExit("No generated Workshop pages found under public/.")

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

server = ThreadingHTTPServer(("127.0.0.1", 8000), QuietHandler)
Thread(target=server.serve_forever, daemon=True).start()

async def export():
    temp_dir = Path("output/pages")
    temp_dir.mkdir(parents=True, exist_ok=True)
    pdf_files = []

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 1440, "height": 1000},
            device_scale_factor=1
        )

        for index, html_file in enumerate(pages, start=1):
            relative = html_file.relative_to(ROOT).as_posix()
            url = "http://127.0.0.1:8000/" + relative
            await page.goto(url, wait_until="networkidle")
            await page.add_style_tag(content="""
                @media print {
                    #sidebar, #header-wrapper, #topbar,
                    #navigation, #chapter, .edit-this-page,
                    .nav-footer, footer, .searchbox, #searchbox {
                        display: none !important;
                    }
                    #body, #body-inner, #content, .content {
                        margin: 0 !important;
                        padding: 0 !important;
                        width: 100% !important;
                        max-width: 100% !important;
                    }
                    body { background: #fff !important; color: #111 !important; }
                    img { max-width: 100% !important; height: auto !important; }
                    pre, table, blockquote, figure, img {
                        break-inside: avoid;
                    }
                    a { color: #0645ad !important; }
                }
            """)
            await page.emulate_media(media="print")
            await page.pdf(
                path=str(temp_dir / f"{index:02d}.pdf"),
                format="A4",
                print_background=True,
                prefer_css_page_size=True,
                margin={"top": "16mm", "right": "15mm", "bottom": "16mm", "left": "15mm"}
            )
            pdf_files.append(temp_dir / f"{index:02d}.pdf")
            print(f"Exported {relative}")

        await browser.close()

    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(str(pdf))
    with OUTPUT.open("wb") as f:
        merger.write(f)
    merger.close()
    print(f"Created {OUTPUT} from {len(pages)} Workshop pages.")

try:
    asyncio.run(export())
finally:
    server.shutdown()
