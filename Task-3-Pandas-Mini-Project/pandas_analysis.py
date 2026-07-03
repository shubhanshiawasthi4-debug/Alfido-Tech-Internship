import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv("accident_data.csv", sep='\t')

# Inspect Dataset
print("First 5 Rows:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nSummary Statistics:")
print(data.describe(include='all'))

# Data Cleaning
data = data.dropna()
data = data.drop_duplicates()

# Filtering
rain_data = data[data["Weather Conditions"] == "Rain"]
print("\nAccidents in Rain:")
print(rain_data.head())

# Grouping
weather_group = data.groupby("Weather Conditions").size()
print("\nAccidents by Weather:")
print(weather_group)

road_group = data.groupby("Road Type").size()
print("\nAccidents by Road Type:")
print(road_group)

# Aggregation
gender_count = data["Driver Gender"].value_counts()
print("\nDriver Gender Count:")
print(gender_count)

# ---------------- Graph 1 ----------------
plt.figure(figsize=(7,5))
weather_group.plot(kind="bar", color="skyblue")
plt.title("Accidents by Weather Conditions")
plt.xlabel("Weather Conditions")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# ---------------- Graph 2 ----------------
plt.figure(figsize=(6,6))
gender_count.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Driver Gender Distribution")
plt.tight_layout()
plt.show()

# ---------------- Graph 3 ----------------
plt.figure(figsize=(7,5))
road_group.plot(kind="bar", color="orange")
plt.title("Accidents by Road Type")
plt.xlabel("Road Type")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# Insights
print("\n----- Insights -----")
print("1. Weather-wise accident counts are displayed.")
print("2. Road type accident counts are displayed.")
print("3. Driver gender distribution is shown.")
print("4. Missing and duplicate values have been removed.")