import pandas as pd

df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['John', 'Jane', 'Bob']
})

df_orders = pd.DataFrame({
    'CustomerID': [1, 2, 4],
    'OrderAmount': [250, 450, 350]
})

# df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="inner")
# print('inner join')
# print(df_merged)

# df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="outer")
# print('outer join')
# print(df_merged)

# df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="left")
# print('left join')
# print(df_merged)

df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="right")
print('right join')
print(df_merged)