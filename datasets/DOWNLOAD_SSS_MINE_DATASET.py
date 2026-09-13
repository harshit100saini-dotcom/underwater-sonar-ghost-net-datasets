"""Download the verified Figshare side-scan sonar dataset.

The dataset is ~585 MB and contains 1,170 real SSS images.
Source: https://figshare.com/articles/dataset/_i_Side-scan_sonar_imaging_for_Mine_detection_i_/24574879
License: CC BY 4.0

Run from the repository root:
    python datasets/DOWNLOAD_SSS_MINE_DATASET.py

The script downloads the public Figshare article archive; it does not upload
third-party data to GitHub.
"""

from pathlib import Path
import requests

ARTICLE_ID = 24574879
OUT = Path("data/raw/sss-mine-detection")
API = f"https://api.figshare.com/v2/articles/{ARTICLE_ID}"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    meta = requests.get(API, timeout=30)
    meta.raise_for_status()
    article = meta.json()
    files = article.get("files", [])
    if not files:
        raise RuntimeError("Figshare returned no files for the dataset.")

    for f in files:
        url = f["download_url"]
        target = OUT / f["name"]
        if target.exists() and target.stat().st_size == f.get("size", -1):
            print(f"Already downloaded: {target}")
            continue
        print(f"Downloading {f['name']} -> {target}")
        with requests.get(url, stream=True, timeout=60) as r:
            r.raise_for_status()
            with target.open("wb") as out:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        out.write(chunk)
        print(f"Saved: {target}")


if __name__ == "__main__":
    main()
