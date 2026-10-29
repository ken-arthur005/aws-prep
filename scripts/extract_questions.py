"""Local, offline Windows OCR. Selected answer marks are deliberately not interpreted.

Run with Python 3.12 and PyWinRT Windows.Media.Ocr, Graphics.Imaging,
Storage, Globalization, Foundation and Storage.Streams packages installed.
The output preserves word coordinates for reproducible layout-aware parsing.
"""
import asyncio
import json
import sys
from pathlib import Path

from winrt.windows.globalization import Language
from winrt.windows.graphics.imaging import BitmapDecoder
from winrt.windows.media.ocr import OcrEngine
from winrt.windows.storage import FileAccessMode, StorageFile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "ocr.json"


async def main():
    engine = OcrEngine.try_create_from_language(Language("en-US"))
    if engine is None:
        raise RuntimeError("Windows English OCR language pack is required")
    files = sorted((ROOT / "public" / "questions").glob("*.png"))
    if len(sys.argv) > 1:
        files = files[:int(sys.argv[1])]
    existing = json.loads(OUTPUT.read_text(encoding="utf-8")) if OUTPUT.exists() else []
    done = {item["source"] for item in existing}
    for index, path in enumerate(files):
        if path.name in done:
            continue
        try:
            file = await StorageFile.get_file_from_path_async(str(path))
            stream = await file.open_async(FileAccessMode.READ)
            decoder = await BitmapDecoder.create_async(stream)
            bitmap = await decoder.get_software_bitmap_async()
            result = await engine.recognize_async(bitmap)
            lines = []
            for line in result.lines:
                words = []
                for word in line.words:
                    box = word.bounding_rect
                    words.append({"text": word.text, "x": round(box.x, 1), "y": round(box.y, 1), "w": round(box.width, 1), "h": round(box.height, 1)})
                lines.append({"text": line.text, "words": words})
            existing.append({"source": path.name, "width": decoder.pixel_width, "height": decoder.pixel_height, "lines": lines})
            stream.close()
            bitmap.close()
        except Exception as error:
            print(f"ERROR {path.name}: {error}", flush=True)
            existing.append({"source": path.name, "error": str(error), "lines": []})
        if (index + 1) % 25 == 0 or index == len(files) - 1:
            OUTPUT.parent.mkdir(exist_ok=True)
            OUTPUT.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"OCR {index + 1}/{len(files)}", flush=True)


asyncio.run(main())
