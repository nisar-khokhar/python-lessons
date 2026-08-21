import pandas as pd

# sales  = [199, 198.98, 1 , 543.0]
# print(sales)

order = [{"Customer_name": "Ali", "Sales": 201, "Region": "Central"},
         {"Customer_name": "Hassan", "Sales": 101, "Region": "West"},
         {"Customer_name": "Hussain", "Sales": 301, "Region": "North"}]

# print(order[0]["Customer_name"])

# for i in order:
#     print(i["Customer_name"])

# df = pd.DataFrame(data=order)
# print(df)

df = pd.read_csv("superstore.csv")
# print(df.head(10))
# print(df.tail())

# print(df.describe())
print(df.info())