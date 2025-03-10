import unittest
import pandas as pd
from datetime import datetime, timedelta
from src.visualize import plot_predictions

class TestVisualize(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        data = {
            'Close': [100, 102, 101, 103, 104, 106, 108, 109, 107, 110, 111, 113, 115, 116, 118, 120]
        }
        self.stock_data = pd.DataFrame(data, index=[datetime.today() - timedelta(days=i) for i in range(15, -1, -1)])

    def test_plot_predictions(self):
        future_dates = [datetime.today() + timedelta(days=i) for i in range(1, 6)]
        future_prices = [121, 122, 123, 124, 125]
        plot_predictions(self.stock_data, future_dates, future_prices, 'AAPL', 5)

if __name__ == '__main__':
    unittest.main()