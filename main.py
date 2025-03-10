import argparse
import logging
import configparser
from src.fetch_data import fetch_stock_data
from src.data_preparation import prepare_data
from src.model import predict_future_prices_lstm
from src.utils import buy_or_sell_recommendation
from src.visualize import plot_predictions

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Read configuration
config = configparser.ConfigParser()
config.read('config.ini')

def main(ticker, forecast_days):
    try:
        # Fetch and prepare data
        stock_data = fetch_stock_data(ticker)
        stock_data = prepare_data(stock_data)
        stock_data_display = stock_data.iloc[-15:]

        # Predict future prices
        future_dates, future_prices = predict_future_prices_lstm(stock_data, forecast_days)

        # Recommendation
        last_close_price = stock_data['Close'].iloc[-1].item()
        predicted_price = future_prices[0]
        recommendation = buy_or_sell_recommendation(last_close_price, predicted_price)
        logging.info(f"Recommendation: {recommendation}")

        # Plot results
        plot_predictions(stock_data_display, future_dates, future_prices, ticker, forecast_days)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Stock Price Prediction using LSTM')
    parser.add_argument('--ticker', type=str, required=True, help='Stock ticker symbol (e.g., AAPL)')
    parser.add_argument('--forecast_days', type=int, default=5, help='Number of days for future prediction')

    args = parser.parse_args()
    main(args.ticker, args.forecast_days)