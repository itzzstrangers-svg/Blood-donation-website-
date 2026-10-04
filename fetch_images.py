"""
Download one photo for every plant into  images/plants/<slug>.jpg

Run it ONCE on a computer with internet access (from the project folder):

    python fetch_images.py

* Photos come from Wikipedia / Wikimedia Commons (looked up by the plant's
  scientific name first, then by its common name).
* Plants that already have an image are skipped, so you can re-run the script
  to retry the ones that failed.
* images/plants/credits.csv lists the source page of every photo. Most of these
  photos are Creative Commons licensed and need attribution, so keep that file
  (or credit "Wikimedia Commons" in your project report / footer).
* The website works without images too: any plant without a photo simply shows
  its emoji.

Use --force to download everything again.
Only the Python standard library is used (no pip install needed).
"""

import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

from database import slugify
from plants_data import PLANTS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, "images", "plants")
CREDITS = os.path.join(OUT_DIR, "credits.csv")

HEADERS = {
    # Wikimedia asks every script to identify itself.
    "User-Agent": "NurseryIQ-student-project/1.0 (plant image downloader)"
}
SUMMARY_API = "https://en.wikipedia.org/api/rest_v1/page/summary/{}"
IMAGE_WIDTH = 640


def get(url, retries=3):
    for attempt in range(retries):
        try:
            request = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(request, timeout=25) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if error.code == 404:
                return None
            if error.code == 429:          # slow down and retry
                time.sleep(3 * (attempt + 1))
                continue
            return None
        except (urllib.error.URLError, TimeoutError):
            time.sleep(1.5 * (attempt + 1))
    return None


def lookup(title):
    """Return (image_url, page_url) for a Wikipedia article, or None."""
    data = get(SUMMARY_API.format(urllib.parse.quote(title.replace(" ", "_"))))
    if not data:
        return None

    info = json.loads(data)
    thumb = (info.get("thumbnail") or {}).get("source")
    if not thumb:
        return None

    # Ask for a larger version of the same picture.
    thumb = re.sub(r"/(\d+)px-", f"/{IMAGE_WIDTH}px-", thumb)
    page = ((info.get("content_urls") or {}).get("desktop") or {}).get("page", "")
    return thumb, page


def candidates(plant):
    scientific = plant["scientific_name"].replace("'", "").replace(" x ", " ")
    words = scientific.split()
    names = [scientific]
    if len(words) > 2:
        names.append(" ".join(words[:2]))   # drop the variety / cultivar
    names.append(plant["name"])
    names.append(plant["name"] + " plant")
    seen = []
    for name in names:
        if name not in seen:
            seen.append(name)
    return seen


def main():
    force = "--force" in sys.argv
    os.makedirs(OUT_DIR, exist_ok=True)

    credits = {}
    if os.path.exists(CREDITS):
        with open(CREDITS, newline="", encoding="utf-8") as file:
            credits = {row["slug"]: row for row in csv.DictReader(file)}

    failed = []

    for number, plant in enumerate(PLANTS, start=1):
        slug = slugify(plant["name"])
        target = os.path.join(OUT_DIR, f"{slug}.jpg")

        if os.path.exists(target) and not force:
            print(f"[{number:3}/{len(PLANTS)}] have     {plant['name']}")
            continue

        found = None
        for title in candidates(plant):
            found = lookup(title)
            time.sleep(0.2)
            if found:
                break

        picture = get(found[0]) if found else None

        if not picture:
            print(f"[{number:3}/{len(PLANTS)}] MISSING  {plant['name']}")
            failed.append(plant["name"])
            continue

        with open(target, "wb") as file:
            file.write(picture)

        credits[slug] = {
            "slug": slug,
            "plant": plant["name"],
            "image_url": found[0],
            "source_page": found[1],
        }
        print(f"[{number:3}/{len(PLANTS)}] ok       {plant['name']}")

    with open(CREDITS, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["slug", "plant", "image_url", "source_page"]
        )
        writer.writeheader()
        writer.writerows(sorted(credits.values(), key=lambda row: row["slug"]))

    print(f"\nDone. {len(PLANTS) - len(failed)} of {len(PLANTS)} plants have a photo.")
    if failed:
        print("No photo found for:", ", ".join(failed))
        print("Run the script again to retry, or save your own photo as")
        print("images/plants/<slug>.jpg (slug = lowercase name with dashes).")


if __name__ == "__main__":
    main()
