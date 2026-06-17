[![Paper](https://img.shields.io/badge/Paper-BioNLP%202025-blue)](https://aclanthology.org/2025.bionlp-1.22/)
[![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-yellow?logo=huggingface)](https://huggingface.co/datasets/cxyzhang/CaseReportCollective_V1.0)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/Dataset-CC--BY--NC--4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Code License: MIT](https://img.shields.io/badge/Code-MIT-green.svg)](https://opensource.org/licenses/MIT)

# CaseReportCollective

CaseReportCollective is a large-scale dataset of 85,961 open-access medical case reports automatically structured using large language models. The dataset was introduced in:

**Zhang XYC, Wasserman W, Fong M, Zhu J. CaseReportCollective: A Large-Scale LLM-Extracted Dataset for Structured Medical Case Reports. BioNLP 2025.**

## Overview

Medical case reports contain rich clinical narratives describing rare, unusual, and diagnostically challenging conditions. Their free-text format limits large-scale computational analysis.

CaseReportCollective converts these narratives into structured clinical representations across 14 patient-assessment categories, enabling biomedical information extraction, retrieval, demographic analysis, and clinical NLP research.

## Dataset Access

The dataset is available on Hugging Face:

`cxyzhang/CaseReportCollective_V1.0`

Each record contains:

- PMCID
- Publication year
- Age group
- Biological sex
- Diagnostic topic
- Article title
- Case-report text
- Structured clinical category extractions

## Key Statistics

| Metric | Value |
| --- | ---: |
| Total case reports | 85,961 |
| Publication years | 1986-2023 |
| Average report length | 3,462 words |
| Clinical categories | 14 |
| Female cases | 55.6% |
| Male cases | 44.1% |
| Intersex cases | 0.1% |

## Clinical Categories

- Vitals_Hema
- EENT
- Neuro
- CVS
- RESP
- GI
- GU
- MSK
- DERM
- LYMPH
- ENDO
- Pregnancy
- Lab_Image
- History

## Repository Contents

```text
DatasetEDA/Dataset_EDA.ipynb
notebooks/Demographics_Topic_EDA.ipynb
notebooks/pool_mean_embeddings.ipynb
notebooks/faiss_retrieval.ipynb
function.py
scripts/check_artifacts.py
scripts/summarize_human_eval.py
docs/artifact_inventory.md
requirements.txt
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For embedding generation, use a CUDA-capable environment if available. Retrieval can also be run from precomputed embedding artifacts.

## Reproducing the Paper

Large generated artifacts and local dataset snapshots are intentionally excluded from Git. Restore the required files listed in [docs/artifact_inventory.md](docs/artifact_inventory.md), then run:

```bash
python scripts/check_artifacts.py --root .
```

The main analysis notebooks are:

| Manuscript output | Source notebook | Expected output |
| --- | --- | --- |
| Extraction EM and TSR by category | `DatasetEDA/Dataset_EDA.ipynb` | `graphs/exact match percentage per category.pdf`, `graphs/tokensetratio.pdf` |
| Extracted string counts by category | `DatasetEDA/Dataset_EDA.ipynb` | `graphs/Dataset_EDA_Extractions_PerCategory.pdf` |
| Publication-year and sex distribution | `notebooks/Demographics_Topic_EDA.ipynb` | `graphs/sex distribution over pub yrs.pdf` |
| Sex distribution by age group | `notebooks/Demographics_Topic_EDA.ipynb` | `graphs/sex distribution over age groups.pdf` |
| Sex distribution over top topics | `notebooks/Demographics_Topic_EDA.ipynb` | `graphs/sex distribution over top 20 medical conditions.pdf` |
| Embedding retrieval metrics | `notebooks/faiss_retrieval.ipynb` | `graphs/mean_IR.pdf` |

## Limitations

- Structured fields were automatically generated and may contain extraction errors.
- Diagnostic labels are not manually curated for every record.
- Case reports are subject to publication and reporting biases.
- The dataset is intended for research use and should not be used for clinical decision-making.

## Citation

```bibtex
@inproceedings{zhang2025casereportcollective,
  title = {CaseReportCollective: A Large-Scale LLM-Extracted Dataset for Structured Medical Case Reports},
  author = {Zhang, Xiao Yu Cindy and Wasserman, Wyeth and Fong, Melissa and Zhu, Jian},
  booktitle = {Proceedings of the 24th Workshop on Biomedical Language Processing},
  pages = {249--262},
  year = {2025}
}
```

## Licensing

Code, scripts, and notebooks in this repository are released under the MIT License. The CaseReportCollective structured annotations are released under CC BY-NC 4.0. Original case reports remain subject to the licenses associated with their source articles in PubMed Central Open Access.
