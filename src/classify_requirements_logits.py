import pandas as pd
import json
from tqdm import tqdm
from model import RequirementClassifierModel



INPUT_FILE = "data/processed/val.csv"
OUTPUT_FILE = "outputs/validation_classification_logits_results.csv"





LABELS = [
    "Functional", 
    "Availability", 
    "Legal", 
    "Look & Feel", 
    "Maintainability", 
    "Operability", 
    "Performance", 
    "Scalability", 
    "Security", 
    "Usability", 
    "Fault Tolerance", 
    "Portability"
]

label_mapping = {
    "Functional": "F",
    "Availability": "A",
    "Legal": "L",
    "Look & Feel": "LF",
    "Maintainability": "MN",
    "Operability": "O",
    "Performance": "PE",
    "Scalability": "SC",
    "Security": "SE",
    "Usability": "US",
    "Fault Tolerance": "FT",
    "Portability": "PO"
}


classifier = RequirementClassifierModel()
test_df = pd.read_csv(INPUT_FILE)

print("Running logit-based classification...")



results = []

for index, row in tqdm(test_df.iterrows(), total=len(test_df), desc="Classifying requirements"):
    requirement_text = row['RequirementText']
    true_label = row['_class_']



    predicted_label, msp_confidence, all_probabilities = classifier.classify_logits(requirement_text, LABELS)
    predicted_label_mapped = label_mapping.get(predicted_label, predicted_label)

    results.append({
        "RequirementText": requirement_text,
        "TrueLabel": true_label,
        "PredictedLabel": predicted_label_mapped,
        "PredictedLabelText": predicted_label,
        "Confidence": msp_confidence,
        "AllProbabilities": json.dumps(all_probabilities)
    })


    
df_results = pd.DataFrame(results)
df_results.to_csv(OUTPUT_FILE, index=False)

print(f"Classification completed. Results saved to {OUTPUT_FILE}.")