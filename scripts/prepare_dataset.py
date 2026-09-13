"""Dataset preparation scaffold.

Keep raw downloaded datasets outside Git when redistribution is not permitted.
Extend this script after each source dataset's annotation schema has been audited.
"""
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
ANNOTATIONS = ROOT / "data" / "annotations"


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    ANNOTATIONS.mkdir(parents=True, exist_ok=True)
    print(f"Raw data directory: {RAW}")
    print(f"Annotations directory: {ANNOTATIONS}")
    print("Add dataset-specific preprocessing after source formats are verified.")


if __name__ == "__main__":
    main()
