# Optimize Portfolio Based on Forecast

## Executive Summary

This report outlines the process of optimizing a sample investment portfolio using forecasted data from Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY). The objective is to adjust the portfolio to maximize returns while minimizing risks based on predicted market trends. The analysis includes portfolio returns, volatility, Sharpe Ratio, and Value at Risk (VaR).

## Portfolio Composition

### Assets
- **Tesla Stock (TSLA)**: A growth stock with higher risk and potential for substantial returns.
- **Vanguard Total Bond Market ETF (BND)**: A bond ETF providing stability and lower risk.
- **S&P 500 ETF (SPY)**: An index fund offering diversification across the market.

### Forecast Data
The forecast includes daily closing prices for each asset, combined into a single DataFrame with columns for TSLA, BND, and SPY.

## Portfolio Analysis

### Returns and Volatility
- **Annual Return Calculation**: The average daily returns for each asset were compounded to estimate annual returns.
- **Covariance Matrix**: This matrix was computed to understand how the returns of the assets move together.

### Portfolio Weights
- **Initial Weights**: The initial allocation was set to 100% in TSLA, with 0% in BND and SPY.
- **Optimization Goal**: The weights were adjusted to maximize the Sharpe Ratio, which measures risk-adjusted return.

### Results
The optimization process yielded the following results:

| Metric                           | Value        |
|----------------------------------|--------------|
| Optimized Portfolio Weights       | TSLA: 1.00, BND: 0.00, SPY: 0.00 |
| Expected Annual Return            | -0.74       |
| Portfolio Volatility              | 0.60        |
| Sharpe Ratio                     | -1.24       |
| TSLA Value at Risk (95% confidence) | -0.0549  |

### Interpretation of Results
- **Expected Annual Return**: A negative expected return of -0.74 indicates potential losses if the current allocation is maintained.
- **Portfolio Volatility**: The volatility of 0.60 reflects the risk associated with the current portfolio allocation, primarily influenced by the high-risk nature of TSLA.
- **Sharpe Ratio**: A Sharpe Ratio of -1.24 suggests that the risk-adjusted return is unfavorable, indicating the need for adjustment in allocations.
- **Value at Risk (VaR)**: The VaR of -0.0549 signifies the potential loss in value of Tesla stock at a 95% confidence level.

## Visualizations

### Cumulative Returns

#### Interpretation:
- The blue line represents the cumulative returns of TSLA, which exhibit significant volatility, reflecting the stock's high-risk profile.
- The orange line shows BND's stable cumulative returns, providing a contrast to TSLA's fluctuations.
- The green line for SPY demonstrates moderate performance, indicative of its diversified nature.
- The cumulative returns chart highlights the potential for loss in TSLA, reinforcing the need for a balanced portfolio.

## Conclusion

The portfolio analysis reveals that the current allocation heavily favors TSLA, leading to high volatility and negative expected returns. To optimize the portfolio, it is advisable to consider increasing allocations to more stable assets like BND and SPY to mitigate risks, especially in an environment where Tesla's stock is forecasted to be volatile.

### Next Steps
- Adjust the portfolio allocations based on risk tolerance and market expectations.
- Continuously monitor the portfolio's performance and adjust as necessary based on changing market conditions.
- Further explore diversification strategies to enhance the risk-return profile.

For more detailed insights and data, please refer to the project repository on [GitHub] https://github.com/eyor23/gmf-portfolio-optimizer.git