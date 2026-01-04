import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from CSV file
df = pd.read_csv("population.csv")

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
