import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv("Cleaned_Public_Libraries.csv")
# ===== Bar Chart: Percent with Library Cards vs Reference Questions =====
plt.figure(figsize=(12, 6))
plt.bar(df["Library"], df["Percent of Residents with Library Cards"], label="Library Card Holders (%)", color='skyblue')
plt.plot(df["Library"], df["Reference Questions"], label="Reference Questions", color='coral', marker='o')
plt.xticks(rotation=90)
plt.title("Library Card Holders vs Reference Questions")
plt.xlabel("Library")
plt.ylabel("Engagement / Questions")
plt.legend()
plt.tight_layout()
plt.show()
# ===== Stacked Bar: Programs, Reference Questions, Program Views =====
stacked_df = df[["Library", "Total Programs (Synchronous + Prerecorded)", "Reference Questions", "Total Program Attendance & Views"]]
stacked_df.set_index("Library", inplace=True)
stacked_df = stacked_df.head(10)  # Limit for visualization
stacked_df.plot(kind="bar", stacked=True, figsize=(14, 6), colormap="Paired")
plt.title("Breakdown of User Engagement by Library (Top 10)")
plt.xlabel("Library")
plt.ylabel("Total Interactions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ===== Pie Chart: Total Proportions of Engagement Types =====
total_programs = df["Total Programs (Synchronous + Prerecorded)"].sum()
total_questions = df["Reference Questions"].sum()
total_views = df["Total Program Attendance & Views"].sum()
labels = ["Programs", "Reference Questions", "Program Attendance & Views"]
sizes = [total_programs, total_questions, total_views]
colors = ['lightgreen', 'gold', 'lightskyblue']
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Overall Breakdown of Engagement Types")
plt.tight_layout()
plt.show()
