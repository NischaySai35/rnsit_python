import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = "D:\\learning\\rnsit_python\\Mini-Project\\Engineering_Branch_Analytics.csv"  
df = pd.read_csv(file_path, skipinitialspace=True) 

bubble_data = df[["Branch Name SS", "Higher Education Rate", "Research Opportunities", "Students Abroad"]]

bubble_data = bubble_data.sort_values(by="Higher Education Rate", ascending=True)

plt.figure(figsize=(12, 7))
scatter = sns.scatterplot(
    x="Higher Education Rate",
    y="Research Opportunities",
    size="Students Abroad",
    hue="Branch Name SS",
    sizes=(800, 8000),
    alpha=0.7,
    edgecolor="black",
    linewidth=1,
    data=bubble_data
)

plt.title("Higher Education vs Research Opportunities by Branch", fontsize=14)
plt.xlabel("Higher Education Rate (%)", fontsize=12)
plt.ylabel("Research Opportunities (Funding/Publications)", fontsize=12)

handles, labels = scatter.get_legend_handles_labels()
new_handles = handles[:len(bubble_data["Branch Name SS"].unique())] 
new_labels = labels[:len(bubble_data["Branch Name SS"].unique())] 

unique_branches = bubble_data["Branch Name SS"].unique()
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=sns.color_palette()[i], markersize=10)
           for i in range(len(unique_branches))]
plt.legend(handles, unique_branches, title="Branch Name", bbox_to_anchor=(0, 1), loc='upper left', frameon=True)

plt.xlim([35, 85]) 
plt.ylim([45, 90]) 

plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout() 
plt.show()
