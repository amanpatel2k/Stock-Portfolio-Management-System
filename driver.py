import view
import sys

app = view.QApplication(sys.argv)
w = view.MainWindow()
w.show()
sys.exit(app.exec_())