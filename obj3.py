import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv("Cleaned_Public_Libraries.csv")
# ========== Heatmap of Correlations ==========
financial_service_cols = [
    "Operating Income Per Capita",
    "Operating Expenditures Per Capita",
    "Library Visits Per Capita Served",
    "Circulation Per Capita Served"
]
correlation_matrix = df[financial_service_cols].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlation: Financial Health vs. Service Output")
plt.tight_layout()
plt.show()
# ========== Bar Charts: Top Libraries ==========
# Top 10 libraries by Operating Income Per Capita
top_income = df.groupby("Library")["Operating Income Per Capita"].mean().nlargest(10).sort_values()
# Top 10 libraries by Visits Per Capita
top_visits = df.groupby("Library")["Library Visits Per Capita Served"].mean().nlargest(10).sort_values()
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
# Bar chart: Operating Income
axes[0].barh(top_income.index, top_income.values, color="teal")
axes[0].set_title("Top 10 Libraries by Avg. Operating Income Per Capita")
axes[0].set_xlabel("Operating Income Per Capita")
# Bar chart: Library Visits
axes[1].barh(top_visits.index, top_visits.values, color="coral")
axes[1].set_title("Top 10 Libraries by Avg. Visits Per Capita")
axes[1].set_xlabel("Library Visits Per Capita")
plt.tight_layout()
plt.show()
