# Time Series Forecasting Models for Tesla Stock Prices

## Executive Summary

This report summarizes the development and evaluation of time series forecasting models aimed at predicting Tesla's future stock prices. Three methodologies were employed: ARIMA, SARIMA, and LSTM. The models were trained on historical data and evaluated using key performance metrics to determine their forecasting accuracy.

## Methodology

### Model Selection
We utilized the following time series forecasting models:

- **ARIMA (AutoRegressive Integrated Moving Average)**: Suitable for univariate time series without seasonality.
- **SARIMA (Seasonal ARIMA)**: An extension of ARIMA that incorporates seasonality into the modeling process.
- **LSTM (Long Short-Term Memory)**: A deep learning model designed to capture long-term dependencies and patterns in time series data.

### Model Optimization
A stepwise search was conducted to minimize the Akaike Information Criterion (AIC) and identify the best ARIMA model parameters. The results of various ARIMA configurations are as follows:

| Model Configuration             | AIC        | Time (sec) |
|---------------------------------|------------|------------|
| ARIMA(2,1,2)(0,0,0)[0] intercept | 12684.802  | 1.92       |
| ARIMA(0,1,0)(0,0,0)[0] intercept | 12680.726  | 0.16       |
| ARIMA(1,1,0)(0,0,0)[0] intercept | 12679.653  | 0.28       |
| ARIMA(0,1,1)(0,0,0)[0] intercept | 12679.753  | 1.05       |
| ARIMA(0,1,0)(0,0,0)[0]          | 12678.997  | 0.13       |
| ARIMA(1,1,1)(0,0,0)[0] intercept | 12680.805  | 3.52       |

### Best Model
The best-performing model identified was **ARIMA(0,1,0)(0,0,0)[0]**, with the lowest AIC value of 12678.997. The total fitting time for all models was 7.070 seconds.

### Evaluation Metrics
Each model was evaluated based on the following metrics:

| Model   | MAE      | RMSE     | MAPE     |
|---------|----------|----------|----------|
| ARIMA   | 89.91    | 111.08   | NaN      |
| SARIMA  | 87.67    | 109.25   | NaN      |
| LSTM    | 52.10    | 71.83    | 25.17%   |

### LSTM Model Training
The LSTM model used a sequence length of 60 and was trained with the following configuration:

- **Architecture**: 
  - Two LSTM layers (50 units each)
  - One Dense layer with 25 units
  - One output Dense layer
  
- **Optimization**: The model was compiled using the Adam optimizer with a learning rate of 0.001 and trained for 20 epochs with a batch size of 16.

### Performance
The LSTM model achieved the best performance, significantly outperforming both ARIMA and SARIMA in terms of MAE and RMSE.

## Visualization

### TSLA Price Forecasting with ARIMA, SARIMA, and LSTM

#### Interpretation:
- The graph displays actual Tesla stock prices along with the predictions from ARIMA, SARIMA, and LSTM models.
- **LSTM Predictions**: The LSTM model closely follows the actual price trends, demonstrating its effectiveness in capturing complex patterns in the data.
- **SARIMA Predictions**: The SARIMA model provides a reasonable approximation but lags behind the actual prices, indicating some limitations in tracking rapid changes.
- **ARIMA Predictions**: The ARIMA model shows the least accuracy, failing to capture the volatility and trends present in the actual data.

## Conclusion

The analysis confirms that the LSTM model is the most effective approach for forecasting Tesla's stock prices, demonstrating significantly better predictive accuracy compared to traditional ARIMA and SARIMA models. The ability of LSTM to handle non-linear relationships and learn from long sequences contributes to its superior performance.


For more detailed insights, please refer to the full project repository on https://github.com/eyor23/gmf-portfolio-optimizer.git