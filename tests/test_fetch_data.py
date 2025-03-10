import unittest
from src.fetch_data import fetch_stock_data

class TestFetchData(unittest.TestCase):

    def test_fetch_stock_data(self):
        ticker = 'AAPL'
        stock_data = fetch_stock_data(ticker)
        self.assertFalse(stock_data.empty)

if __name__ == '__main__':
    unittest.main()