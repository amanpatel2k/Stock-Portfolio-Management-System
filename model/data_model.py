import yfinance as yf 
import requests
import json
import os.path
import pandas as pd

class Adaptee_URL():
    def __init__(self, stock):
        self.stock = stock
    
    def get_historical_data(self):
        return self.stock_detail_url()

    def stock_values(self, trait):
        if(os.path.isfile('stock_data.json')):
            with open('stock_data.json', 'r') as f:
                data = json.load(f)
            return str(data['quoteResponse']['result'][0][trait])
        else:
            pass

    def grab_json(self):
        URL = ('https://query1.finance.yahoo.com/v7/finance/quote?symbols=' + self.stock)
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

        result = requests.get(URL, headers=headers)
        temp = result.content.decode()
    
        text_file = open("stock_data.json", "w", encoding='utf-8')
        n = text_file.write(temp)
        text_file.close()

    def stock_detail_url(self):
        stock_info = self.grab_json()
        data = {
            'stock_symbol': self.stock_values(trait='symbol'),
            'stock_short': self.stock_values(trait='shortName'),
            'stock_long': self.stock_values(trait='longName'),   
            'market_ask': self.stock_values(trait='ask'),
            'market_close': self.stock_values(trait='regularMarketPreviousClose'),
            'market_open': self.stock_values(trait='regularMarketOpen'),
            'market_price': self.stock_values(trait='regularMarketPrice'),
            'market_volume': self.stock_values(trait='regularMarketVolume'),
            'Analyst_rec': self.stock_values(trait='averageAnalystRating'),
            'market_EPS': self.stock_values(trait='epsTrailingTwelveMonths'),
            'market_PE': self.stock_values(trait='trailingPE'),
            'market_bid': self.stock_values(trait='bid'),
            'previous_close_price': self.stock_values(trait='regularMarketPreviousClose')
        }

        with open('stock_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    
        li = []
        for index in data:
            li.append(data[index])
        return li

class Adaptee_YAHOO(): # decorator impleme
    def __init__(self, stock):
        self.stock = stock
    
    def get_historical_data(self):
        return self.stock_data()

    def stock_data(self):  
        stock_info = yf.Ticker(self.stock).info

        # Implement Decorator Start
        stock_info['Close'] = stock_info['previousClose']
        stock_info.pop('previousClose')
        # Implement Decorator End 

        data = {
            'stock_symbol': str(stock_info.get('symbol', 'N/A')),
            'stock_short': str(stock_info.get('shortName', 'N/A')),
            'stock_long': str(stock_info.get('longName', 'N/A')),
            'market_ask': str(stock_info.get('ask', 'N/A')),
            'market_close': str(stock_info.get('Close', 'N/A')),
            'market_open': str(stock_info.get('regularMarketOpen', 'N/A')),
            'market_price': str(stock_info.get('regularMarketPrice', 'N/A')),
            'market_volume': str(stock_info.get('volume', 'N/A')),
            'Analyst_rec': str(stock_info.get('recommendationKey', 'N/A')),
            'market_EPS': str(stock_info.get('trailingEps', 'N/A')),
            'market_PE': str(stock_info.get('trailingPE', 'N/A')),
            'market_bid': str(stock_info.get('bid', 'N/A')),
            'previous_close_price': str(stock_info.get('regularMarketPreviousClose', 'N/A'))
        }
        
        with open('stock_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        li = []
        for index in data:
            li.append(data[index])
        return li

class Adapter():
    def __init__(self, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.__dict__.update(adapted_methods)
 
def client_code(stock, data_source="Adaptee_YAHOO"):
    
    if data_source == "Adaptee_YAHOO":
        hd = Adaptee_YAHOO(stock)
    else:
        hd = Adaptee_URL(stock)
    
    data_adapter = Adapter(historical_data=hd.get_historical_data)
    hdata = data_adapter.historical_data()
    return hdata

def return_json(file):
    json_data = []
    with open(file) as json_file:
        json_data = json.load(json_file)
    return json_data
