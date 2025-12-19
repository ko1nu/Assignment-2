# src/input.py
from __future__ import annotations

from datetime import datetime
from pathlib import Path

from storage import append_expense, ensure_csv_exists

DEFAULT_CSV_PATH = Path("data") / "expenses.csv"

def read_date() -> str:
    """
    Read date in YYYY-MM-DD format (default = today if empty).
    """
    while True:
        s = input("Date (YYYY-MM-DD) [Enter = today]: ").strip()
        if s == "":
            return datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(s, "%Y-%m-%d")
            return s
        except ValueError:
            print("❌ Invalid date format. Example: 2025-12-19")


def read_amount() -> float:
    """
    Read positive amount.
    """
    while True:
        s = input("Amount (e.g., 120.5): ").strip()
        try:
            val = float(s)
            if val <= 0:
                print("❌ Amount must be > 0")
                continue
            return val
        except ValueError:
            print("❌ Invalid number. Example: 120.5")


def read_category() -> str:
    """
    Read non-empty category.
    """
    while True:
        s = input("Category (e.g., Food/Transport/Rent): ").strip()
        if s:
            return s
        print("❌ Category cannot be empty")


def main() -> None:
    print("=== Expense Input (Member A) ===")
    print("Type 'q' at category prompt to quit.\n")

    # Ensure CSV file exists with header
    ensure_csv_exists(DEFAULT_CSV_PATH)

    while True:
        date = read_date()
        amount = read_amount()

        category = input("Category (or 'q' to quit): ").strip()
        if category.lower() == "q":
            print("👋 Bye! Data saved in:", DEFAULT_CSV_PATH)
            break
        if not category:
            print("❌ Category cannot be empty")
            continue

        notes = input("Notes (optional): ").strip()

        append_expense(DEFAULT_CSV_PATH, date=date, amount=amount, category=category, notes=notes)
        print("✅ Saved!\n")


if __name__ == "__main__":
    main()
