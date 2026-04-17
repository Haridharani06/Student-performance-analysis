# 🔹 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# 🔹 2. Load Dataset
df = pd.read_csv("student_dataset.csv")

# 🔹 3. Clean Column Names (VERY IMPORTANT)
df.columns = df.columns.str.strip().str.lower()

# 🔹 4. View Data
print("First 5 rows:\n", df.head())
print("\nDataset Info:\n")
print(df.info())

# 🔹 5. Rename Columns to Standard Names
df.rename(columns={
    'name': 'Name',
    'maths': 'Maths',
    'math': 'Maths',
    'physics': 'Physics',
    'chemistry': 'Chemistry',
    'grade': 'Grade',
    'school': 'School'
}, inplace=True)

# 🔹 6. Total & Average Calculation
df['Total'] = df[['Maths', 'Physics', 'Chemistry']].sum(axis=1)
df['Average'] = df['Total'] / 3

# 🔹 7. Cutoff Calculation
df['Cutoff'] = df['Maths'] + (df['Physics']/2) + (df['Chemistry']/2)

print("\nData with Total, Average, Cutoff:\n")
print(df.head())

# 🔹 8. Top Performer (Total)
top_total = df.loc[df['Total'].idxmax()]
print("\nTopper (Total Marks):", top_total['Name'])

# 🔹 9. Top Performer (Cutoff)
top_cutoff = df.loc[df['Cutoff'].idxmax()]
print("Topper (Cutoff):", top_cutoff['Name'])

# 🔹 10. Subject-wise Average
print("\nSubject Averages:")
print("Maths Avg:", df['Maths'].mean())
print("Physics Avg:", df['Physics'].mean())
print("Chemistry Avg:", df['Chemistry'].mean())

# 🔹 11. Grade Distribution
if 'Grade' in df.columns:
    print("\nGrade Distribution:")
    print(df['Grade'].value_counts())

# 🔹 12. School-wise Analysis
if 'School' in df.columns:
    print("\nSchool-wise Average Cutoff:")
    print(df.groupby('School')['Cutoff'].mean())

# 🔹 13. Cutoff Range Analysis
high = df[df['Cutoff'] > 180].shape[0]
medium = df[(df['Cutoff'] >= 150) & (df['Cutoff'] <= 180)].shape[0]
low = df[df['Cutoff'] < 150].shape[0]

print("\nCutoff Distribution:")
print("Above 180:", high)
print("150 - 180:", medium)
print("Below 150:", low)

# 🔹 14. Visualization

# 📊 Bar Chart - Total Marks
plt.figure()
plt.bar(df['Name'], df['Total'])
plt.title("Total Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=90)
plt.show()

# 📊 Histogram - Cutoff Distribution
plt.figure()
plt.hist(df['Cutoff'])
plt.title("Cutoff Distribution")
plt.xlabel("Cutoff")
plt.ylabel("Number of Students")
plt.show()

# 📊 Pie Chart - Grade Distribution
if 'Grade' in df.columns:
    plt.figure()
    df['Grade'].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title("Grade Distribution")
    plt.ylabel("")
    plt.show()

# 🔹 15. Save Updated Data
df.to_csv("updated_student_analysis.csv", index=False)

print("\n✅ Analysis Completed Successfully!")
