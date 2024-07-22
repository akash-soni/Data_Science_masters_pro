

class Order:
    def __init__(self, order_id, product_list):
        self.order_id = order_id
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product_id):
        self.product_list[:] = [p for p in self.product_list if p.product_id != product_id]

    def get_total_price(self):
        return sum(p.price for p in self.product_list)
