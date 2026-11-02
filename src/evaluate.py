import ast

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

INPUT_FILE = "outputs/validation_classification_results.csv"
OUTPUT_FILE = "outputs/qwen_validation_accuracy_f1_metrics.csv"

df_data = pd.read_csv(INPUT_FILE)




predicted_labels = df_data['PredictedLabel']
true_labels = df_data['TrueLabel']
y_true = true_labels
y_pred = predicted_labels



accuracy = accuracy_score(true_labels, predicted_labels)
macro_f1 = f1_score(true_labels, predicted_labels, average='macro')


df_accuracy_f1 = pd.DataFrame({
    'Metric': ['Accuracy', 'Macro F1 Score'],
    'Value': [accuracy, macro_f1]
})

df_accuracy_f1.to_csv(OUTPUT_FILE, index=False)

print(" -------- Evaluation completed --------")
print(f"Accuracy: {accuracy:.4f}")
print(f"Macro F1 Score: {macro_f1:.4f}")




