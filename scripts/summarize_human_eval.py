#!/usr/bin/env python3
"""Summarize diagnostic-label human evaluation annotations."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from statistics import mean, pstdev


METRICS = ["Relevance", "Specificity", "Completeness"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path, help="Path to human_evaluated_labels.csv")
    args = parser.parse_args()

    rows = []
    with args.csv_path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if all(row.get(metric, "").strip() for metric in METRICS):
                rows.append(row)

    if not rows:
        print("No scored rows found.")
        return 1

    print(f"Scored rows: {len(rows)}")
    for metric in METRICS:
        values = [int(row[metric]) for row in rows]
        print(f"{metric}: mean={mean(values):.3f}, std={pstdev(values):.3f}")

    hallucinations = [
        row
        for row in rows
        if any(int(row[metric]) <= 1 for metric in METRICS)
    ]
    print(f"Rows with any score <= 1: {len(hallucinations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
