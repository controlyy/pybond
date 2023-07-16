import pandas as pd
import utility
import cal_return_by_long_hold
import math

ticker = 'JPM'
stock_filename = 'data/' + ticker + '.csv'
dividend_filename = 'data/' + ticker + '_dividend.csv'

stock = pd.read_csv(stock_filename, index_col='Date')
dividend = pd.read_csv(dividend_filename, index_col='Date')

stock = utility.add_avg_price(stock)

return_rate = cal_return_by_long_hold.cal_return_by_long_hold('2016-10-03', stock, dividend)
sd = stock['Avg'].std()

years = utility.get_years_duration(stock)
year_return_rate = math.pow(return_rate,1/years) - 1
year_return_rate *= 100

print("Years: " + str(years))
print("Ticker: " + ticker)
print("Yearly return: " + str(year_return_rate))
print("SD: " + str(sd))
print("CoV: " + str(sd/year_return_rate))




