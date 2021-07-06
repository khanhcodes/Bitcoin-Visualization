import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.offline import plot
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick_ohlc
import plotly.io as plt_io #get the theme settings

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id = 'bitcoin', vs_currency = 'usd', days = 30)
pd.DataFrame.from_dict(bitcoin_data)


bitcoin_price_data = bitcoin_data['prices']
data = pd.DataFrame(data = bitcoin_price_data,columns = ['Time Stamp', 'Prices'])
data['date'] = data['Time Stamp'].apply(lambda unit: datetime.date.fromtimestamp(unit/1000.0))
candlestick_data = data.groupby(by = ['date'], as_index = False ).agg({'Prices': ['min', 'max', 'first', 'last']})

figure = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Prices']['first'], 
                high=candlestick_data['Prices']['max'],
                low=candlestick_data['Prices']['min'], 
                close=candlestick_data['Prices']['last'])])

figure.update_layout(xaxis_rangeslider_visible=False)

figure.update_layout(
    title='Bitcoin Price Chart',
    yaxis_title='USD')

plt_io.templates["custom_dark"] = plt_io.templates["plotly_dark"]

# set the paper_bgcolor and the plot_bgcolor to a new color
plt_io.templates["custom_dark"]['layout']['paper_bgcolor'] = '#30404D'
plt_io.templates["custom_dark"]['layout']['plot_bgcolor'] = '#30404D'

# change gridline colors 
plt_io.templates['custom_dark']['layout']['yaxis']['gridcolor'] = '#4f687d'
plt_io.templates['custom_dark']['layout']['xaxis']['gridcolor'] = '#4f687d'

figure.layout.template = 'custom_dark'
figure.show()




