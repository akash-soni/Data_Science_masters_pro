# tests/test_product_management.py

import unittest
from ecommerce.product_management import Product, add_product, remove_product

class TestProductManagement(unittest.TestCase):
    
    def test_add_product(self):
        products = []
        p = Product(1, 'Test Product', 100, 10)
        add_product(products, p)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, 'Test Product')
    
    def test_remove_product(self):
        p1 = Product(1, 'Product 1', 100, 10)
        p2 = Product(2, 'Product 2', 200, 20)
        products = [p1, p2]
        remove_product(products, 1)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, 'Product 2')

if __name__ == '__main__':
    unittest.main()
