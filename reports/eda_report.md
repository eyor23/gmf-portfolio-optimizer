# Guide Me in Finance (GMF) Investments: Exploratory Data Analysis Report
# GitHub Repo name: gmf-portfolio-optimizer

## Executive Summary

Guide Me in Finance (GMF) Investments is a pioneering financial advisory firm focused on personalized portfolio management. The firm employs cutting-edge technology and data analytics to provide clients with tailored investment strategies. Utilizing advanced time series forecasting models, GMF aims to predict market trends, optimize asset allocation, and enhance portfolio performance. This report outlines the findings from exploratory data analysis (EDA) performed on historical financial data sourced from YFinance.

## Business Need

As a Financial Analyst at GMF Investments, the primary goal is to enhance portfolio management through time series forecasting. By analyzing historical financial data, building predictive models, and providing actionable insights, the firm seeks to optimize returns while managing risks.

### Objectives:
- Extract historical financial information (stock prices, market indices, etc.) from YFinance.
- Preprocess and analyze data to identify trends and patterns.
- Develop and evaluate forecasting models to predict market movements.
- Recommend portfolio adjustments based on forecasted trends.

## Initial Data Overview

The dataset comprises historical prices for three financial instruments: BND (Bond), SPY (S&P 500 ETF), and TSLA (Tesla Inc.). Below are the key statistics derived from the initial analysis.

### Data Summary

- **Total Entries**: 2535 (from 2015-01-02 to 2025-01-30)
- **Columns**: BND, SPY, TSLA
- **Data Types**: All columns are of type float64.

### Descriptive Statistics

| Ticker | Count | Mean      | Std Dev  | Min      | 25%      | 50%      | 75%      | Max        |
|--------|-------|-----------|----------|----------|----------|----------|----------|------------|
| BND    | 2535  | 69.08     | 4.78     | 61.68    | 65.37    | 68.13    | 72.66    | 78.59      |
| SPY    | 2535  | 316.07    | 117.93   | 156.80   | 214.84   | 277.12   | 405.87   | 609.75     |
| TSLA   | 2535  | 117.85    | 116.51   | 9.58     | 17.23    | 30.30    | 221.53   | 479.86     |

### Missing Values
- All columns have 0 missing values.

## Risk Metrics Analysis

### Mean Returns

| Ticker | Mean Return |
|--------|-------------|
| BND    | 0.000062    |
| SPY    | 0.000557    |
| TSLA   | 0.001952    |

### Standard Deviations

| Ticker | Std Dev     |
|--------|-------------|
| BND    | 0.003427    |
| SPY    | 0.011083    |
| TSLA   | 0.036005    |

### Value at Risk (VaR) at 95% Confidence Level

| Ticker | VaR         |
|--------|-------------|
| BND    | -0.004802   |
| SPY    | -0.016719   |
| TSLA   | -0.051387   |

### Sharpe Ratio

| Ticker | Sharpe Ratio |
|--------|--------------|
| BND    | 0.018204     |
| SPY    | 0.050239     |
| TSLA   | 0.054218     |

## Visualizations

The following visualizations provide insights into the historical performance and volatility of the financial instruments analyzed.

### 1. Adjusted Closing Prices Over Time

The graph displays the adjusted closing prices of BND, SPY, and TSLA from January 2015 to January 2025.

#### Interpretation:
BND shows relatively stable prices, indicating lower volatility.
SPY exhibits moderate growth, reflecting the overall performance of the S&P 500 index.
TSLA demonstrates significant volatility and rapid growth, particularly after 2020, indicating its higher risk and potential for high returns.

### 2. Daily Percentage Change

The visualization shows the daily percentage change in prices for each asset.

#### Interpretation:
TSLA displays the highest variability in daily returns, suggesting it is more volatile than both BND and SPY.
SPY has moderate fluctuations, while BND shows the least variability, indicating its role as a more stable investment.

### 3. 20-Day Rolling Volatility

The chart illustrates the 20-day rolling volatility for each asset.

#### Interpretation:
TSLA exhibits spikes in volatility, especially during significant market events, reflecting its higher risk.
SPY shows occasional increases in volatility, while BND maintains a consistent low level, reinforcing its position as a low-risk asset.

### 4. TSLA Time Series Decomposition

The visualization breaks down TSLA’s price series into trend, seasonal, and residual components.

#### Interpretation:
The trend component shows a general upward movement, indicating strong long-term growth.
The seasonal component suggests predictable fluctuations in certain periods, likely influenced by market cycles.
The residual component indicates random variations not explained by the trend or seasonality, which can affect short-term performance.

### 5. Boxplot of Daily Returns

The boxplot displays the distribution of daily returns for BND, SPY, and TSLA.

#### Interpretation:
TSLA has a wider interquartile range and more outliers, emphasizing its high risk and potential for extreme returns.
SPY shows a more moderate distribution, while BND has the narrowest range, indicating its stability and lower risk.

### 6. Cumulative Returns

This graph illustrates the cumulative returns of BND, SPY, and TSLA over the observed period.

#### Interpretation:
TSLA shows the highest cumulative returns, highlighting its potential for significant growth.
SPY provides steady returns, while BND offers minimal cumulative growth, consistent with its lower risk profile but also lower return potential.

## Conclusion

The exploratory data analysis reveals significant insights into the performance and risks associated with BND, SPY, and TSLA. The findings will inform portfolio adjustments aimed at optimizing returns while managing risks. GMF Investments is positioned to leverage these insights to enhance its advisory services and provide clients with tailored investment strategies.

---

For further details, please refer to the full report available on [GitHub] https://github.com/eyor23/gmf-portfolio-optimizer.git