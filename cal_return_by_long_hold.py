import pandas as pd

def cal_return_by_long_hold(buy_date, stock_data, dividend_data):
    # buy
    buy_price = stock_data.loc[buy_date]['Open']
    current_price = stock_data.iloc[-1]['Open']
    total_dividends = 0

    for index, row in dividend_data.iterrows():
        if (buy_date < index):
            #print("Date: " + str(index))
            #print("Dividend: " + str(row['Dividends']))
            total_dividends += row['Dividends']
    
    # print(total_dividends)

    total_value = current_price + total_dividends

    return total_value / buy_price




if __name__ == "__main__":
    stock_data = pd.read_csv('data/JNJ.csv', index_col='Date')
    dividend_data = pd.read_csv('data/JNJ_dividend.csv', index_col='Date')

    return_rate = cal_return_by_long_hold('2016-10-03', stock_data, dividend_data)

    print("Return rate: " + str(return_rate))
    #print("price: " + str(stock_data.loc['2015-01-02']['Open']))
