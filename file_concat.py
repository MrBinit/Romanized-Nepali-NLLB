import pandas as pd

train_path = "/home/binit/translation-Romanized-NLLB/data/nepali_roman_transliteration/train.csv"
validation_path = "/home/binit/translation-Romanized-NLLB/data/nepali_roman_transliteration/validation.csv"
output_path = "/home/binit/translation-Romanized-NLLB/data/nepali_romanized_words_combined.csv"

train_df = pd.read_csv(train_path)
validation_df = pd.read_csv(validation_path)
combined_df = pd.concat([train_df, validation_df])

combined_df = combined_df.rename(columns={"native word": "nepali_word", "english word": "romanized_nepali"})[["nepali_word", "romanized_nepali"]]

# Save the combined dataset to a CSV file
combined_df.to_csv(output_path, index=False)

print(f"Combined dataset saved to: {output_path}")
