import logging

def buy_or_sell_recommendation(last_close_price, predicted_price):
    """
    Determine buy or sell recommendation based on predicted price.

    :param last_close_price: Last known close price
    :param predicted_price: Predicted price
    :return: Recommendation string ("BUY", "SELL", or "HOLD")
    """
    if predicted_price > last_close_price * 1.02:  # 2% increase threshold
        return "BUY"
    elif predicted_price < last_close_price * 0.95:  # 5% decrease threshold
        return "SELL"
    else:
        return "HOLD"