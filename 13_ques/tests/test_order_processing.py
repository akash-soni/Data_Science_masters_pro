# tests/test_order_processing.py

import unittest
from ecommerce.order_processing import Order
from ecommerce.product_management import Product

class TestOrderProcessing(unittest.TestCase):
    
    def test_add_product(self):
        o = Order(1, [])
        p = Product(1, 'Test Product', 100, 10)
        o.add_product(p)
        self.assertEqual(len(o.product_list), 1)
        self.assertEqual(o.product_list[0].name, 'Test Product')

    def test_remove_product(self):
        p1 = Product(1, 'Product 1', 100, 10)
        p2 = Product(2, 'Product 2', 200, 20)
        o = Order(1, [p1, p2])
        o.remove_product(1)
        self.assertEqual(len(o.product_list), 1)
        self.assertEqual(o.product_list[0].name, 'Product 2')
    
    def test_get_total_price(self):
        p1 = Product(1, 'Product 1', 100, 10)
        p2 = Product(2, 'Product 2', 200, 20)
        o = Order(1, [p1, p2])
        self.assertEqual(o.get_total_price(), 300)

if __name__ == '__main__':
    unittest.main()
