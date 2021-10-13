from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import pandas as pd
import matplotlib.pyplot as plt
import swifter

#ticker =pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'].values
tdf = pd.read_csv('tickers.csv', names=['tickers'])
#ticker = set(tdf['tickers'].values.tolist() + ticker.tolist())
#print(len(ticker))

ticker = tdf['tickers'].values.tolist()

start_time = '2010-01-04'
_min, _max = 11.8, 52.62
tdf = pd.read_csv('data624_s04.csv')
tdf = tdf[:1622]
tdf['Var01'] = tdf['Var01'].fillna(tdf['Var01'].mean())

#df = pd.concat([pdr.get_data_yahoo(i, start=start_time).rename(columns={'Volume': i})[i] for i in ticker], axis=1).reset_index()
#df.to_csv('stock_values_2.csv', index=False)
df = pd.read_csv('stock_volume.csv')
df = df.drop(['Date'], axis=1).fillna(0).astype(int)
tdf['Var02'] = tdf['Var02'].astype(int)

sdf = df.rolling(window=tdf.shape[0]).apply(lambda x: sum(x - tdf['Var02'].values))
import pdb; pdb.set_trace()

sdf.dropna().to_csv('rolling_volume.csv', index=False)


