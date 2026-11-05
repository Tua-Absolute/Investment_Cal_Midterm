apple_stock = 10
ostock_price = 150
nstock_price = 175
years = 1
total_price = (apple_stock * nstock_price)
total_return = ((total_price / (apple_stock * ostock_price) ** (1 / years) - 1) * 100)

print("INVESTMENT CALCULATOR")
print(f"Apple Stock Amount: {apple_stock}")
print(f"Current Stock Value: ${nstock_price}")
print(f"Total Investment Cost: ${total_price}")
print(f"Total Return on Investment: {total_return:.2f}%")