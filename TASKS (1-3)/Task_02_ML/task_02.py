import yfinance as yf
import pandas as pd
import time
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# Parameters
start_date = '2005-12-12'
end_date = '2020-03-03'
ticker = 'TSLA'

# Download data
try:
    data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)
except ValueError:
    print("No Data Found!")
else:
    data.to_csv(f"{ticker}.csv")
    print("Data Downloaded")

time.sleep(5)

# Prepare DataFrame
df = data.copy()
df.dropna(inplace=True)
df.index = pd.to_datetime(df.index)  # Ensure datetime index

# Create target and features
df['Next_Close'] = df['Close'].shift(-1)
df['PriceChange'] = df['Close'] - df['Open']
df['Volatility'] = df['High'] - df['Low']
df['DailyReturnValue'] = df['Close'].pct_change()
df['Moving_AV_L10'] = df['Close'].rolling(10).mean()
df['Moving_AV_50'] = df['Close'].rolling(50).mean()

df.dropna(inplace=True)

X = df[['Open', 'High', 'Low', 'Volume', 'PriceChange',
        'Volatility', 'DailyReturnValue', 'Moving_AV_L10', 'Moving_AV_50']]
y = df['Next_Close']

# Train/test split (time-series)
split_idx = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

# Train model
model = RandomForestRegressor(random_state=0)
model.fit(X_train, y_train)
y_pred = pd.Series(model.predict(X_test), index=y_test.index)

# Plot results
plt.figure(figsize=(12,6))
plt.plot(y_test.index, y_test, color='blue', label='Actual')
plt.plot(y_test.index, y_pred, color='pink', label='Predicted')
plt.grid(True)
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.title(f'Next Day Close Price Prediction for {ticker}')
plt.show()
