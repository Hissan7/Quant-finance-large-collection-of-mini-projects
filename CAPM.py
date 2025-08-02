import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import scipy.optimize as optimization


class CAPM:

    def __init__(self, stocks, start_date, end_date):
        self.data = None
        self.stocks = stocks
        self.start_date = start_date
        self.end_date = end_date

    def download_data(self):  #get the data from yahoo finance

        data = {}
        for stock in self.stocks:
            ticker = yf.download(stock, self.start_date, self.end_date,auto_adjust=False)
            data[stock] = ticker['Adj Close']

        return pd.DataFrame(data)

    def initialise(self):
        stock_data = self.download_data()
        stock_data = stock_data.resample('M').last()
        print(stock_data)


if __name__ == '__main__':
    capm = CAPM(['IBM', '^GSPC'], '2010-01-01', '2017-01-01')
    capm.initialise()
