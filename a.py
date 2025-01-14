import pandas as pd

# Paths to the CSV files
file1_path = "/home/binit/translation-Romanized-NLLB/data/nepali_romanized_dataset.csv"
file2_path = "/home/binit/translation-Romanized-NLLB/merged_translation.csv"
output_path = "/home/binit/translation-Romanized-NLLB/final_merged_translation.csv"

df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

merged_df = pd.concat([df1, df2], ignore_index=True)
merged_df.to_csv(output_path, index=False)

print(f"Merged dataset saved to: {output_path}")
