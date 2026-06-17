import json
import pandas as pd
from datasets import load_from_disk

def process_extraction(local_hf_dataset="./pmc_llmExtraction_v8/"):
    # Load dataset
    llm_extract = load_from_disk(local_hf_dataset)
    extract = llm_extract.to_list()

    # Function to parse nested JSON strings
    def parse_nested_json(value):
        while isinstance(value, str):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                break
        return value

    # Convert JSON strings in `case` and `extraction` fields
    for item in extract:
        if isinstance(item, dict):
            if isinstance(item.get("extraction"), str):
                item["extraction"] = parse_nested_json(item["extraction"])
            if isinstance(item.get("case"), str):
                item["case"] = parse_nested_json(item["case"])

    # Function to concatenate case dictionary values into a single string
    def combined_corpus(dic):
        if isinstance(dic.get("case"), dict):
            dic["case"] = " ".join(dic["case"].values())
        return dic

    # Apply transformations
    preprocessed_extract = [combined_corpus(i) for i in extract]

    # Remove cases with empty strings
    preprocessed_extract = [item for item in preprocessed_extract if item.get("case", "").strip()]

    # Remove entries with empty extraction
    preprocessed_extract = [item for item in preprocessed_extract if item.get("extraction")]

    return preprocessed_extract

def category_df(process_extraction):

    with open("./data/merged_extracted_sex.json") as f:
        sex = json.load(f)
    
    sex_df = pd.DataFrame(list(sex.items()), columns=["pmcid", "sex"])
    
    sex_df["Sex"] = sex_df["sex"].replace({None: "unspecified"}) # convert failed to extraction to "unspecified" 
    sex_df["pmcid"] = sex_df["pmcid"].astype(str)
    
    male_pmcid = set(sex_df[sex_df["Sex"]=="male"]["pmcid"].tolist())
    
    # Convert the male PMCID list to a set for fast lookups (O(1) instead of O(n))
    male_pmcid_set = set(male_pmcid)
    
    # Efficiently update 'Pregnancy' in place
    for item in process_extraction:
        if item["pmcid"] in male_pmcid_set:
            item["extraction"].setdefault("Pregnancy", [])[:] = []  # Ensures empty list in pregnancy for males
        
    categories = ['Vitals_Hema', 'Pregnancy', 'Neuro', 'CVS', 'RESP', 'EENT', 
                  'GI', 'GU', 'DERM', 'MSK', 'ENDO', 'LYMPH', 'History', 'Lab_Image']
    
    df = pd.DataFrame([
        {
            "pmcid": entry["pmcid"],
            "title": entry["title"],
            "case": entry["case"], 
            "case_length": len(str(entry["case"]).split()) if pd.notna(entry["case"]) else 0,

            **{
                category: entry["extraction"].get(category, []) for category in categories
            },
            **{
                f"{category}_word_count": sum(len(item.split()) for item in entry["extraction"].get(category, []))  
                for category in categories
            }
        }
        for entry in process_extraction
    ])

    return df