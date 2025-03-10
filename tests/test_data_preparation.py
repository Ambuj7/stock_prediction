import unittest
import pandas as pd
from src.data_preparation import prepare_data

class TestDataPreparation(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        data = {
            'Close': [100, 102, 101, 103, 104, 106, 108, 109, 107, 110, 111, 113, 115, 116, 118, 120]
        }
        self.stock_data = pd.DataFrame(data)

    def test_prepare_data(self):
        prepared_data = prepare_data(self.stock_data)
        self.assertIn('MA_10', prepared_data.columns)
        self.assertIn('MA_50', prepared_data.columns)
        self.assertIn('Volatility', prepared_data.columns)
        self.assertIn('Momentum', prepared_data.columns)
        self.assertIn('RSI', prepared_data.columns)
        self.assertIn('MACD', prepared_data.columns)
        self.assertIn('BB_upper', prepared_data.columns)
        self.assertIn('BB_lower', prepared_data.columns)

if __name__ == '__main__':
    unittest.main()