import pandas as pd

data = pd.read_csv('DIS.csv')

data_dec_2percent = pd.DataFrame()

for index, row in data.iterrows():
    if index == 0:
        continue

    last_close_price = data.iloc[index-1]["Close"]
    open_price = row["Open"]
    diff = last_close_price - open_price
    dec_percent = diff/last_close_price
    if  dec_percent > 0.02:
        #new_row = pd.DataFrame({'Date':row["Date"], 'last_close':last_close_price, 'open_price':open_price, 'diff_percentage':dec_percent})
        new_row = pd.Series([row["Date"],last_close_price, open_price, dec_percent],index=['Date','last_close','open_price','diff_percentage'])
        data_dec_2percent = data_dec_2percent.append(new_row, ignore_index = True)

data_dec_2percent = data_dec_2percent.set_index('Date')
print(data_dec_2percent)
