import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv("Cleaned_Public_Libraries.csv")
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Cleaned_Public_Libraries.csv")
def remove_outliers_iqr(df, column, group_by):
    cleaned_df = pd.DataFrame()
    for group, subset in df.groupby(group_by):
        Q1 = subset[column].quantile(0.25)
        Q3 = subset[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        filtered = subset[(subset[column] >= lower_bound) & (subset[column] <= upper_bound)]
        cleaned_df = pd.concat([cleaned_df, filtered], axis=0)
    return cleaned_df
df_no_outliers = remove_outliers_iqr(df, "Library Visits Per Capita Served", "County")
# Set seaborn style
sns.set(style="whitegrid")
# Plot box plot without outliers
plt.figure(figsize=(12, 6))
sns.boxplot(
    x="County",
    y="Library Visits Per Capita Served",
    data=df_no_outliers,
    palette="Set2"
)
plt.title("Library Visits Per Capita by County (Outliers Removed)")
plt.xlabel("County")
plt.ylabel("Library Visits Per Capita")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()