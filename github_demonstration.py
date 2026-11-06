import pandas as pd

df = pd.read_csv("sample_data/donors.csv")

print(df.head())

print(df.describe())
