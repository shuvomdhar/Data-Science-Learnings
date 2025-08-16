import pandas as pd

# df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

'''
xlrd (version 2.0.1 and above) only supports .xls files, not .xlsx.
If your file is .xlsx, you should use the openpyxl engine instead.
df = pd.read_excel("SampleSuperstore.xlsx", engine="openpyxl")
'''

# df = pd.read_excel("SampleSuperstore.xlsx")
df = pd.read_json("sample_Data.json")
print(df)