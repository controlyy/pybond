import pandas as pd

data = pd.read_csv('DIS.csv', index_col='Date')

data_inc_3percent = data[(data['Close']-data['Open'])/data['Open'] >= 0.03]

print(data_inc_3percent)
