import yfinance as yf

ticker = 'JPM'

data = yf.download(ticker, start="2015-01-01")

#print(data)

data.to_csv(ticker + '.csv')

company = yf.Ticker(ticker)
company.dividends.to_csv(ticker + '_dividend.csv')
