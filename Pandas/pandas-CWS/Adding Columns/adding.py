# adding columns
import pandas as pd

data = {
    "Name": ["John", "Anna", "Peter", "Linda", "Bob", "Raj", "Simran", "Ram"],
    "Age": [28, 24, 35, 32, 50, 60, 70, 45],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)
print(df)

df["Bonus"] = df['Salary'] * 0.1
print(df)

# using insert()
df.insert(0, 'Employee ID', [10, 20, 30, 40, 50, 60, 70, 80])
print(df)