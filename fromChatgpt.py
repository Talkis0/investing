import pandas as pd
import numpy as np
from alpha_vantage.timeseries import TimeSeries
from itertools import product
from tqdm import tqdm
import requests
import csv
import os
"""
identify two sets of two moving averages. one set for selling stock, the other for buying stock. 
set one: ma11 and ma12. when ma11 crosses above ma12, buy stock. this means ma11 will be faster than ma12. very broad numbers for this to start.
ma11 can be like [5,15,25,35,45,55,65] and ma12 can be like [10,25,50,75,100,125,150] starting off with day time frames. from here i can narrow down the time frames 
so that it is more precise. this will be the same for the selling of stock.
set two: ma21 and ma22. when ma21 crosses below ma22, then sell. ma21 will be faster moving than ma22. same time frames as ma11 and ma12 to start but will most likely
change. 

will need daily closing price values and that is it.


"""
import matplotlib.pyplot as plt
# # import csv
# # def compute_buy():
# #     # with open('spy_price.csv', mode ='r')as file:
# #     #     csvFile = csv.reader(file)
# #     #     for lines in csvFile:
# #     #         print(lines)
# # csvFile = pd.read_csv('spy_price.csv')
# # print(csvFile)
# # column_name = 'Close'  # Replace with your actual column name

# # # Plot the column data
# # plt.plot(csvFile[column_name])
# # plt.title(f'{column_name} over Index')
# # plt.xlabel('Index')
# # plt.ylabel(column_name)
# # plt.grid(True)
# # plt.show()

# # csvFile = pd.read_csv('SMA_200.csv')
# # print(csvFile)
# # column_name = 'SMA Values'  # Replace with your actual column name

# # # Plot the column data
# # plt.plot(csvFile[column_name])
# # plt.title(f'{column_name} over Index')
# # plt.xlabel('Index')
# # plt.ylabel(column_name)
# # plt.grid(True)
# # plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# # Load both CSV files
# df1 = pd.read_csv('spy_price.csv')
# df2 = pd.read_csv('SMA_200.csv')
# df3 = pd.read_csv('SMA_150.csv')
# df4 = pd.read_csv('SMA_100.csv')
# df5 = pd.read_csv('SMA_50.csv')
# df6 = pd.read_csv('SMA_10.csv')

# # Plot both on the same graph
# plt.plot(df1['Close'].tail(1000).reset_index(drop=True), label='SPY Close Price')
# plt.plot(df2['SMA Values'].tail(1000).reset_index(drop=True), label='SMA 200')
# plt.plot(df3['SMA Values'].tail(1000).reset_index(drop=True), label='SMA 150')
# plt.plot(df4['SMA Values'].tail(1000).reset_index(drop=True), label='SMA 100')
# plt.plot(df5['SMA Values'].tail(1000).reset_index(drop=True), label='SMA 50')
# plt.plot(df6['SMA Values'].tail(1000).reset_index(drop=True), label='SMA 10')

# plt.title('SPY Close Price and SMA 200')
# plt.xlabel('Index')
# plt.ylabel('Price')
# plt.legend()
# plt.grid(True)
# plt.show()


# compute_buy()
# # === CONFIG ===
# API_KEY = 'BIDSOENB1ORVQ4BI'
# SYMBOL = 'SPY'
# # START_DATE = '2021-01-01'
# # END_DATE = '2024-01-01'
# # API_KEY ='C62GRJ0OMZUVMNVB'
# API_KEY = 'YYUM5UTU5E5A32RA'

# url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={SYMBOL}&outputsize=full&apikey={API_KEY}'
# r = requests.get(url)
# data = r.json()

# print(data)


# ticker = "BA"

# this will give us stock sentiment
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

