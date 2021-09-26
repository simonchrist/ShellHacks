import datetime
import plotly.offline as py
import plotly.graph_objs as go
import pandas_datareader as web
import matplotlib.pyplot as plt

start = datetime.datetime(2014, 1, 1)
end = datetime.datetime(2025, 1, 1)

BTC = web.DataReader('BTC-USD', 'yahoo', start, end)
ETH = web.DataReader('ETH-USD', 'yahoo', start, end)
DOGE = web.DataReader('DOGE-USD', 'yahoo', start, end)
TETHER = web.DataReader('USDT-USD', 'yahoo', start, end)

trace = go.Ohlc(
    x=BTC.index[:],
    open=BTC['Open'],
    high=BTC['High'],
    low=BTC['Low'],
    close=BTC['Close'],
    name='BTC',
    increasing=dict(line=dict(color='green')),
    decreasing=dict(line=dict(color='red')),
)

trace2 = go.Ohlc(
    x=ETH.index[:],
    open=ETH['Open'],
    high=ETH['High'],
    low=ETH['Low'],
    close=ETH['Close'],
    name='ETH',
    increasing=dict(line=dict(color='black')),
    decreasing=dict(line=dict(color='red')),
)

trace3 = go.Ohlc(
    x=DOGE.index[:],
    open=DOGE['Open'],
    high=DOGE['High'],
    low=DOGE['Low'],
    close=DOGE['Close'],
    name='DOGE',
    increasing=dict(line=dict(color='purple')),
    decreasing=dict(line=dict(color='pink')),
)

trace4 = go.Ohlc(
    x=TETHER.index[:],
    open=TETHER['Open'],
    high=TETHER['High'],
    low=TETHER['Low'],
    close=TETHER['Close'],
    name='TETHER',
    increasing=dict(line=dict(color='blue')),
    decreasing=dict(line=dict(color='yellow')),
)

data = [trace]
layout = {
    'title': 'BTC - Bitcoin',
    'xaxis': {'title': 'Timeframe'},
    'yaxis': {'title': 'Price'}
}

data2 = [trace2]
layout = {
    'title': 'ETH - ETHEREUM',
    'xaxis': {'title': 'Timeframe'},
    'yaxis': {'title': 'Price'}
}

data3 = [trace3]
layout = {
    'title': 'DOGE - DOGECOIN',
    'xaxis': {'title': 'Timeframe'},
    'yaxis': {'title': 'Price'}
}

data4 = [trace4]
layout = {
    'title': 'USDT - TETHER',
    'xaxis': {'title': 'Timeframe'},
    'yaxis': {'title': 'Price'}
}

fig = dict(data=data, layout=layout)
fig2 = dict(data=data2, layout=layout)
fig3 = dict(data=data3, layout=layout)
fig4 = dict(data=data4, layout=layout)

py.plot(fig, filename='crypto.html')
py.plot(fig2, filename='crypto1.html')
py.plot(fig3, filename='crypto2.html')
py.plot(fig4, filename='crypto3.html')
