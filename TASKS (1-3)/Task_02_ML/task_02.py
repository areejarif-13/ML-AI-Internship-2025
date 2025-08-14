#-------------------------------------------Libraries
import yfinance as yf
import pandas as pd
import time
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import sklearn.metrics as mean_squared_error
#---------------------------------------initializing the duration of data
start_date = '2005-12-12'
end_date = '2020-03-03'
#------------------------------------initializing the data for Tesla
tickers = 'TSLA'
#--------------------------------------loading the tickers
try:
    df = yf.download(tickers, start=start_date, end=end_date, auto_adjust=False)
    df.reset_index(inplace=True)
except ValueError:
    print("No Data Found!")
else:
    df.to_csv(f"{tickers}.csv")
    print(" Data Downloaded")
#--------------------------------------delay time
time.sleep(5)
#------------------------main()-------------------------
#--------------------------------------Convertion to dataframe
df.index = pd.to_datetime(df.index)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
#-----------------------------------------------------Computing Diffrent Features for Model to learn From
df['Next_Close'] = df['Close'].shift(-1)
df['PriceChange'] = df['Close'] - df['Open']
df['Volatility'] = df['High'] - df['Low']
df['DailyReturnValue'] = df['Close'].pct_change()  #Calculates the percentage chnage of Closing Value
df['Moving_AV_L10'] = df['Close'].rolling(10).mean()  # Calculates the moving average of last 10 days
df['Moving_AV_50'] = df['Close'].rolling(50).mean()  # Calculates the moving average of last 50 days
df.dropna(inplace=True)
#----------------------------------------------------Assigning the training data to variables
X = df[
    ['Open', 'High', 'Low', 'Volume', 'PriceChange',
     'Volatility', 'DailyReturnValue', 'Moving_AV_L10',
     'Moving_AV_50']]
y = df['Next_Close']
#------------------------------------------------model training
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False)
model = RandomForestRegressor(random_state=0)
model.fit(X_train, y_train.values.ravel())
y_predict = model.predict(X_test)
y_predict_all = pd.Series(y_predict, index=y_test.index)
last_row = X.iloc[[-1]]
next_day_pred = model.predict(last_row)[0]
#-------------------------------------------------------MSE
# mse=mean_squared_error(y_test, y_predict)
# print(f"Mean Squared Error: {mse:2f}")
#--------------------------------------------------------graphs
plt.figure(figsize=(14, 6))
plt.plot(y_test.index,y_test, color='blue', label='Actual')
plt.plot(y_predict_all.index,y_predict_all, color='pink', label='Predicted (Test)')
plt.scatter(df.index[-1] + pd.Timedelta(days=1), next_day_pred, color='red', label='Next Day Prediction')
plt.title(f'Next Day Close Price Prediction for {tickers.upper()}')
plt.xlabel('Index(date)')
plt.ylabel('Price($)')
plt.grid(True)
plt.legend()
plt.show()
print(f"Predicted closing price for the next day: ${next_day_pred:.2f}")
#-------------------------------------------------------------end of program
