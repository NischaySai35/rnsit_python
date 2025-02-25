import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


file_path = "Mini-Project/Engineering_Branch_Analytics.csv"
df = pd.read_csv(file_path)

heatmap_data = df[["Branch Name SS", "Tech Adoption Score", "Industry Collaboration Score"]]

heatmap_data = heatmap_data.sort_values(by="Tech Adoption Score", ascending=False)

heatmap_data = heatmap_data.set_index("Branch Name SS")

plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", linewidths=0.5, fmt=".1f")

plt.title("Technological Advancements Potential by Branch (Sorted by Tech Adoption)")
plt.xlabel("Metrics")
plt.ylabel("Branch Name")

plt.show()
