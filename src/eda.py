import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose


def fetch_financial_data(tickers, start_date, end_date):
    """Fetches historical financial data from YFinance."""
    data = yf.download(tickers, start=start_date, end=end_date)
    return data['Close']  # Focus on adjusted close prices

def preprocess_data(df):
    """Preprocesses the financial data."""
    print("Initial Data Info:")
    print(df.info())
    print("\nInitial Data Description:")
    print(df.describe())

    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Fill missing values (forward fill, can be adjusted)
    df.fillna(method='ffill', inplace=True)

    # Ensure correct data types (already done by yfinance, but good practice)
    df.index = pd.to_datetime(df.index)

    return df

def perform_eda(df):
    """Performs exploratory data analysis."""
    plt.figure(figsize=(15, 7))
    for ticker in df.columns:
        plt.plot(df[ticker], label=ticker)
    plt.title("Adjusted Closing Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

    # Daily Percentage Change
    daily_returns = df.pct_change().dropna()
    plt.figure(figsize=(15, 7))
    for ticker in daily_returns.columns:
        plt.plot(daily_returns[ticker], label=ticker)
    plt.title("Daily Percentage Change")
    plt.xlabel("Date")
    plt.ylabel("Returns")
    plt.legend()
    plt.show()

    # Rolling Volatility (20-day window)
    rolling_std = daily_returns.rolling(window=20).std()
    plt.figure(figsize=(15, 7))
    for ticker in rolling_std.columns:
        plt.plot(rolling_std[ticker], label=ticker)
    plt.title("20-Day Rolling Volatility")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.legend()
    plt.show()

    # Seasonality and Trends (TSLA Example)
    decomposition = seasonal_decompose(
        df['TSLA'], model='additive', period=252
    )  # Assuming 252 trading days/year
    decomposition.plot()
    plt.show()

    # Boxplots for outlier detection
    plt.figure(figsize=(15, 7))
    sns.boxplot(data=daily_returns)
    plt.title("Boxplot of Daily Returns")
    plt.show()

    return daily_returns

def calculate_risk_metrics(daily_returns, df):
    """Calculates and analyzes risk metrics."""
    mean_returns = daily_returns.mean()
    std_returns = daily_returns.std()

    # Value at Risk (VaR) - 95% Confidence
    var_95 = daily_returns.quantile(0.05)

    # Sharpe Ratio (Assuming risk-free rate of 0 for simplicity)
    sharpe_ratio = mean_returns / std_returns

    print("\nRisk Metrics:")
    print("Mean Returns:\n", mean_returns)
    print("\nStandard Deviations:\n", std_returns)
    print("\nVaR (95%):\n", var_95)
    print("\nSharpe Ratio:\n", sharpe_ratio)

    print("\n--- VaR and Sharpe Ratio Analysis ---")
    print("\nValue at Risk (VaR):")
    print(
        "VaR at 95% confidence represents the maximum potential loss that an "
        "investment could experience with a 95% probability over a given period."
    )
    print("Lower (more negative) VaR values indicate lower risk. In our analysis:")
    print(f"- TSLA's VaR (95%): {var_95['TSLA']:.4f}")
    print(f"- SPY's VaR (95%): {var_95['SPY']:.4f}")
    print(f"- BND's VaR (95%): {var_95['BND']:.4f}")
    print(
        "TSLA has the highest potential for loss, followed by SPY, while BND "
        "shows the least potential for loss, consistent with our volatility "
        "analysis."
    )

    print("\nSharpe Ratio:")
    print(
        "The Sharpe Ratio measures risk-adjusted return. A higher Sharpe Ratio "
        "indicates better risk-adjusted performance."
    )
    print(f"- TSLA's Sharpe Ratio: {sharpe_ratio['TSLA']:.4f}")
    print(f"- SPY's Sharpe Ratio: {sharpe_ratio['SPY']:.4f}")
    print(f"- BND's Sharpe Ratio: {sharpe_ratio['BND']:.4f}")
    print(
        "While TSLA offers the potential for high returns, its high volatility "
        "results in a Sharpe Ratio that should be considered in light of an "
        "investors risk tolerance. SPY offers a good risk-adjusted return. BND "
        "offers the lowest return, but also the best risk adjusted return."
    )

    # Calculate cumulative returns
    cumulative_returns = (1 + daily_returns).cumprod()

    # Plot cumulative returns
    plt.figure(figsize=(15, 7))
    for ticker in cumulative_returns.columns:
        plt.plot(cumulative_returns[ticker], label=ticker)
    plt.title("Cumulative Returns")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Returns")
    plt.legend()
    plt.show()

    return cumulative_returns  # Return cumulative returns
