import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations

# Load CSVs
df1 = pd.read_csv('spy_price.csv')
df2 = pd.read_csv('SMA_200.csv')
df3 = pd.read_csv('SMA_150.csv')
df4 = pd.read_csv('SMA_100.csv')
df5 = pd.read_csv('SMA_50.csv')
df6 = pd.read_csv('SMA_10.csv')

# Tail and align
price = df1['Close'].tail(1000).reset_index(drop=True)
smas = {
    'SMA_200': df2['SMA Values'].tail(1000).reset_index(drop=True),
    'SMA_150': df3['SMA Values'].tail(1000).reset_index(drop=True),
    'SMA_100': df4['SMA Values'].tail(1000).reset_index(drop=True),
    'SMA_50': df5['SMA Values'].tail(1000).reset_index(drop=True),
    'SMA_10': df6['SMA Values'].tail(1000).reset_index(drop=True)
}
# print(smas['SMA_200'][0])
# print(smas['SMA_50'][0])
# print(price[0])
# plt.plot(smas['SMA_10'])
# plt.show()
sma_200 = smas['SMA_200']
sma_150 = smas['SMA_150']
sma_100 = smas['SMA_100']
sma_50 = smas['SMA_50']
sma_10 = smas['SMA_10']
value = 0
equity = 100
buy=False
for i in range(1,len(sma_200)):

    # if the 50 sma moves above the 200 sma and currently do not hold, buy
    if sma_200[i] < sma_50[i] and sma_200[i-1] > sma_50[i-1] and buy == False:
        # print(f"Index {i}: SMA_200 > SMA_50 ({sma_200[i]} > {sma_50[i]})")

        #simulate buying share
        value = price[i]
        buy = True
    
    # if the 50 sma moves below the 200 sma and currently hold stock, sell
    if sma_200[i] > sma_50[i] and sma_200[i-1] < sma_50[i-1] and buy == True:

        # value is the change in percentage between the buy and the sell
        value = price[i]/value
        buy = False

        # change in value multiplied by equity to get new equity value
        equity = equity*value
    # else:
    #     print(f"Index {i}: SMA_200 <= SMA_50 ({sma_200[i]} <= {sma_50[i]})")

print(equity)
# sma_200 = smas['SMA_200']

results = {}
for long_name, short_name in combinations(smas.keys(), 2):
    short_sma = smas[short_name]
    long_sma = smas[long_name]

    value = 0
    equity = 100
    buy = False
    print("short_sma",short_name,"    long_sma",long_name)
    for i in range(1, len(price)):
        # Buy signal: short SMA crosses above long SMA
        if short_sma[i] > long_sma[i] and short_sma[i-1] < long_sma[i-1] and not buy:
            value = price[i]
            buy = True

        # Sell signal: short SMA crosses below long SMA
        elif short_sma[i] < long_sma[i] and short_sma[i-1] > long_sma[i-1] and buy:
            value = price[i]/value
            buy = False

        # change in value multiplied by equity to get new equity value
            equity = equity*value

    results[f"{short_name} < {long_name}"] = equity

# Print results
for pair, final_equity in results.items():
    print(f"{pair}: Final equity = {final_equity:.2f}")


# for i in range(len(sma_200)):
#     s200 = sma_200[i]
#     s150 = smas['SMA_150'][i]
#     s100 = smas['SMA_100'][i]
#     s50  = smas['SMA_50'][i]
#     s10  = smas['SMA_10'][i]

    # print(f"Index {i}:")
    # print(f"  SMA_200 > SMA_150: {s200 > s150} ({s200} > {s150})")
    # print(f"  SMA_200 > SMA_100: {s200 > s100} ({s200} > {s100})")
    # print(f"  SMA_200 > SMA_50 : {s200 > s50}  ({s200} > {s50})")
    # print(f"  SMA_200 > SMA_10 : {s200 > s10}  ({s200} > {s10})")
    # print()

# # Grid search combinations
# best_return = float('-inf')
# best_combo = ()

# for buy_sma, sell_sma in combinations(smas.keys(), 2):
#     buy_signal = price > smas[buy_sma]
#     sell_signal = price < smas[sell_sma]
#     # print(price)

#     position = False
#     entry_price = 0
#     total_return = 0

#     for i in range(len(price)):
#         if not position and buy_signal[i]:
#             entry_price = price[i]
#             position = True
#         elif position and sell_signal[i]:
#             total_return += price[i] - entry_price
#             position = False

#     if total_return > best_return:
#         best_return = total_return
#         best_combo = (buy_sma, sell_sma)

# print(f"Best SMA combo: Buy on {best_combo[0]}, Sell on {best_combo[1]}, Return: {best_return:.2f}")