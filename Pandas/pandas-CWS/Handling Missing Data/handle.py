import pandas as pd

data = {
    "Name": ["John", None, "Peter", "Linda", "Bob", "Raj", "Simran", "Ram"],
    "Age": [28, None, 35, 32, 50, 60, 70, 45],
    "Salary": [50000, None, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score": [85, None, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)
print(df)

# axis=0 -> delete missing element at rows (default)
# axis=1 -> delete missing element at columns
df.dropna(inplace=True)
print(df)