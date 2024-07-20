# main.py

from ecommerce.product_management import Product, add_product, remove_product
from ecommerce.order_processing import Order

# Create some products
product1 = Product(1, 'Laptop', 1500, 10)
product2 = Product(2, 'Smartphone', 800, 20)

# Add products to a list
products = []
add_product(products, product1)
add_product(products, product2)

print("Products after adding:")
for p in products:
    print(f"ID: {p.product_id}, Name: {p.name}, Price: {p.price}, Quantity: {p.quantity}")

# Remove a product
remove_product(products, 1)

print("\nProducts after removing product with ID 1:")
for p in products:
    print(f"ID: {p.product_id}, Name: {p.name}, Price: {p.price}, Quantity: {p.quantity}")

# Create an order
order = Order(1, [product2])

# Add a product to the order
order.add_product(product2)

# Calculate total price of the order
total_price = order.get_total_price()
print(f"\nTotal price of the order: {total_price}")

# Remove a product from the order
order.remove_product(2)

print("\nOrder after removing product with ID 2:")
for p in order.product_list:
    print(f"ID: {p.product_id}, Name: {p.name}, Price: {p.price}, Quantity: {p.quantity}")
