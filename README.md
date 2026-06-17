[![Paper](https://img.shields.io/badge/Paper-BioNLP%202025-blue)](https://aclanthology.org/2025.bionlp-1.22/)
[![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-yellow?logo=huggingface)](https://huggingface.co/datasets/cxyzhang/CaseReportCollective_V1.0)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC--BY--NC--4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

# CaseReportCollective

CaseReportCollective is a large-scale dataset of 85,961 open-access medical case reports automatically structured using large language models (LLMs). The dataset was introduced in:

**Zhang XYC, Wasserman W, Fong M, Zhu J. CaseReportCollective: A Large-Scale LLM-Extracted Dataset for Structured Medical Case Reports. BioNLP 2025.**

## Overview

Medical case reports contain rich clinical narratives describing rare, unusual, and diagnostically challenging conditions. However, their free-text format limits large-scale computational analysis.

CaseReportCollective converts these narratives into structured clinical representations across 14 patient-assessment categories, enabling biomedical information extraction, retrieval, demographic analysis, and clinical NLP research.

### Key Statistics

| Metric                | Value       |
| --------------------- | ----------- |
| Total case reports    | 85,961      |
| Publication years     | 1986–2023   |
| Average report length | 3,462 words |
| Clinical categories   | 14          |
| Female cases          | 55.6%       |
| Male cases            | 44.1%       |
| Intersex cases        | 0.1%        |

## Dataset Access

The dataset is available on Hugging Face:

`cxyzhang/CaseReportCollective_V1.0`

Each record contains:

* PMCID
* Publication year
* Age group
* Biological sex
* Diagnostic topic
* Article title
* Structured clinical findings
* Clinical category extractions

## Clinical Categories

* Vitals_Hema
* EENT
* Neuro
* CVS
* RESP
* GI
* GU
* MSK
* DERM
* LYMPH
* ENDO
* Pregnancy
* Lab_Image
* History

## Repository Contents

This repository contains the code used for:

* Dataset characterization
* Demographic analyses
* Extraction-quality evaluation
* Embedding generation
* Retrieval experiments

The primary notebooks are:

* DatasetEDA/Dataset_EDA.ipynb
* notebooks/Demographics_Topic_EDA.ipynb
* notebooks/pool_mean_embeddings.ipynb
* notebooks/faiss_retrieval.ipynb

## Reproducing the Paper

See `docs/artifact_inventory.md` for required local artifacts and instructions for reproducing the analyses reported in the paper.

## Limitations

* Structured fields were automatically generated using LLMs and may contain extraction errors.
* Diagnostic labels are not manually curated.
* Case reports are subject to publication and reporting biases.
* The dataset is intended for research use and should not be used for clinical decision-making.

## Citation
```
@inproceedings{zhang2025casereportcollective,
  title={CaseReportCollective: A Large-Scale LLM-Extracted Dataset for Structured Medical Case Reports},
  author={Zhang, Xiao Yu Cindy and Fong, Melissa and Wasserman, Wyeth and Zhu, Jian},
  booktitle={Proceedings of the 24th Workshop on Biomedical Language Processing},
  pages={249--262},
  year={2025}
}
```
## License

Structured annotations are released under CC BY 4.0.

Original case reports remain subject to the licenses associated with their source articles in PubMed Central Open Access.
