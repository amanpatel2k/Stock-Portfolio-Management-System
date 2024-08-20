from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import settings 

def Controllers(self, win, class_name):
    if(win == 'Main'):
        QApplication.closeAllWindows()
        self.w = class_name(QMainWindow)
        self.w.show()
        self.hide()
        settings.COUNT = 0
    elif(win == 'Window2'):
        self.w = class_name()
        self.w.show()
        self.hide()
        settings.COUNT = 0
    elif(win == 'rsi'):
        # self.w = rsiWindow(self.name)
        self.w = class_name(self.name)
        self.w.show()
    elif(win == 'sma'):
        self.w = class_name(self.name)
        self.w.show()

    

def Controller(self,win,stock,class_name):
    if(win == "ClickOnStock"):
        QApplication.closeAllWindows()
        self.w = class_name(stock)
        self.w.show()
        self.hide()
    elif(win == 'Main'):
        QApplication.closeAllWindows()
        # self.w = MainWindow(QMainWindow)
        self.w = class_name(stock)
        self.w.show()
        self.hide()
        settings.COUNT = 0
    else:
        self.w = win(stock)
        self.w.show()
        self.hide()
    