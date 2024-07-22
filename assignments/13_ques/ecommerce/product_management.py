
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_price(self, new_price):
        self.price = new_price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

def add_product(product_list, product):
    product_list.append(product)

def remove_product(product_list, product_id):
    product_list[:] = [p for p in product_list if p.product_id != product_id]
