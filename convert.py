import pandas

df = pandas.read_excel("data/DAlessandro JCI 2020 Exposome Dataset.xlsx")
df.to_csv("data/DAlessandro JCI 2020 Exposome Dataset.csv", index=False)
df = pandas.read_excel("data/DAlessandro_JCI_2020_Exposome_Dataset_WithDonorIDs_v3.xlsx")
df.to_csv("data/DAlessandro_JCI_2020_Exposome_Dataset_WithDonorIDs_v3.csv", index=False)

print("completed")