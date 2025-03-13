# Time Series Forecasting Models for Tesla Stock Prices

## Executive Summary

This report details the development and evaluation of time series forecasting models to predict Tesla's future stock prices. Three modeling approaches were utilized: ARIMA, SARIMA, and LSTM. The models were trained on historical data and assessed based on their predictive accuracy using key evaluation metrics.

## Methodology

### Model Selection
The following forecasting models were implemented:
- **ARIMA (AutoRegressive Integrated Moving Average)**: Suitable for univariate time series without seasonality.
- **SARIMA (Seasonal ARIMA)**: Extends ARIMA to include seasonal effects.
- **LSTM (Long Short-Term Memory)**: A deep learning model ideal for capturing long-term dependencies in time series data.

### Data Preparation
1. **Dataset Division**: The dataset was split into training and testing sets to evaluate model performance effectively.
2. **Model Training**: Each model was trained using the training set.

### Optimization and Evaluation
- **Parameter Optimization**: The ARIMA model parameters were optimized using a stepwise search to minimize the Akaike Information Criterion (AIC).
- **Evaluation Metrics**:
  - **Mean Absolute Error (MAE)**
  - **Root Mean Squared Error (RMSE)**
  - **Mean Absolute Percentage Error (MAPE)**

### Results
The following models were assessed:

| Model   | MAE     | RMSE    | MAPE    |
|---------|---------|---------|---------|
| ARIMA   | 89.91   | 111.08  | NaN     |
| SARIMA  | 87.67   | 109.25  | NaN     |
| LSTM    | 8.20    | 11.63   | 3.36%   |

### Best Model
The best-performing model was identified as the **LSTM**, exhibiting significantly lower MAE and RMSE values compared to ARIMA and SARIMA.

## Visualization

### TSLA Price Forecasting with ARIMA, SARIMA, and LSTM

TSLA Price Forecasting

#### Interpretation:
- The graph displays the actual Tesla stock prices alongside the predictions made by ARIMA, SARIMA, and LSTM models.
- **LSTM Predictions**: The LSTM model closely follows the actual price trends, showcasing its capacity to capture the underlying patterns in the data.
- **SARIMA Predictions**: The SARIMA model also performs well but exhibits some lag in tracking the actual prices.
- **ARIMA Predictions**: The ARIMA model shows the least accuracy in following the actual price movements, indicating its limitations in capturing complex patterns compared to LSTM.

## Conclusion

The analysis demonstrates that the LSTM model is the most effective approach for forecasting Tesla's stock prices, significantly outperforming traditional ARIMA and SARIMA models. The ability of LSTM to handle non-linear relationships and long-term dependencies in data contributes to its superior predictive performance.

### Next Steps
- Implement the LSTM model in a production environment for real-time forecasting.
- Continuously monitor model performance and retrain with new data to maintain accuracy.
- Explore additional features and external factors that may influence Tesla's stock prices for further model refinement. 

For more details, the complete analysis can be found in the project repository on [GitHub](link_to_github_report).