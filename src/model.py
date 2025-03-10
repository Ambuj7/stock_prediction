import numpy as np
import logging
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

def predict_future_prices_lstm(stock_data, forecast_days):
    """
    Predict future stock prices using LSTM.

    :param stock_data: DataFrame containing stock data with technical indicators
    :param forecast_days: Number of days to forecast
    :return: List of future dates and predicted prices
    """
    stock_data['Target'] = stock_data['Close'].shift(-1)
    stock_data.dropna(inplace=True)

    features = ['Close', 'MA_10', 'MA_50', 'Volatility', 'Momentum', 'RSI', 'MACD', 'BB_upper', 'BB_lower']
    X = stock_data[features]
    y = stock_data['Target']

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # Reshape for LSTM input (samples, timesteps, features)
    timestep = 10
    X_reshaped = []
    y_reshaped = []
    for i in range(timestep, len(X_scaled)):
        X_reshaped.append(X_scaled[i-timestep:i])
        y_reshaped.append(y.iloc[i])
    X_reshaped, y_reshaped = np.array(X_reshaped), np.array(y_reshaped)

    X_train, X_test, y_train, y_test = train_test_split(X_reshaped, y_reshaped, test_size=0.2, random_state=42, shuffle=False)

    # Build LSTM model
    model = Sequential([
        LSTM(256, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])),
        Dropout(0.3),
        LSTM(256, return_sequences=True),
        Dropout(0.3),
        LSTM(256, return_sequences=False),
        Dropout(0.3),
        Dense(128, activation='relu'),
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mean_squared_error')
    
    # Early stopping to prevent overfitting
    early_stopping = EarlyStopping(monitor='val_loss', patience=50, restore_best_weights=True)
    
    # Learning rate scheduler to reduce learning rate when loss plateaus
    lr_scheduler = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=20, min_lr=1e-6)
    
    # Train model
    logging.info("Training LSTM model.")
    model.fit(X_train, y_train, epochs=1000, batch_size=32, verbose=1, validation_data=(X_test, y_test), 
              callbacks=[early_stopping, lr_scheduler])

    # Predict future prices (daily steps)
    future_dates = [stock_data.index[-1] + timedelta(days=i) for i in range(1, forecast_days + 1)]
    last_known_data = X_scaled[-timestep:]

    future_preds = []
    for _ in range(forecast_days):
        pred_price = model.predict(last_known_data.reshape(1, timestep, -1))[0][0]
        future_preds.append(pred_price)

        # Update for next day's prediction
        new_data = np.append(last_known_data[1:], np.array([[pred_price] * last_known_data.shape[1]]), axis=0)
        last_known_data = new_data

    return future_dates, future_preds