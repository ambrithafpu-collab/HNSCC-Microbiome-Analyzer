import pandas as pd
import numpy as np

df = pd.read_csv("data/microbiome.csv")

bacteria = [
    "Fusobacterium",
    "Prevotella",
    "Streptococcus",
    "Haemophilus"
]

def shannon_index(row):
    proportions = row / row.sum()
    proportions = proportions[proportions > 0]
    return -np.sum(proportions * np.log(proportions))

df["Shannon_Index"] = df[bacteria].apply(shannon_index, axis=1)

print(df[["Sample", "Group", "Shannon_Index"]])

print("\nAverage Shannon Diversity:")
print(df.groupby("Group")["Shannon_Index"].mean())