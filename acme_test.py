#!/usr/bin/env python

import unittest
from acme import Product, BoxingGlove
import acme_report



class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    
    def test_default_product_weight(self):
        """Test default product weight for being 20"""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
    
    def test_product_stealability_explode(self):
        """Test product stealability"""
        prod = prod = Product('Test Product')
        stealable = prod.stealability()
        explodable = prod.explode() 
        self.assertEqual(stealable, 'Kinda stealable.')
        self.assertEqual(explodable, '...boom!')

class AcmeReportTests(unittest.TestCase):
    """Test Acme Reporting Functions"""
    def test_default_num_products(self):
        """Test default number of items is 30 in report"""
        x = acme_report.generate_products()
        self.assertEqual(len(x), 30)
    
    def test_legal_names(self):
        """Test for legal names"""
        prods = acme_report.generate_products()
        adj_list = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        noun_list = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
        for i in range(len(prods)):
            p_name = prods[i].name
            split_list = p_name.split()
            self.assertIn(split_list[0],adj_list)
            self.assertIn(split_list[1],noun_list)

if __name__ == '__main__':
    unittest.main()