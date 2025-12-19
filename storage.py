# src/storage.py
from __future__ import annotations

import csv
import os
from pathlib import Path

CSV_HEADER = ["date", "amount", "category", "notes"]

def ensure_csv_exists(csv_path: str | os.PathLike) -> Path:
    """
    Ensure the CSV file exists and has a header row.
    Returns the resolved Path.
    """
    p = Path(csv_path)
    p.parent.mkdir(parents=True, exist_ok=True)

    if not p.exists() or p.stat().st_size == 0:
        with p.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADER)

    return p.resolve()


def append_expense(csv_path: str | os.PathLike, date: str, amount: float, category: str, notes: str = "") -> None:
    """
    Append one expense row to CSV.
    """
    p = ensure_csv_exists(csv_path)

    with p.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, f"{amount:.2f}", category, notes])
