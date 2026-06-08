# Product Price Analysis

prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# Display products costing more than ₹5000
print("Products costing more than ₹5000:")
for product, price in prices.items():
    if price > 5000:
        print(product, ":", price)

# Count products costing less than ₹3000
count = 0
for price in prices.values():
    if price < 3000:
        count += 1

print("\nProducts costing less than ₹3000:", count)

# Find the most expensive product
max_product = ""
max_price = 0

for product, price in prices.items():
    if price > max_price:
        max_price = price
        max_product = product

print("\nMost Expensive Product:", max_product, "-", max_price)

# Create a list of products priced between ₹2000 and ₹10000
price_range = []

for product, price in prices.items():
    if 2000 <= price <= 10000:
        price_range.append(product)

print("\nProducts priced between ₹2000 and ₹10000:")
print(price_range)

# Calculate the total value of all products
total_value = 0

for price in prices.values():
    total_value += price

print("\nTotal Value of All Products:", total_value)