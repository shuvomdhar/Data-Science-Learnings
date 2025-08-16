import pandas as pd

data = {
    "Name": ["John", "Anna", "Peter", "Linda", "Bob", "Raj", "Simran", "Ram"],
    "Age": [28, 24, 35, 32, 50, 60, 70, 45],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)
print(df)

print('Modified Data')
df.drop(columns=['Performance_Score'], inplace=True)
print(df)