# month = '2009-01'
# function  = 'BOP'
def csvTechnicalSMA(ticker, time_interval, time_period, series_type, API_KEY):
    current_folder = os.getcwd()
    # print()
    # series_type can equal close, open, high or low
    # time_period can be 
    technical_indicators = {
    'SMA': f'https://www.alphavantage.co/query?function=SMA&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}',
    # 'EMA': f'https://www.alphavantage.co/query?function=EMA&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}',
    # 'WMA': f'https://www.alphavantage.co/query?function=WMA&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}',
    # 'DEMA': f'https://www.alphavantage.co/query?function=DEMA&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}',
    # 'TEMA': f'https://www.alphavantage.co/query?function=TEMA&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}',
    # 'TRIMA': f'https://www.alphavantage.co/query?function=TRIMA&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}',
    # 'KAMA': f'https://www.alphavantage.co/query?function=KAMA&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}',
    # 'MAMA': f'https://www.alphavantage.co/query?function=MAMA&symbol={ticker}&interval={time_interval}&series_type={series_type}&fastlimit=.01&apikey={API_KEY}',
    # 'T3': f'https://www.alphavantage.co/query?function=T3&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}',
    # 'MACDEXT': f'https://www.alphavantage.co/query?function=MACDEXT&symbol={ticker}&interval={time_interval}&series_type={series_type}&apikey={API_KEY}',
    # 'RSI': f'https://www.alphavantage.co/query?function=RSI&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}',
    # 'MOM': f'https://www.alphavantage.co/query?function=MOM&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}',
    # 'STOCH': f'https://www.alphavantage.co/query?function=STOCH&symbol={ticker}&interval={time_interval}&apikey={API_KEY}',
    # 'STOCHF': f'https://www.alphavantage.co/query?function=STOCHF&symbol={ticker}&interval={time_interval}&apikey={API_KEY}',
    # 'STOCHRSI': f'https://www.alphavantage.co/query?function=STOCHRSI&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&fastkperiod=5&fastdmatype=0&apikey={API_KEY}',
    # 'WILLR': f'https://www.alphavantage.co/query?function=WILLR&symbol={ticker}&interval={time_interval}&time_period={time_period}&apikey={API_KEY}',
    # 'ADX': f'https://www.alphavantage.co/query?function=ADX&symbol={ticker}&interval={time_interval}&time_period={time_period}&apikey={API_KEY}',
    # 'ADXR': f'https://www.alphavantage.co/query?function=ADXR&symbol={ticker}&interval={time_interval}&time_period={time_period}&apikey={API_KEY}',
    # 'APO': f'https://www.alphavantage.co/query?function=APO&symbol={ticker}&interval={time_interval}&series_type={series_type}&fastperiod=12&matype=1&apikey={API_KEY}',
    # 'PPO': f'https://www.alphavantage.co/query?function=PPO&symbol={ticker}&interval={time_interval}&series_type={series_type}&fastperiod=12&matype=1&apikey={API_KEY}',
    # 'CCI': f'https://www.alphavantage.co/query?function=CCI&symbol={ticker}&interval={time_interval}&time_period={time_period}&apikey={API_KEY}',
    # 'ROCR': f'https://www.alphavantage.co/query?function=ROCR&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}',
    # 'AROON': f'https://www.alphavantage.co/query?function=AROON&symbol={ticker}&interval={time_interval}&time_period={time_period}&apikey={API_KEY}',
    # 'AROONOSC': f'https://www.alphavantage.co/query?function=AROONOSC&symbol={ticker}&interval={time_interval}&time_period={time_period}&apikey={API_KEY}',
    # 'DX': f'https://www.alphavantage.co/query?function=DX&symbol={ticker}&interval={time_interval}&time_period={time_period}&apikey={API_KEY}',
    # 'MINUS_DI': f'https://www.alphavantage.co/query?function=MINUS_DI&symbol={ticker}&interval={time_interval}&time_period={time_period}&apikey={API_KEY}',
    # 'PLUS_DI': f'https://www.alphavantage.co/query?function=PLUS_DI&symbol={ticker}&interval={time_interval}&time_period={time_period}&apikey={API_KEY}',
    # 'MINUS_DM': f'https://www.alphavantage.co/query?function=MINUS_DM&symbol={ticker}&interval={time_interval}&time_period={time_period}&apikey={API_KEY}',
    # 'PLUS_DM': f'https://www.alphavantage.co/query?function=PLUS_DM&symbol={ticker}&interval={time_interval}&time_period={time_period}&apikey={API_KEY}',
    # 'BBANDS': f'https://www.alphavantage.co/query?function=BBANDS&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&nbdevup=2&nbdevdn=2&apikey={API_KEY}',
    # 'MIDPRICE': f'https://www.alphavantage.co/query?function=MIDPRICE&symbol={ticker}&interval={time_interval}&time_period={time_period}&apikey={API_KEY}',
    # 'SAR': f'https://www.alphavantage.co/query?function=SAR&symbol={ticker}&interval={time_interval}&acceleration=.01&maximum=.2&apikey={API_KEY}',
    # 'AD': f'https://www.alphavantage.co/query?function=AD&symbol={ticker}&interval={time_interval}&apikey={API_KEY}',
    # 'OBV': f'https://www.alphavantage.co/query?function=OBV&symbol={ticker}&interval={time_interval}&apikey={API_KEY}',
    # 'ATR': f'https://www.alphavantage.co/query?function=ATR&symbol={ticker}&interval={time_interval}&time_period={time_period}&apikey={API_KEY}',
    # 'NATR': f'https://www.alphavantage.co/query?function=NATR&symbol={ticker}&interval={time_interval}&time_period={time_period}&apikey={API_KEY}',
    # 'TRANGE': f'https://www.alphavantage.co/query?function=TRANGE&symbol={ticker}&interval={time_interval}&apikey={API_KEY}',
    # 'ROC': f'https://www.alphavantage.co/query?function=ROC&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}',
    # 'MFI': f'https://www.alphavantage.co/query?function=MFI&symbol={ticker}&interval={time_interval}&time_period={time_period}&apikey={API_KEY}',
    # 'TRIX': f'https://www.alphavantage.co/query?function=TRIX&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}',
    # 'ULTOSC': f'https://www.alphavantage.co/query?function=ULTOSC&symbol={ticker}&interval={time_interval}&timeperiod1=8&apikey={API_KEY}',
    # 'CMO': f'https://www.alphavantage.co/query?function=CMO&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}',
    # 'ADOSC': f'https://www.alphavantage.co/query?function=ADOSC&symbol={ticker}&interval={time_interval}&fastperiod=3&apikey={API_KEY}',
    # 'BOP': f'https://www.alphavantage.co/query?function=BOP&symbol={ticker}&interval={time_interval}&apikey={API_KEY}',
    # 'MIDPOINT': f'https://www.alphavantage.co/query?function=MIDPOINT&symbol={ticker}&interval={time_interval}&time_period={time_period}&series_type={series_type}&apikey={API_KEY}',
    # 'HT_TRENDLINE': f'https://www.alphavantage.co/query?function=HT_TRENDLINE&symbol={ticker}&interval={time_interval}&series_type={series_type}&apikey={API_KEY}',
    # 'HT_SINE': f'https://www.alphavantage.co/query?function=HT_SINE&symbol={ticker}&interval={time_interval}&series_type={series_type}&apikey={API_KEY}',
    # 'HT_TRENDMODE': f'https://www.alphavantage.co/query?function=HT_TRENDMODE&symbol={ticker}&interval={time_interval}&series_type={series_type}&apikey={API_KEY}',
    # 'HT_DCPERIOD': f'https://www.alphavantage.co/query?function=HT_DCPERIOD&symbol={ticker}&interval={time_interval}&series_type={series_type}&apikey={API_KEY}',
    # 'HT_DCPHASE': f'https://www.alphavantage.co/query?function=HT_DCPHASE&symbol={ticker}&interval={time_interval}&series_type={series_type}&apikey={API_KEY}',
    # 'HT_PHASOR': f'https://www.alphavantage.co/query?function=HT_PHASOR&symbol={ticker}&interval={time_interval}&series_type={series_type}&apikey={API_KEY}'
    }
    for indicator, url in technical_indicators.items():
        print('indicator: ',indicator,'\n')
        dan = 'gay'
        if 'time_period' in url:
            filename = f'{current_folder}\{indicator}_{time_period}.csv'
        else:
            filename = f'{current_folder}\\{indicator}.csv'
        if not os.path.exists(filename):
            print('indicator in if statement: ',indicator,'\n')
            r = requests.get(url)
            data = r.json()
            print(data,'\n')
            valuesList = list(data.values())
            data = valuesList[1]

            dates = []
            values = []

            # data = data[f'Technical Analysis: {indicator}']
            for key,value in data.items():
                dates.append(key)
                for k, v in value.items():
                    values.append(v)

            data = list(zip(dates, values))
            # folder_path = f'{current_folder}\{ticker}'
        # Open the file in write mode
                # os.makedirs(folder_path)
            with open(filename, 'w', newline='') as csvfile:
                # Create a CSV writer object
                writer = csv.writer(csvfile)

                # Write the header
                writer.writerow(['Dates', f'{indicator} Values'])

                # Write the data to the CSV file
                writer.writerows(data)
        else:
            # The file already exists, so do nothing
            pass
