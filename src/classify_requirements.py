import pandas as pd
from model import RequirementClassifierModel



INPUT_FILE = "data/processed/val.csv"
OUTPUT_FILE = "outputs/validation_classification_results.csv"





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

print("Loading model and starting classification...")



results = []

for index, row in test_df.iterrows():
    requirement_text = row['RequirementText']
    true_label = row['_class_']




    predicted_label = classifier.classify(requirement_text, LABELS)
    predicted_label_mapped = label_mapping.get(predicted_label, predicted_label)

    results.append({
        "RequirementText": requirement_text,
        "TrueLabel": true_label,
        "PredictedLabel": predicted_label_mapped,
        "PredictedLabelText": predicted_label,
    })


    
df_results = pd.DataFrame(results)
df_results.to_csv(OUTPUT_FILE, index=False)

print(f"Classification completed. Results saved to {OUTPUT_FILE}.")