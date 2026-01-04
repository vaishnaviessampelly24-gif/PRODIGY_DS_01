import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from CSV file
df = pd.read_csv("population.csv")

# -------------------------------
# Histogram for continuous variable: Age
# -------------------------------
plt.figure()
plt.hist(df["Age"], bins=5)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution of Population")
plt.show()

# -------------------------------
# Bar chart for categorical variable: Gender
# -------------------------------
gender_counts = df["Gender"].value_counts()

plt.figure()
plt.bar(gender_counts.index, gender_counts.values)
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Gender Distribution of Population")
plt.show()
