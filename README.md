# CaseReportCollective

CaseReportCollective is a large-scale, LLM-structured dataset of open-access medical case reports used in the BioNLP 2025 paper:

**CaseReportCollective: A Large-Scale LLM-Extracted Dataset for Structured Medical Case Reports**

The dataset contains structured extractions across 14 clinical categories, diagnostic labels, demographic attributes, and analysis artifacts for dataset characterization and embedding-based retrieval experiments.

## Dataset

The paper dataset is published on Hugging Face:

`cxyzhang/CaseReportCollective_V1.0`

Earlier intermediate datasets used during analysis were named `pmc_llmExtraction_v7`, `pmc_llmExtraction_v8`, `pmc_llmExtraction_v9`, and `pmc_llmExtraction_v10`. The final paper-facing table corresponds to the `v10` schema:

```text
pmcid, publication_year, age, sex, topic, title, case, case_length,
Vitals_Hema, Pregnancy, Neuro, CVS, RESP, EENT, GI, GU, DERM,
MSK, ENDO, LYMPH, History, Lab_Image
```

Large local artifacts are intentionally not stored in Git. See [docs/artifact_inventory.md](docs/artifact_inventory.md) for the expected local files and how they map to manuscript sections.

## Repository Layout

```text
DatasetEDA/Dataset_EDA.ipynb          Extraction quality and category-count analysis
notebooks/Demographics_Topic_EDA.ipynb Demographics, publication year, and topic analyses
notebooks/pool_mean_embeddings.ipynb   MedEmbed embedding generation
notebooks/faiss_retrieval.ipynb        FAISS retrieval and IR metric analysis
function.py                            Shared preprocessing helpers
scripts/check_artifacts.py             Local artifact availability check
scripts/summarize_human_eval.py        Human-evaluation summary from annotation CSV
docs/artifact_inventory.md             Required non-Git artifacts
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For embedding generation, use a CUDA-capable environment if available. The retrieval notebook can run from precomputed embedding artifacts.

## Reproducing Paper Analyses

1. Restore the non-Git artifacts listed in [docs/artifact_inventory.md](docs/artifact_inventory.md).
2. Confirm artifact availability:

```bash
python scripts/check_artifacts.py --root .
```

3. Run dataset extraction quality analysis:

```bash
jupyter notebook DatasetEDA/Dataset_EDA.ipynb
```

4. Run demographics and topic analysis:

```bash
jupyter notebook notebooks/Demographics_Topic_EDA.ipynb
```

5. Generate or restore embeddings:

```bash
jupyter notebook notebooks/pool_mean_embeddings.ipynb
```

6. Run FAISS retrieval evaluation:

```bash
jupyter notebook notebooks/faiss_retrieval.ipynb
```

## Manuscript Figure Mapping

| Manuscript output | Source notebook | Expected artifact |
| --- | --- | --- |
| Extraction EM and TSR by category | `DatasetEDA/Dataset_EDA.ipynb` | `graphs/exact match percentage per category.pdf`, `graphs/tokensetratio.pdf` |
| Extracted string counts by category | `DatasetEDA/Dataset_EDA.ipynb` | `graphs/Dataset_EDA_Extractions_PerCategory.pdf` |
| Publication year and sex distribution | `notebooks/Demographics_Topic_EDA.ipynb` | `graphs/sex distribution over pub yrs.pdf` |
| Sex distribution by age group | `notebooks/Demographics_Topic_EDA.ipynb` | `graphs/sex distribution over age groups.pdf` |
| Sex distribution over top topics | `notebooks/Demographics_Topic_EDA.ipynb` | `graphs/sex distribution over top 20 medical conditions.pdf` |
| IR metrics by frequency group | `notebooks/faiss_retrieval.ipynb` | `graphs/mean_IR.pdf` |

## Notes

The notebooks were used for the paper analyses and retain exploratory cells. For a production workflow, the next step is to convert the main notebook paths into parameterized Python scripts.
