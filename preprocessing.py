import pandas as pd 

df = pd.read_csv("/home/binit/translation-Romanized-NLLB/data/final_merged_translation.csv")
print(df.head())
print("This is the shape of the dataset: ", df.shape)
print("This is the columns of the dataset: ", df.columns)
print("Null value in the dataset: ", df.isnull().sum())