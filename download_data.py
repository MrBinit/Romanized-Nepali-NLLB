from datasets import load_dataset

# Load the dataset from Hugging Face
dataset = load_dataset("momo22/eng2nep")
output_dir = "./eng2nep_dataset"

for split in dataset.keys():
    output_file = f"{output_dir}/{split}.csv"
    dataset[split].to_csv(output_file, index=False)
    print(f"Saved {split} split to {output_file}")

print("Dataset successfully saved as CSV files!")
