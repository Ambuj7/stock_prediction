import yfinance as yf
import logging
from datetime import datetime, timedelta

def fetch_stock_data(ticker):
    """
    Fetch stock data for the past year.

    :param ticker: Stock ticker symbol
    :return: DataFrame containing stock data
    """
    logging.info(f"Fetching stock data for {ticker}.")
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365)
    stock = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'), interval='1d')
    if stock.empty:
        logging.error(f"No data found for {ticker}.")
        raise ValueError(f"No data found for {ticker}.")
    return stock
