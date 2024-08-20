from backtesting import Backtest
import pandas as pd
import yfinance as yf
import json
from backtesting_strategy import SmaCross, BasicRsiStrategy

class Strategys: #this is the strategy interface, it contains the method that the strategy class has
    def choose_a_strategy():  #We can give the start and end dates
        pass

class Rsi(Strategys): #Strat 1
    def choose_a_strategy():
        return BasicRsiStrategy
     

class Sma(Strategys): #strat 2
    def choose_a_strategy():
        return SmaCross

        
class Context(): #calls the strategy interface for the method, 
    #takes in parameter from client which is the strategy
    def __init__(self, strat):
        
        if strat == 'rsi':
            self.output = Rsi.choose_a_strategy() # 'RSI'.choose_a_strategy()
        else:
            self.output = Sma.choose_a_strategy()

    def output(self):
        return self.output
    

def _read_file(filename):
    from os.path import dirname, join

    return pd.read_csv(join(dirname(__file__), filename),
                       index_col=0, parse_dates=True, infer_datetime_format=True)

def strat(strat, stock):

    google = yf.download(stock, start='2019-01-01', end='2021-06-12', progress=False)
    google = google.drop(columns='Adj Close')
    google.to_csv('out.csv')
    current = _read_file('out.csv')
    choose_strategy = Context(strat).output
    bt = Backtest(current, choose_strategy, cash=1000000, commission=.002, exclusive_orders=True)
    stats = bt.run()
    # print(stats)

    data = {
        'Start': str(stats['Start']),
        'End': str(stats['End']),
        'Duration': str(stats['Duration']),   
        'Exposure Time [%]': str(stats['Exposure Time [%]']),  
        'Equity Final [$]': str(stats['Equity Final [$]']),  
        'Equity Peak [$]': str(stats['Equity Peak [$]']),
        'Return [%]': str(stats['Return [%]']),
        'Buy & Hold Return [%]': str(stats['Buy & Hold Return [%]']),  
        'Return (Ann.) [%]': str(stats['Return (Ann.) [%]']),  
        'Volatility (Ann.) [%]': str(stats['Volatility (Ann.) [%]']),
        'Sharpe Ratio': str(stats['Sharpe Ratio']), 
        'Sortino Ratio': str(stats['Sortino Ratio']),
        'Calmar Ratio': str(stats['Calmar Ratio']), 
        'Max. Drawdown [%]': str(stats['Max. Drawdown [%]']),
        'Avg. Drawdown [%]': str(stats['Avg. Drawdown [%]']),
        'Max. Drawdown Duration': str(stats['Max. Drawdown Duration']),
        'Avg. Drawdown Duration': str(stats['Avg. Drawdown Duration']),
        '# Trades': str(stats['# Trades']),
        'Win Rate [%]': str(stats['Win Rate [%]']),
        'Best Trade [%]': str(stats['Best Trade [%]']),
        'Worst Trade [%]': str(stats['Worst Trade [%]']),
        'Avg. Trade [%]': str(stats['Avg. Trade [%]']),
        'Max. Trade Duration': str(stats['Max. Trade Duration']),
        'Avg. Trade Duration': str(stats['Avg. Trade Duration']),
        'Profit Factor': str(stats['Profit Factor']),
        'Expectancy [%]': str(stats['Expectancy [%]']), 
        'SQN': str(stats['SQN']), 
    }
    
    return data

# main('Rsi')
