from backtesting import Backtest, Strategy, _stats
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG
from numpy import choose
import yfinance as yf
import pandas as pd;
from pandas_ta import rsi

class SmaCross(Strategy):
    n1 = 50
    n2 = 100
    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)
    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()

class BasicRsiStrategy(Strategy):
    def init(self):
        self.rsi = self.I(rsi, self.data.df.Close, length=14)
    def next(self):
        today = self.rsi[-1]
        yesterday = self.rsi[-2]
        if yesterday > 30 and today < 30 and not self.position.is_long:
            self.buy()
        elif yesterday < 70 and today > 70 and self.position.size > 0:
            self.position.close()