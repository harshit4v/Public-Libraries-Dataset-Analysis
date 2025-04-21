import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_csv('Public_libraries.csv')
# print(df)
# df.info()
# df.describe()
# print(df.isnull().sum())
# df.head()
basic_info = {
    "shape": df.shape,
    "null_values": df.isnull().sum(),
    "data_types": df.dtypes,
    "duplicates": df.duplicated().sum()
}
# Step 2: Data Cleaning & Preprocessing
# Drop columns with over 25% missing data
threshold = len(df) * 0.75
df_cleaned = df.dropna(thresh=threshold, axis=1)
# Drop rows where essential fields are missing
essential_columns = ['Population of Service Area', 'Total Library Visits', 'Fiscal Year']
df_cleaned = df_cleaned.dropna(subset=essential_columns)
# Fill remaining numeric NaN with median
numeric_cols = df_cleaned.select_dtypes(include=['float64', 'int64']).columns
df_cleaned[numeric_cols] = df_cleaned[numeric_cols].fillna(df_cleaned[numeric_cols].median())
# Standardize column names (optional: remove trailing spaces etc.)
df_cleaned.columns = df_cleaned.columns.str.strip()
df_cleaned.to_csv("Cleaned_Public_Libraries.csv", index=False)
print(df_cleaned.head())
