product1_name = input("Enter product 1 name: ")
product1_price = float(input("Enter product 1 price: "))

# Collect item 2
product2_name = input("Enter product 2 name: ")
product2_price = float(input("Enter product 2 price: "))

# Collect item 3
product3_name = input("Enter product 3 name: ")
product3_price = float(input("Enter product 3 price: "))

# Calculate total
total = product1_price + product2_price + product3_price

# Print formatted receipt
print("\n-----------------------")
print(f"{product1_name:<15} ${product1_price:>6.2f}")
print(f"{product2_name:<15} ${product2_price:>6.2f}")
print(f"{product3_name:<15} ${product3_price:>6.2f}")
print("------------------------")
print(f"{'TOTAL':<15} ${total:>6.2f}")