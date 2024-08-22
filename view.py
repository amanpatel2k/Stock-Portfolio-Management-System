import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
from model.data_model import return_json, client_code
from model.strategy_pattern import strat
from controller import Controller, Controllers
import settings


class ClickOnStock(QMainWindow):
    def __init__(self,name):
        super().__init__()
        font_size = 45

        json_data = return_json('stock_list.json')
        data_set = client_code(json_data[name])
        self.name = name
        self.setGeometry(600, 100, 800, 600)
        self.controls = QWidget()  
        self.controlsLayout = QVBoxLayout() 

        self.setWindowTitle("Stats Page")
        self.pushButton = QPushButton("Home", self)
        self.pushButton.move(690, 2)

        self.back = QPushButton("Back Testing", self)
        self.back.move(15, 2)
         
        self.pushButton.clicked.connect(lambda:Controllers(self,'Main', MainWindow))  
        self.back.clicked.connect(self.back_test_btn)
       
        self.label_1 = QLabel('Stock Symbol:  '+ data_set[0], self)
        self.label_2 = QLabel('Stock Name:  ' + data_set[1], self)
        self.label_3 = QLabel('Volume:  ' + data_set[7], self)
        self.label_4 = QLabel('Analyst Recommendation:  ' + data_set[8], self)
        self.label_5 = QLabel('Market EPS:  ' + data_set[9], self)
        self.label_6 = QLabel('Market Open:  ' + data_set[5], self)
        self.label_7 = QLabel('Market Close:  ' + data_set[4], self)
        self.label_8 = QLabel('Market Bid:  ' + data_set[11], self)
        self.label_9 = QLabel('Market Ask:  ' + data_set[3], self)
        self.label_10 = QLabel('Market PE Ratio:  ' + str(round(float(data_set[10]),2)), self)
        
        self.label_1.move(7, (20+(50*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_1.setFont(QFont('Gill Sans', font_size))
        self.label_1.resize(1100, 80)
        self.label_2.move(7, (20+(50*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_2.setFont(QFont('Gill Sans', font_size))
        self.label_2.resize(1100, 80)
        self.label_3.move(7, (20+(50*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_3.setFont(QFont('Gill Sans', font_size))
        self.label_3.resize(1100, 80)
        self.label_4.move(7, (20+(50*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_4.setFont(QFont('Gill Sans', font_size))
        self.label_4.resize(1100, 80)
        self.label_5.move(7, (20+(50*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_5.setFont(QFont('Gill Sans', font_size))
        self.label_5.resize(1100, 80)
        self.label_6.move(7, (20+(50*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_6.setFont(QFont('Gill Sans', font_size))
        self.label_6.resize(1100, 80)
        self.label_7.move(7, (20+(50*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_7.setFont(QFont('Gill Sans', font_size))
        self.label_7.resize(1100, 80)
        self.label_8.move(7, (20+(50*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_8.setFont(QFont('Gill Sans', font_size))
        self.label_8.resize(1100, 80)
        self.label_9.move(7, (20+(50*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_9.setFont(QFont('Gill Sans', font_size))
        self.label_9.resize(1100, 80)
        self.label_10.move(7, (20+(50*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_10.setFont(QFont('Gill Sans', font_size))
        self.label_10.resize(1100, 80)
        settings.COUNT = 0

    def back_test_btn(self):
        messageBox = QMessageBox(self)
        messageBox.setWindowTitle("Back Testing Method")
        messageBox.setIcon(QMessageBox.Question)
        messageBox.setText("Back Testing Method")
        messageBox.setInformativeText("Which back testing methord would you like to test?")
        buttonoptionA = messageBox.addButton("SMA Crossover", QMessageBox.YesRole)    
        buttonoptionB = messageBox.addButton("RSI", QMessageBox.AcceptRole)  
        messageBox.setDefaultButton(buttonoptionA)
        messageBox.exec_()
        if messageBox.clickedButton() == buttonoptionA:
            Controllers(self,"sma", smaWindow)

        elif messageBox.clickedButton() == buttonoptionB:
            Controllers(self,"rsi", rsiWindow)

class smaWindow(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.sma = 'sma'
        font_size = 25
        offset = 0
        temp = font_size + 5
        self.setGeometry(600, 100, 800, 600)
        self.controls = QWidget()
        self.controlsLayout = QVBoxLayout()

        self.setWindowTitle(name + " with SMA back test")
        self.pushButton = QPushButton("Home", self)
        self.pushButton.move(690, 2)
        self.pushButton.clicked.connect(lambda:Controllers(self,'Main', MainWindow)) 
        json_data = []
        json_data = return_json('stock_list.json')
        ret = []
        for names in json_data:
            ret.append(json_data[names])
        
        data = strat(self.sma, json_data[name])
        self.label_1 = QLabel('Start:                   '+ data['Start'], self)
        self.label_2 = QLabel('End:                     ' + data['End'], self)
        self.label_3 = QLabel('Duration:                ' + data['Duration'], self)
        self.label_4 = QLabel('Exposure Time [%]:       ' + data['Exposure Time [%]'], self)
        self.label_5 = QLabel('Equity Final [$]:        ' + data['Equity Final [$]'], self)
        self.label_6 = QLabel('Equity Peak [$]:         ' + data['Equity Peak [$]'], self)
        self.label_7 = QLabel('Return [%]:              ' + data['Return [%]'], self)
        self.label_8 = QLabel('Buy & Hold Return [%]:   ' + data['Buy & Hold Return [%]'], self)
        self.label_9 = QLabel('Return (Ann.) [%]:       ' + data['Return (Ann.) [%]'], self)
        self.label_10 = QLabel('Volatility (Ann.) [%]:  ' + data['Volatility (Ann.) [%]'], self)
        self.label_11 = QLabel('Sharpe Ratio :          ' + data['Sharpe Ratio'], self)
        self.label_12 = QLabel('Sortino Ratio:          ' + data['Sortino Ratio'], self)
        self.label_13 = QLabel('Calmar Ratio:           ' + data['Calmar Ratio'], self)
        self.label_14 = QLabel('Max. Drawdown [%]:      ' + data['Max. Drawdown [%]'], self)
        self.label_15 = QLabel('Avg. Drawdown [%]:      ' + data['Avg. Drawdown [%]'], self)
        self.label_16 = QLabel('Max. Drawdown Duration: ' + data['Max. Drawdown Duration'], self)
        self.label_17 = QLabel('Avg. Drawdown Duration: ' + data['Avg. Drawdown Duration'], self)
        self.label_18 = QLabel('Win Rate [%]:           ' + data['Win Rate [%]'], self)
        self.label_19 = QLabel('Best Trade [%]:         ' + data['Best Trade [%]'], self)
        self.label_20 = QLabel('Worst Trade [%]:        ' + data['Worst Trade [%]'], self)
        self.label_21 = QLabel('Avg. Trade [%]:         ' + data['Volatility (Ann.) [%]'], self)
        self.label_22 = QLabel('Max. Trade Duration:    ' + data['Max. Trade Duration'], self)
        self.label_23 = QLabel('Avg. Trade Duration:    ' + data['Avg. Trade Duration'], self)
        self.label_24 = QLabel('Profit Factor:          ' + data['Profit Factor'], self)
        self.label_25 = QLabel('Expectancy [%]:         ' + data['Expectancy [%]'], self)
        self.label_26 = QLabel('SQN:                    ' + data['SQN'], self)

        self.label_1.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_1.setFont(QFont('Gill Sans', font_size))
        self.label_1.resize(1100, 80)
        #
        self.label_2.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_2.setFont(QFont('Gill Sans', font_size))
        self.label_2.resize(1100, 80)
        #
        self.label_3.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_3.setFont(QFont('Gill Sans', font_size))
        self.label_3.resize(1100, 80)
        #
        self.label_4.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_4.setFont(QFont('Gill Sans', font_size))
        self.label_4.resize(1100, 80)
        #
        self.label_5.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_5.setFont(QFont('Gill Sans', font_size))
        self.label_5.resize(1100, 80)
        #
        self.label_6.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_6.setFont(QFont('Gill Sans', font_size))
        self.label_6.resize(1100, 80)
        #
        self.label_7.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_7.setFont(QFont('Gill Sans', font_size))
        self.label_7.resize(1100, 80)
        #
        self.label_8.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_8.setFont(QFont('Gill Sans', font_size))
        self.label_8.resize(1100, 80)
        #
        self.label_9.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_9.setFont(QFont('Gill Sans', font_size))
        self.label_9.resize(1100, 80)
        #
        self.label_10.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_10.setFont(QFont('Gill Sans', font_size))
        self.label_10.resize(1100, 80)
        #
        self.label_11.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_11.setFont(QFont('Gill Sans', font_size))
        self.label_11.resize(1100, 80)
        #
        self.label_12.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_12.setFont(QFont('Gill Sans', font_size))
        self.label_12.resize(1100, 80)
        #
        self.label_13.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_13.setFont(QFont('Gill Sans', font_size))
        self.label_13.resize(1100, 80)
        #
        self.label_14.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_14.setFont(QFont('Gill Sans', font_size))
        self.label_14.resize(1100, 80)
        #
        self.label_15.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_15.setFont(QFont('Gill Sans', font_size))
        self.label_15.resize(1100, 80)
        #
        self.label_16.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_16.setFont(QFont('Gill Sans', font_size))
        self.label_16.resize(1100, 80)
        #
        self.label_17.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_17.setFont(QFont('Gill Sans', font_size))
        self.label_17.resize(1100, 80)
        #
        self.label_18.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_18.setFont(QFont('Gill Sans', font_size))
        self.label_18.resize(1100, 80)
        #
        self.label_19.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_19.setFont(QFont('Gill Sans', font_size))
        self.label_19.resize(1100, 80)
        #
        self.label_20.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_20.setFont(QFont('Gill Sans', font_size))
        self.label_20.resize(1100, 80)
        #
        self.label_21.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_21.setFont(QFont('Gill Sans', font_size))
        self.label_21.resize(1100, 80)
        #
        self.label_22.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_22.setFont(QFont('Gill Sans', font_size))
        self.label_22.resize(1100, 80)
        #
        self.label_23.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_23.setFont(QFont('Gill Sans', font_size))
        self.label_23.resize(1100, 80)
        #
        self.label_24.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_24.setFont(QFont('Gill Sans', font_size))
        self.label_24.resize(1100, 80)
        #
        self.label_25.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_25.setFont(QFont('Gill Sans', font_size))
        self.label_25.resize(1100, 80)
        #
        self.label_26.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_26.setFont(QFont('Gill Sans', font_size))
        self.label_26.resize(1100, 80)
        settings.COUNT = 0

class rsiWindow(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.rsi = 'rsi'
        font_size = 25
        offset = 0
        temp = font_size + 5
        self.setGeometry(600, 100, 800, 600)
        self.controls = QWidget()  # Controls container widget.
        self.controlsLayout = QVBoxLayout()   # Controls container layout.

        self.setWindowTitle(name + " with RSI back test")
        self.pushButton = QPushButton("Home", self)
        self.pushButton.move(690, 2)
        self.pushButton.clicked.connect(lambda:Controllers(self,'Main', MainWindow))      
        json_data = []
        json_data = return_json('stock_list.json')
        ret = []
        for names in json_data:
            ret.append(json_data[names])
        
        data = strat(self.rsi, json_data[name])
        self.label_1 = QLabel('Start:                   '+ data['Start'], self)
        self.label_2 = QLabel('End:                     ' + data['End'], self)
        self.label_3 = QLabel('Duration:                ' + data['Duration'], self)
        self.label_4 = QLabel('Exposure Time [%]:       ' + data['Exposure Time [%]'], self)
        self.label_5 = QLabel('Equity Final [$]:        ' + data['Equity Final [$]'], self)
        self.label_6 = QLabel('Equity Peak [$]:         ' + data['Equity Peak [$]'], self)
        self.label_7 = QLabel('Return [%]:              ' + data['Return [%]'], self)
        self.label_8 = QLabel('Buy & Hold Return [%]:   ' + data['Buy & Hold Return [%]'], self)
        self.label_9 = QLabel('Return (Ann.) [%]:       ' + data['Return (Ann.) [%]'], self)
        self.label_10 = QLabel('Volatility (Ann.) [%]:  ' + data['Volatility (Ann.) [%]'], self)
        self.label_11 = QLabel('Sharpe Ratio :          ' + data['Sharpe Ratio'], self)
        self.label_12 = QLabel('Sortino Ratio:          ' + data['Sortino Ratio'], self)
        self.label_13 = QLabel('Calmar Ratio:           ' + data['Calmar Ratio'], self)
        self.label_14 = QLabel('Max. Drawdown [%]:      ' + data['Max. Drawdown [%]'], self)
        self.label_15 = QLabel('Avg. Drawdown [%]:      ' + data['Avg. Drawdown [%]'], self)
        self.label_16 = QLabel('Max. Drawdown Duration: ' + data['Max. Drawdown Duration'], self)
        self.label_17 = QLabel('Avg. Drawdown Duration: ' + data['Avg. Drawdown Duration'], self)
        self.label_18 = QLabel('Win Rate [%]:           ' + data['Win Rate [%]'], self)
        self.label_19 = QLabel('Best Trade [%]:         ' + data['Best Trade [%]'], self)
        self.label_20 = QLabel('Worst Trade [%]:        ' + data['Worst Trade [%]'], self)
        self.label_21 = QLabel('Avg. Trade [%]:         ' + data['Volatility (Ann.) [%]'], self)
        self.label_22 = QLabel('Max. Trade Duration:    ' + data['Max. Trade Duration'], self)
        self.label_23 = QLabel('Avg. Trade Duration:    ' + data['Avg. Trade Duration'], self)
        self.label_24 = QLabel('Profit Factor:          ' + data['Profit Factor'], self)
        self.label_25 = QLabel('Expectancy [%]:         ' + data['Expectancy [%]'], self)
        self.label_26 = QLabel('SQN:                    ' + data['SQN'], self)

        # moving position
        self.label_1.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_1.setFont(QFont('Gill Sans', font_size))
        self.label_1.resize(1100, 80)
        #
        self.label_2.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_2.setFont(QFont('Gill Sans', font_size))
        self.label_2.resize(1100, 80)
        #
        self.label_3.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_3.setFont(QFont('Gill Sans', font_size))
        self.label_3.resize(1100, 80)
        #
        self.label_4.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_4.setFont(QFont('Gill Sans', font_size))
        self.label_4.resize(1100, 80)
        #
        self.label_5.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_5.setFont(QFont('Gill Sans', font_size))
        self.label_5.resize(1100, 80)
        #
        self.label_6.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_6.setFont(QFont('Gill Sans', font_size))
        self.label_6.resize(1100, 80)
        #
        self.label_7.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_7.setFont(QFont('Gill Sans', font_size))
        self.label_7.resize(1100, 80)        
        #
        self.label_8.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_8.setFont(QFont('Gill Sans', font_size))
        self.label_8.resize(1100, 80)
        #
        self.label_9.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_9.setFont(QFont('Gill Sans', font_size))
        self.label_9.resize(1100, 80)
        #
        self.label_10.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_10.setFont(QFont('Gill Sans', font_size))
        self.label_10.resize(1100, 80)
        #
        self.label_11.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_11.setFont(QFont('Gill Sans', font_size))
        self.label_11.resize(1100, 80)
        #
        self.label_12.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_12.setFont(QFont('Gill Sans', font_size))
        self.label_12.resize(1100, 80)
        #
        self.label_13.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_13.setFont(QFont('Gill Sans', font_size))
        self.label_13.resize(1100, 80)
        #
        self.label_14.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_14.setFont(QFont('Gill Sans', font_size))
        self.label_14.resize(1100, 80)
        #
        self.label_15.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_15.setFont(QFont('Gill Sans', font_size))
        self.label_15.resize(1100, 80)
        #
        self.label_16.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_16.setFont(QFont('Gill Sans', font_size))
        self.label_16.resize(1100, 80)
        #
        self.label_17.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_17.setFont(QFont('Gill Sans', font_size))
        self.label_17.resize(1100, 80)
        #
        self.label_18.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_18.setFont(QFont('Gill Sans', font_size))
        self.label_18.resize(1100, 80)
        #
        self.label_19.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_19.setFont(QFont('Gill Sans', font_size))
        self.label_19.resize(1100, 80)
        #
        self.label_20.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_20.setFont(QFont('Gill Sans', font_size))
        self.label_20.resize(1100, 80)
        #
        self.label_21.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_21.setFont(QFont('Gill Sans', font_size))
        self.label_21.resize(1100, 80)
        #
        self.label_22.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_22.setFont(QFont('Gill Sans', font_size))
        self.label_22.resize(1100, 80)
        #
        self.label_23.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_23.setFont(QFont('Gill Sans', font_size))
        self.label_23.resize(1100, 80)
        #
        self.label_24.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_24.setFont(QFont('Gill Sans', font_size))
        self.label_24.resize(1100, 80)
        #
        self.label_25.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_25.setFont(QFont('Gill Sans', font_size))
        self.label_25.resize(1100, 80)
        #
        self.label_26.move(7, (offset+(temp*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_26.setFont(QFont('Gill Sans', font_size))
        self.label_26.resize(1100, 80)
        #
        settings.COUNT = 0

class Window2(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 100, 800, 600)
        self.controls = QWidget() 
        self.controlsLayout = QVBoxLayout() 

        self.setWindowTitle("Portfolio Window")
        self.pushButton = QPushButton("Home", self)
        self.pushButton.move(690, 2)
        self.pushButton.clicked.connect(lambda:Controllers(self,"Main", MainWindow))
        
        json_data = []
        json_data = return_json('stock_list.json')
        ret = []
        for names in json_data:
            ret.append(json_data[names])
        for names in json_data:
            self.data(names,json_data,ret)

    def create_label(self,name):
        # global COUNT  
        self.label_1 = QLabel(name, self)
        self.label_1.move(7, (20+(50*settings.COUNT)))            
        settings.COUNT = settings.COUNT + 1
        self.label_1.setFont(QFont('Gill Sans', 45))
        self.label_1.resize(1100, 80)
            
    def data(self,names,jet,ret):
        if names in settings.buy:
            self.print_stocks(names)
    
    def print_stocks(self,name):
        # global COUNT  
        self.label_1 = QLabel(name, self)
        self.label_1.move(7, (20+(50*settings.COUNT)))
        settings.COUNT = settings.COUNT + 1
        self.label_1.setFont(QFont('Gill Sans', 45))
        self.label_1.resize(1100, 80)
    
class OnOffWidget(QWidget):
    def __init__(self, name,i):
        super(OnOffWidget, self).__init__()

        self.name = name
        if i == 0: self.is_on = False
        else: self.is_on = True

        self.lbl = QPushButton(self.name, self)
        self.btn_on = QPushButton("Add to Portfolio")
        self.btn_off = QPushButton("Not in Portfolio")

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.lbl)
        self.hbox.addWidget(self.btn_on)
        self.hbox.addWidget(self.btn_off)

        self.btn_on.clicked.connect(self.on)
        self.btn_off.clicked.connect(self.off)
        self.lbl.clicked.connect(lambda:Controller(self,"ClickOnStock",self.name, ClickOnStock))

        self.setLayout(self.hbox)
        self.update_button_state()
    def stats(self):      
        QApplication.closeAllWindows()
        self.w = ClickOnStock(self.name)
        self.w.show()
        self.hide()
    def show(self):
        for w in [self, self.lbl, self.btn_on, self.btn_off]:
            w.setVisible(True)

    def hide(self):
        for w in [self, self.lbl, self.btn_on, self.btn_off]:
            w.setVisible(False)
    def off(self):
        self.is_on = False
        if self.name in settings.buy:
            settings.buy.remove(self.name)
        self.update_button_state()
        print("\n\nUpdated BUY list: ", settings.buy)

    def on(self):
        self.is_on = True
        if self.name not in settings.buy:
            settings.buy.append(self.name)
        self.update_button_state()
        print("\n\nUpdated BUY list: ", settings.buy)

    def update_button_state(self):
        if self.is_on == True:
            self.btn_on.setStyleSheet("background-color: #4CAF50; color: #fff;")
            self.btn_off.setStyleSheet("background-color: none; color: none;")
        else:
            self.btn_on.setStyleSheet("background-color: none; color: none;")
            self.btn_off.setStyleSheet("background-color: #D32F2F; color: #fff;")
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.controls = QWidget()
        self.controlsLayout = QVBoxLayout()
        self.widgets = []
        json_data = []
        json_data = return_json('stock_list.json')
        ret = []
        for names in json_data:
            ret.append(json_data[names])
        if(settings.on_stock == False):
            for name in json_data:
                if name in settings.buy:item = OnOffWidget(name,1)
                else: item =OnOffWidget(name,0)
                self.controlsLayout.addWidget(item)
                self.widgets.append(item)
        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.controlsLayout.addItem(spacer)
        self.controls.setLayout(self.controlsLayout)

        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.controls)

        self.searchbar = QLineEdit()
        self.searchbar.move(250,250)
        self.searchbar.textChanged.connect(self.update_display)

        self.completer = QCompleter(json_data)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.searchbar.setCompleter(self.completer)

        container = QWidget()
        containerLayout = QVBoxLayout()
        containerLayout.addWidget(self.searchbar)
        
        containerLayout.addWidget(self.scroll)

        container.setLayout(containerLayout)
        self.setCentralWidget(container)

        self.setGeometry(600, 100, 800, 600)
        self.setWindowTitle('CPSC-362 Stock Checker')
        
        self.pushButton = QPushButton("Portfolio", self)
        self.pushButton.move(690, 10)      
        self.pushButton.clicked.connect(lambda:Controllers(self,"Window2", Window2))

    def update_display(self, text):
        for widget in self.widgets:
            if text.lower() in widget.name.lower():
                widget.show()
            else:
                widget.hide()
    def location_on_the_screen(self):
        topLeftPoint = QApplication.desktop().availableGeometry().topLeft()
        self.move(topLeftPoint)
