#!/usr/bin/env python3
"""Check whether local non-Git artifacts needed for paper reproduction exist."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_PATHS = [
    "data/filtered_final_label_case_df.csv",
    "data/filtered_pub_yr.json",
    "data/merged_extracted_sex.json",
    "pmc_llmExtraction_v8",
    "pmc_llmExtraction_v10",
]

EMBEDDING_FILES = [
    "CVS_embeddings.npz",
    "DERM_embeddings.npz",
    "EENT_embeddings.npz",
    "ENDO_embeddings.npz",
    "GI_embeddings.npz",
    "GU_embeddings.npz",
    "History_embeddings.npz",
    "Lab_Image_embeddings.npz",
    "LYMPH_embeddings.npz",
    "MSK_embeddings.npz",
    "Neuro_embeddings.npz",
    "Pregnancy_embeddings.npz",
    "RESP_embeddings.npz",
    "Vitals_Hema_embeddings.npz",
]


def describe(path: Path) -> str:
    if not path.exists():
        return "missing"
    if path.is_dir():
        count = sum(1 for _ in path.rglob("*"))
        return f"present directory ({count} entries)"
    size_mb = path.stat().st_size / 1024 / 1024
    return f"present file ({size_mb:.2f} MB)"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository or artifact root.")
    args = parser.parse_args()

    root = args.root.resolve()
    missing = []

    print(f"Artifact root: {root}")
    print("\nCore artifacts")
    for rel in REQUIRED_PATHS:
        path = root / rel
        status = describe(path)
        print(f"- {rel}: {status}")
        if status == "missing":
            missing.append(rel)

    print("\nEmbedding artifacts")
    for filename in EMBEDDING_FILES:
        rel = f"embeddings/{filename}"
        path = root / rel
        status = describe(path)
        print(f"- {rel}: {status}")
        if status == "missing":
            missing.append(rel)

    if missing:
        print("\nMissing artifacts:")
        for rel in missing:
            print(f"- {rel}")
        print("\nSee docs/artifact_inventory.md for expected sources.")
        return 1

    print("\nAll expected local artifacts are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
