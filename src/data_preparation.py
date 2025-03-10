import pandas as pd
import logging

def prepare_data(stock_data):
    """
    Prepare data with technical indicators.

    :param stock_data: DataFrame containing stock data
    :return: DataFrame with technical indicators
    """
    logging.info("Preparing data with technical indicators.")
    stock_data['MA_10'] = stock_data['Close'].rolling(window=10).mean()
    stock_data['MA_50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['Volatility'] = stock_data['Close'].pct_change().rolling(window=10).std()
    stock_data['Momentum'] = stock_data['Close'] - stock_data['Close'].shift(10)

    # RSI Calculation
    delta = stock_data['Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    stock_data['RSI'] = 100 - (100 / (1 + rs))

    # MACD Calculation
    stock_data['EMA_12'] = stock_data['Close'].ewm(span=12, adjust=False).mean()
    stock_data['EMA_26'] = stock_data['Close'].ewm(span=26, adjust=False).mean()
    stock_data['MACD'] = stock_data['EMA_12'] - stock_data['EMA_26']
    
    # Bollinger Bands
    stock_data['BB_std'] = stock_data['Close'].rolling(window=10).std()
    stock_data['BB_upper'] = stock_data['MA_10'] + (stock_data['BB_std'] * 2)
    stock_data['BB_lower'] = stock_data['MA_10'] - (stock_data['BB_std'] * 2)

    stock_data.dropna(inplace=True)
    return stock_data