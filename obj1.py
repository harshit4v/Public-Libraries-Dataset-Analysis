import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_csv('Cleaned_Public_libraries.csv')
print(df)

df = df.rename(columns={
    'Population of Service Area': 'Population',
    'Total Library Visits': 'Visits',
    'Total Registered Borrowers': 'Borrowers'
})

#scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df['Population'], df['Visits'], alpha=0.5, s=20, color='blue')
plt.title('Library Visits vs Population Served')
plt.xlabel('Population')
plt.ylabel('Total Library Visits')
plt.grid(True)
plt.tight_layout()
plt.show()
