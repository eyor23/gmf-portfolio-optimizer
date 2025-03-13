import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam

def create_sequences(data, seq_length=10):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i + seq_length])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

def calculate_metrics(test, forecast, model_name):
    """Calculates MAE and RMSE, handling potential NaN values."""

    # Ensure forecast is same length as test
    min_len = min(len(test), len(forecast))
    test_trimmed = test[:min_len]
    forecast_trimmed = forecast[:min_len]

    mae = (
        np.nan
        if np.all(np.isnan(forecast_trimmed))
        else mean_absolute_error(test_trimmed, forecast_trimmed)
    )
    rmse = (
        np.nan
        if np.all(np.isnan(forecast_trimmed))
        else sqrt(mean_squared_error(test_trimmed, forecast_trimmed))
    )
    mape = (
        np.nan
        if np.all(np.isnan(forecast_trimmed)) or np.any(test_trimmed == 0)
        else np.mean(np.abs((test_trimmed - forecast_trimmed) / test_trimmed)) * 100
    )
    print(f'{model_name} - MAE: {mae:.4f}, RMSE: {rmse:.4f}, MAPE: {mape:.4f}')
