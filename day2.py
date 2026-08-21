print("-----------P1------------")
raw = "   LOS angeles   "
refined = raw.strip().title()
print(raw)  # Output: "   LOS angeles   "
print(refined)  # Output: "Los Angeles"

print("-----------P2------------")
revenue = "  160 € "
revenue_cleaned = float(revenue.strip().replace("€", "").strip())
print(revenue_cleaned)  # Output: 160.0
print(revenue_cleaned + 100)  # Output: 260.0

print("-----------P3------------")
order_id = "US-2015-108966"
print("\n".join(order_id.split("-"))) 


print("-----------P4------------")
sales = [261.96, 731.94, 14.62, 957.58, 22.37]
print(len(sales))
print(sum(sales))
print(float(sum(sales) / len(sales)))
print(max(sales))
print(sorted(sales)[-2:])

print("-----------P5------------")
regions = ["West", "East", "West", "Central", "South", "West"]
print(regions.count("West"))


print("-----------P6------------")
profit = 250.75
if(profit > 0):
    print("Profit is positive")
else:
    print("Profit is negative")

print("-----------P7------------")
sale = 500
if(sale >= 1000):
    print("High")
elif(sale >= 100):
    print("Medium")
else:
    print("Low")



