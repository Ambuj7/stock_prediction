import unittest
import pandas as pd
from src.model import predict_future_prices_lstm
from src.data_preparation import prepare_data

class TestModel(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        data = {
            'Close': [100, 102, 101, 103, 104, 106, 108, 109, 107, 110, 111, 113, 115, 116, 118, 120]
        }
        self.stock_data = prepare_data(pd.DataFrame(data))

    def test_predict_future_prices_lstm(self):
        forecast_days = 5
        future_dates, future_prices = predict_future_prices_lstm(self.stock_data, forecast_days)
        self.assertEqual(len(future_dates), forecast_days)
        self.assertEqual(len(future_prices), forecast_days)

if __name__ == '__main__':
    unittest.main()