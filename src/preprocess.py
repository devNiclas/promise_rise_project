import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/raw/promise_raw.csv", encoding="utf-8")


#Split the dataset into training and temporary sets

train_df, temp_df = train_test_split(
    df,
    test_size=0.3,
    random_state=42,
    stratify=df['_class_']
)

# Split the temporary set into validation and test sets

val_df, test_df = train_test_split(
    temp_df,
    test_size=0.5,
    random_state=42,
    stratify=temp_df['_class_']
)


train_df.to_csv("data/processed/train.csv", index=False, encoding="utf-8")
val_df.to_csv("data/processed/val.csv", index=False, encoding="utf-8")
test_df.to_csv("data/processed/test.csv", index=False, encoding="utf-8")


print("Data splitting completed successfully.")
print("Total dataset size:", len(df))
print("Training set size:", len(train_df))
print("Validation set size:", len(val_df))
print("Test set size:", len(test_df))


num_classes = df['_class_'].nunique()
print("Number of unique classes:", num_classes)


class_dist = df['_class_'].value_counts(normalize=True) * 100
print("Class distribution (%):\n", class_dist.round(2))


word_counts = df['RequirementText'].str.split().str.len()
avg_words = word_counts.mean()
std_words = word_counts.std()

print(f"Average number of words in RequirementText: {avg_words:.2f}")
print(f"Standard deviation of words in RequirementText: {std_words:.2f}")











