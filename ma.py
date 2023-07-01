import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('MSFT.csv', index_col='Date')

data['ma10'] = data['Open'].rolling(10).mean()
data['ma50'] = data['Open'].rolling(50).mean()

#print(data)
#data[['Close','ma10','ma50']].plot()

data = data.dropna()

#golden_cross_df = []
#death_cross_df = []
#
#for i in range(1,len(data)):
#    if (data['ma10'][i-1] > data['ma50'][i-1]) and (data['ma10'][i] <= data['ma50'][i]):
#        # death cross
#        death_cross_df.append(data.index[i])
#    elif (data['ma10'][i-1] < data['ma50'][i-1]) and  (data['ma10'][i] >= data['ma50'][i]):
#        # golden cross
#        golden_cross_df.append(data.index[i])

# TTTTFFFFFTTTT
#  FFFFTTTTTFFFF

sr1 = data['ma10'] < data['ma50']
sr2 = data['ma10'] >= data['ma50']

death_cross = data[sr1 & sr2.shift(1)].index
golden_cross = data[~(sr1 | sr2.shift(1))].index

#print(death_cross)
#print(golden_cross)

money = 10000
hold = 0

sr1 = pd.Series(1, index=golden_cross)
sr2 = pd.Series(0, index=death_cross)

sr = sr1.append(sr2).sort_index()

for i in range(0, len(sr)):
    price = data['Open'][sr.index[i]]
    if sr.iloc[i] == 1:
        # golden cross
        hold = money // price
        money -= hold*price
    else:
        # death cross
        money += hold*price
        hold = 0

price = data['Open'][-1]
total_money = hold * price + money

print(total_money)

#plt.show()
