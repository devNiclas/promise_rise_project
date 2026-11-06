import ast

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report

INPUT_FILE = "outputs/validation_classification_logits_results.csv"
OUTPUT_FILE = "outputs/qwen_validation_logits_accuracy_f1_metrics.csv"

df_data = pd.read_csv(INPUT_FILE)




predicted_labels = df_data['PredictedLabel']
true_labels = df_data['TrueLabel']
confidence_scores = df_data['Confidence']



accuracy = accuracy_score(true_labels, predicted_labels)
macro_f1 = f1_score(true_labels, predicted_labels, average='macro')

df_data['Correct'] = (predicted_labels == true_labels)
mean_msp_overall = confidence_scores.mean()
mean_msp_correct = confidence_scores[df_data['Correct']].mean()
mean_msp_incorrect = confidence_scores[~df_data['Correct']].mean()


print("===============================================================")
print("        LOGIT CLASSIFICATION EVALUTION RESULTS       ")
print("===============================================================")
print(f"Accuracy: {accuracy:.4f}")
print(f"Macro F1 Score: {macro_f1:.4f}")
print(f"Mean MSP (Overall): {mean_msp_overall:.4f}")
print(f"Mean MSP (When Correct): {mean_msp_correct:.4f}")
print(f"Mean MSP (When Incorrect): {mean_msp_incorrect:.4f}")



print ("--- Classification Report F1 per Class ---")
print(classification_report(true_labels, predicted_labels, zero_division=0))

print ("--- Confusion Matrix ---")
print(confusion_matrix(true_labels, predicted_labels))

df_metrics = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Macro F1 Score",
        "Mean MSP (Overall)",
        "Mean MSP (When Correct)",
        "Mean MSP (When Incorrect)"
    ],
    "Value": [
        accuracy,
        macro_f1,
        mean_msp_overall,
        mean_msp_correct,
        mean_msp_incorrect
    ]
    

})
df_metrics.to_csv(OUTPUT_FILE, index=False)
print(f"Summary of metrics saved to {OUTPUT_FILE}.")


report_dict = classification_report(true_labels, predicted_labels, zero_division=0, output_dict=True)
df_per_class = pd.DataFrame(report_dict).transpose()
per_class_output_file = "outputs/qwen_validation_logits_per_class_metrics.csv"
df_per_class.to_csv(per_class_output_file)
print(f"Per-class metrics saved to {per_class_output_file}.")


cm = confusion_matrix(true_labels, predicted_labels)
unique_labels = sorted(list(set(true_labels)))
df_cm = pd.DataFrame(cm, index=unique_labels, columns=unique_labels)
cm_output_file = "outputs/qwen_validation_logits_confusion_matrix.csv"
df_cm.to_csv(cm_output_file)
print(f"Confusion matrix saved to {cm_output_file}.")








