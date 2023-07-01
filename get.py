import yfinance as yf

data = yf.download("MSFT", start="2018-01-01")

print(data)

data.to_csv('MSFT.csv')