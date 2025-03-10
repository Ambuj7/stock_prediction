# Stock Price Prediction using LSTM

This project predicts future stock prices using LSTM (Long Short-Term Memory) neural networks. It fetches historical stock data, performs feature engineering, trains an LSTM model, and provides buy/sell recommendations based on the predicted prices.

## Project Structure

```
stock_prediction/
├── config.ini
├── Dockerfile
├── .dockerignore
├── main.py
├── requirements.txt
├── README.md
├── src/
│   ├── data_preparation.py
│   ├── fetch_data.py
│   ├── model.py
│   ├── utils.py
│   └── visualize.py
└── tests/
    ├── test_data_preparation.py
    ├── test_fetch_data.py
    ├── test_model.py
    ├── test_utils.py
    └── test_visualize.py
```

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerization)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stock_prediction.git
   cd stock_prediction
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the project using `config.ini` file:
   ```ini
   [DEFAULT]
   ticker = AAPL
   forecast_days = 5
   ```

### Running the Project

To run the project, use the following command:
```bash
python main.py --ticker AAPL --forecast_days 5
```

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t stock_prediction .
   ```

2. Run the Docker container:
   ```bash
   docker run -it stock_prediction
   ```

## Testing

Unit tests are located in the `tests` directory. To run the tests, use the following command:
```bash
pytest tests/
```

## License

This project is licensed under the MIT License.