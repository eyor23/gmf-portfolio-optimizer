# gmf-portfolio-optimizer
A data-driven portfolio optimization and forecasting tool by Guide Me in Finance (GMF) Investments. This project leverages real-time market data, statistical modeling, and machine learning to enhance asset allocation and maximize risk-adjusted returns.

```markdown

This repository contains the code and documentation for a project that focuses on predicting stock market prices using LSTM models and optimizing a portfolio based on these predictions.

## Project Overview

This project aims to:

1. **Retrieve and preprocess financial data** from Yahoo Finance.
2. **Build and train LSTM models** to predict stock prices.
3. **Implement a trading strategy** based on the model's predictions.
4. **Optimize a portfolio** using forecasted data.
5. **Create a dashboard** to visualize key metrics and performance.

## Tasks

### Task 1: Data Retrieval and Preprocessing
- **Objective:** Fetch historical stock data for TSLA, BND, and SPY from Yahoo Finance and preprocess it for analysis.
- **Implementation:**
  - Used `yfinance` to download data.
  - Handled missing values and converted data types.
  - Split the data into training and testing sets.

### Task 2: LSTM Model Building and Training
- **Objective:** Develop and train an LSTM model to predict stock prices.
- **Implementation:**
  - Created sequences of data for LSTM input.
  - Built an LSTM model using TensorFlow Keras.
  - Trained the model and evaluated its performance using MAE, RMSE, and MAPE.
  - Experimented with different `seq_length` values.

### Task 3: Trading Strategy Implementation
- **Objective:** Implement a trading strategy based on the LSTM model's predictions.
- **Implementation:**
  - Developed a strategy to buy and sell stocks based on predicted price changes.
  - Calculated portfolio value, returns, and performance metrics.
  - Visualized the portfolio's performance over time.

### Task 4: Portfolio Optimization Based on Forecast
- **Objective:** Optimize a portfolio using forecasted stock prices.
- **Implementation:**
  - Fetched data for TSLA, BND, and SPY.
  - Generated placeholder forecast data.
  - Calculated annual returns and covariance matrices.
  - Optimized portfolio weights using the Sharpe Ratio.
  - Analyzed portfolio risk and return.
  - Visualized portfolio performance.

### Bonus Task: Dashboard
- **Objective:** Create a dashboard to visualize key metrics and performance.
- **Implementation:**
  - Used Streamlit to build an interactive dashboard.
  - Displayed stock price predictions, portfolio performance, and other relevant metrics.
  - Included interactive elements for user input and customization.

## Repository Structure

```
├── notebooks/
│   ├── eda.ipynb # Used for EDA
│   ├── forecast_future_market_trends.ipynb # Used for market trend forecasting
│   ├── optimize_portfolio_based_on_forecast.ipynb # Used for portfolio optimization
│   └── time_series_forecasting.ipynb # Used for time series forecasting and modeling
├── reports/
│   ├── eda_report.md # Used for EDA
│   ├── future-market-trend.md # Used for market trend forecasting
│   ├── optimized-portfolio.md # Used for portfolio optimization
│   └── time-series-report.md # Used for time series forecasting and modeling
├── models/
│   ├── lstm_model.h5 # LSTM Model for TSLA
│   ├── lstm_model.keras # LSTM Model for TSLA in Keras
│   └── lstm_model.pkl # LSTM older model
├── src/
│   ├── eda.py # Used for EDA
│   └── time_series_forecast.py # Used for time series forecasting and modeling
├── dashboard/
│   └── app_py.py (Streamlit dashboard)
├── README.md
├── requirements.txt
├── LICENSE
```

## Installation

1. Clone the repository:

   ```bash
   git clone [repository URL]
   cd [repository directory]
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the scripts for data analysis and modeling:**

   ```bash
   python src/eda.py  # For exploratory data analysis
   python src/time_series_forecast.py  # For time series forecasting and modeling
   ```

2. **Run the Jupyter notebooks for detailed analysis:**
   - Open Jupyter Notebook and run the following notebooks:
     - `notebooks/eda.ipynb`
     - `notebooks/forecast_future_market_trends.ipynb`
     - `notebooks/optimize_portfolio_based_on_forecast.ipynb`
     - `notebooks/time_series_forecasting.ipynb`

3. **Run the dashboard:**

   ```bash
   streamlit run dashboard/app_py.py
   ```

## Dependencies

- pandas
- numpy
- matplotlib
- yfinance
- scikit-learn
- tensorflow
- streamlit
- scipy

## Model Selection

- **TSLA:** LSTM (due to high volatility and non-linearity)
- **BND:** ARIMA (due to stable and relatively linear behavior)
- **SPY:** LSTM (due to upward trend and non-linear characteristics)

## Results and Analysis

- Detailed results and analysis are included in the scripts and dashboard.
- The LSTM model's performance varies depending on the `seq_length` and asset.
- The portfolio optimization aims to maximize the Sharpe Ratio.
- The dashboard provides an interactive visualization of the project's outputs.

## Future Improvements

- Implement more sophisticated forecasting models (e.g., SARIMA, Prophet).
- Incorporate real-time data updates.
- Add more advanced portfolio optimization techniques.
- Enhance the dashboard with more interactive features.
- Implement backtesting to evaluate trading strategies.
- Add unit tests.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements.

## License

This project is licensed under the MIT License. See the [LICENSE] file for details.

Eyor Getachew
March 14, 2025