import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file_path = "Mini-Project-Hackathon\\Engineering_Branch_Analytics.csv"
df = pd.read_csv(file_path)

branches = df["Branch Name SS"]
enrollments = df["Students Enrolled"]
placements = df["Placements (%)"] * 2

x = np.arange(len(branches))
width = 0.4

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(x - width/2, enrollments, width, color="yellow", edgecolor="black", label="Students Enrolled")
ax.bar(x + width/2, placements, width, color="red", edgecolor="black", label="Placement %")

ax.set_xticks(x)
ax.set_xticklabels(branches, rotation=45)
ax.set_ylabel("Count / Percentage")
ax.set_xlabel("Branch")
ax.set_title("Enrollment vs Placement for All Branches")
ax.legend()

plt.show()
