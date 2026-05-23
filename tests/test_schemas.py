import json
from pathlib import Path


def test_schema_files_are_valid_json():
    root = Path(__file__).resolve().parents[1]
    for path in (root / "schemas").glob("*.json"):
        with open(path, "r", encoding="utf-8") as f:
            json.load(f)
