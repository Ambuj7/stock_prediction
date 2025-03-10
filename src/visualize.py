import matplotlib.pyplot as plt

def plot_predictions(stock_data, future_dates, future_prices, ticker, forecast_days):
    """
    Plot historical and predicted stock prices.

    :param stock_data: DataFrame containing historical stock prices
    :param future_dates: List of future dates for prediction
    :param future_prices: List of predicted prices
    :param ticker: Stock ticker symbol
    :param forecast_days: Number of days for future prediction
    """
    plt.figure(figsize=(14, 7))
    plt.plot(stock_data.index, stock_data['Close'], label='Historical Prices (Last 15 Days)', color='blue', marker='o', linestyle='-')
    plt.plot(future_dates, future_prices, label=f'Predicted Prices ({forecast_days} days, LSTM, Daily)', linestyle='dashed', color='red', marker='x')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title(f'{ticker} Stock Price Prediction (LSTM - Daily)')
    plt.legend()
    plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()