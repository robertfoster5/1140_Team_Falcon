import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from tnc_main_ui import Ui_MainWindow
from tnc_controller import TrainController
from signals import signals


class TrainControllerMain(QObject):

    def __init__(self):
        super().__init__()

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.controller_thread = QThread()
        self.controller = TrainController()
        self.controller.moveToThread(self.controller_thread)
        self.controller_thread.start()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    c = TrainControllerMain()
    app.exec_()