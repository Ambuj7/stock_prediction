import unittest
from src.utils import buy_or_sell_recommendation

class TestUtils(unittest.TestCase):

    def test_buy_recommendation(self):
        last_close_price = 100
        predicted_price = 105
        recommendation = buy_or_sell_recommendation(last_close_price, predicted_price)
        self.assertEqual(recommendation, "BUY")

    def test_sell_recommendation(self):
        last_close_price = 100
        predicted_price = 90
        recommendation = buy_or_sell_recommendation(last_close_price, predicted_price)
        self.assertEqual(recommendation, "SELL")

    def test_hold_recommendation(self):
        last_close_price = 100
        predicted_price = 101
        recommendation = buy_or_sell_recommendation(last_close_price, predicted_price)
        self.assertEqual(recommendation, "HOLD")

if __name__ == '__main__':
    unittest.main()