def stock_price_data(symbol, API_KEY):
    # API_KEY = 'GOIR6JKN4TW5HNGO'
    current_folder = os.getcwd()
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    # print(data)
    # Extract the time series data
    time_series = data['Time Series (Daily)']

    if 'Error Message' in data:
        print('An error occurred:', data['Error Message'])

    # Prepare CSV file for writing
    filename = f'{current_folder}\\{symbol}.csv'
    # filename = f'C:\Projects\moneybags\Stocks_daily\{symbol}.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Open', 'High', 'Low', 'Close','Adjusted Close', 'Volume', 'Dividend Amount', 'Split Coefficient'])

        # Write each data point to CSV
        for timestamp, values in time_series.items():
            row = [timestamp, values['1. open'], values['2. high'], values['3. low'], values['4. close'], values['5. volume']]
            writer.writerow(row)

    print(f'Intraday data exported to {filename}')

API_KEY = 'GOIR6JKN4TW5HNGO'
# API_KEY ='C62GRJ0OMZUVMNVB'
# API_KEY = 'BIDSOENB1ORVQ4BI'
# API_KEY = 'FVDFYPUKXD8YETUJ'
ticker = 'SPY'
time_interval = 'daily'
# # time_period = [10, 50, 200]
time_period = 155
# # series_type = ['close','open','high','low']
series_type = 'close'
csvTechnicalSMA(ticker, time_interval, time_period, series_type, API_KEY)

