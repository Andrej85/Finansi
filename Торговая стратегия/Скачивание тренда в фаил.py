import yfinance as yf
import pandas as pd

stock = yf.Ticker("IBM")


# get historical market data
hist = stock.history(period = "730d", interval="1d")
hist = pd.DataFrame(hist)


hist.index = hist.index.tz_localize(None)
hist.to_excel(excel_writer= "IBM_1d.xlsx")
print('Готово')