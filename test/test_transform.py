import unittest
import pandas as pd
from utils.transform import process_product_data

class TestTransform(unittest.TestCase):

    def test_transform_data(self):
        # Arrange
        products = [
            {'title': 'Product 1', 'price': '10000', 'rating': '4.5', 'colors': '3', 'size': 'M', 'gender': 'Men'},
            {'title': 'Product 2', 'price': '20000', 'rating': '5.0', 'colors': '3', 'size': 'L', 'gender': 'Women'}
        ]
        
        # Act
        df = process_product_data(products)
        
        # Assert
        self.assertEqual(len(df), 2)
        self.assertIn('price', df.columns)
        self.assertIn('rating', df.columns)
        self.assertIn('timestamp', df.columns)
        self.assertTrue(df['price'].iloc[0] > 0)
        self.assertTrue(df['rating'].iloc[0] > 0)

    def test_invalid_price(self):
        # Arrange
        products = [
            {'title': 'Product 1', 'price': 'invalid_price', 'rating': '4.5', 'colors': '3', 'size': 'M', 'gender': 'Men'}
        ]
        
        # Act
        df = process_product_data(products)
        
        # Assert
        self.assertEqual(len(df), 0) 
if __name__ == '__main__':
    unittest.main()