# stock_price_data(ticker,API_KEY)
# price_data(API_KEY, ticker)




# BUY_SMA_RANGE = range(5, 31, 5)
# BUY_SIGNAL_RANGE = range(15, 66, 10)
# SELL_SMA_RANGE = range(5, 31, 5)
# SELL_SIGNAL_RANGE = range(15, 66, 10)

# # === DATA FETCH ===
# def fetch_data(symbol, api_key):
#     ts = TimeSeries(key=api_key, output_format='pandas')
#     data, _ = ts.get_daily(symbol=symbol, outputsize='full')
#     df = data.rename(columns={
#         '1. open': 'Open',
#         '2. high': 'High',
#         '3. low': 'Low',
#         '4. close': 'Close',
#         '5. volume': 'Volume'
#     })
#     df.index = pd.to_datetime(df.index)
#     df = df.sort_index()
#     return df

# # === STRATEGY LOGIC ===
# def backtest(df, buy_sma, buy_signal, sell_sma, sell_signal):
#     df = df.copy()
#     df['buy_sma'] = df['Close'].rolling(buy_sma).mean()
#     df['buy_signal'] = df['Close'].rolling(buy_signal).mean()
#     df['sell_sma'] = df['Close'].rolling(sell_sma).mean()
#     df['sell_signal'] = df['Close'].rolling(sell_signal).mean()

#     buy_condition = df['buy_sma'] > df['buy_signal']
#     sell_condition = df['sell_sma'] < df['sell_signal']

#     position = np.zeros(len(df))
#     for i in range(1, len(df)):
#         if buy_condition.iloc[i] and position[i - 1] == 0:
#             position[i] = 1  # buy
#         elif sell_condition.iloc[i] and position[i - 1] == 1:
#             position[i] = 0  # sell
#         else:
#             position[i] = position[i - 1]  # hold

#     df['position'] = position
#     df['returns'] = df['Close'].pct_change().fillna(0)
#     df['strategy'] = df['returns'] * df['position']

#     total_return = (df['strategy'] + 1).prod() - 1
#     sharpe = df['strategy'].mean() / df['strategy'].std() * np.sqrt(252) if df['strategy'].std() > 0 else 0
#     drawdown = (df['strategy'].cumsum() - df['strategy'].cumsum().cummax()).min()

#     return {
#         'buy_sma': buy_sma,
#         'buy_signal': buy_signal,
#         'sell_sma': sell_sma,
#         'sell_signal': sell_signal,
#         'return': total_return,
#         'sharpe': sharpe,
#         'max_drawdown': drawdown
#     }

# # === GRID SEARCH ===
# def run_grid(df):
#     results = []
#     for params in tqdm(product(BUY_SMA_RANGE, BUY_SIGNAL_RANGE, SELL_SMA_RANGE, SELL_SIGNAL_RANGE), total=len(BUY_SMA_RANGE) * len(BUY_SIGNAL_RANGE) * len(SELL_SMA_RANGE) * len(SELL_SIGNAL_RANGE)):
#         buy_sma, buy_sig, sell_sma, sell_sig = params
#         if max(buy_sma, buy_sig, sell_sma, sell_sig) >= len(df):
#             continue
#         try:
#             result = backtest(df, buy_sma, buy_sig, sell_sma, sell_sig)
#             results.append(result)
#         except Exception:
#             continue
#     return pd.DataFrame(results)

# # === EXECUTE ===
# if __name__ == "__main__":
#     print("Fetching SPY data...")
#     df = fetch_data(SYMBOL, API_KEY)
#     df = df[(df.index >= START_DATE) & (df.index < END_DATE)]

#     print("Running grid search...")
#     results = run_grid(df)

#     if results.empty:
#         print("❌ No results found.")
#     else:
#         top = results.sort_values(by='return', ascending=False).iloc[0]
#         print("\n✅ Best Parameters (Jan 2021–Jan 2024):")
#         print(top)
