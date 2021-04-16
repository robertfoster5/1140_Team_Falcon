import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from time_ui import Ui_Time
from t_time import timing
from signals import signals

class TimeMain(QObject):
    def __init__(self):
        print("time running")
        super().__init__()

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Time()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.time_thread = QThread()
        self.time = timing()
        self.time.moveToThread(self.time_thread)
        self.time_thread.started.connect(self.time.start)
        self.time_thread.start()

        self.ui.label_5.setText(" " + str(1))

        signals.time.connect(self.update_gui)
        self.ui.lineEdit.editingFinished.connect(self.set_multiplier)


    def update_gui(self,s,m,h,t):
        self.ui.label_3.setText(" " + str(h) + ":" + str(m) + ":" + str(s))

    def set_multiplier(self):
        mult = self.ui.lineEdit.text()
        self.ui.label_5.setText(" " + mult)
        signals.time_multiplier.emit(int(mult))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    c = TimeMain()
    app.exec_()