import yfinance as yf

data = yf.download('AAPL', '2020-03-20', '2021-03-26')

import matplotlib.pyplot as plt

data.Close.plot()

plt.show()











# print('Hello World!')