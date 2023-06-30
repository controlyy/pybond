import pandas as pd

data = pd.read_csv('DIS.csv')

data_inc_3percent = pd.DataFrame()

for index, row in data.iterrows():
    diff = row["Close"] - row["Open"]
    increase_percent = diff/row["Close"]
    if  increase_percent > 0.03:
        new_row = row
        new_row["increase_percentage"] = increase_percent
        data_inc_3percent = data_inc_3percent.append(new_row)

data_inc_3percent = data_inc_3percent.set_index('Date')
print(data_inc_3percent)
