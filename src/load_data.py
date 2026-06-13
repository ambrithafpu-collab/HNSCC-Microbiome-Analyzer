import pandas as pd

df = pd.read_csv("data/microbiome.csv")

print("Original Dataset")
print(df)

# Bacterial columns
bacteria = ["Fusobacterium", "Prevotella",
            "Streptococcus", "Haemophilus"]

# Convert counts to percentages
relative_abundance = df.copy()

relative_abundance[bacteria] = (
    df[bacteria]
    .div(df[bacteria].sum(axis=1), axis=0)
    * 100
)

print("\nRelative Abundance (%)")
print(relative_abundance)
import matplotlib.pyplot as plt

bacteria = ["Fusobacterium", "Prevotella",
            "Streptococcus", "Haemophilus"]

mean_abundance = (
    relative_abundance
    .groupby("Group")[bacteria]
    .mean()
)

print("\nMean Relative Abundance")
print(mean_abundance)

mean_abundance.T.plot(kind="bar")

plt.title("Mean Relative Abundance by Group")
plt.ylabel("Percentage")
plt.tight_layout()

plt.savefig("results/abundance_plot.png")

plt.show()