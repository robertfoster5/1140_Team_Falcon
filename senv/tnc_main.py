import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from tnc_main_ui import Ui_MainWindow
from tnc_controller import TrainController
from signals import signals


class TrainControllerMain(QObject):

    def __init__(self):
        print("train controller running")
        super().__init__()

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.controller_thread = QThread()
        self.controller = TrainController()
        self.controller.moveToThread(self.controller_thread)
        self.controller_thread.start()

        self.controller.updated.connect(self.update_gui)
        self.ui.brake_button.clicked.connect(self.emergency_brake)
        self.ui.brake_button_2.clicked.connect(self.service_brake)


    def update_gui(self):
        self.ui.curr_speed_text.setText(str(int(self.controller.powsys.current_speed * 2.237)) + " mph")
        self.ui.max_speed_text.setText(str(int(self.controller.powsys.command_speed * 2.237)) + " mph")
        self.ui.power_text.setText(str(int(self.controller.powsys.power/1000.0)) + " kW")

    def emergency_brake(self):
        if not self.controller.emergency_brake:
            self.ui.brake_button.setText("CANCEL")
            self.ui.brake_button.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
            self.controller.driver_emer_brake = True
            signals.tnc_emergency_brake.emit(True)
        else:
            self.ui.brake_button.setText("EMERGENCY BRAKE")
            self.ui.brake_button.setStyleSheet("background-color: red; color: white;")
            self.controller.driver_emer_brake = False
            if(not self.controller.emergency_brake):
                signals.tnc_emergency_brake.emit(False)

    def service_brake(self):
        if not self.controller.driver_serv_brake:
            self.ui.brake_button_2.setText("cancel")
            self.ui.brake_button_2.setStyleSheet("background-color: lightgray; color: white;")
            self.controller.driver_serv_brake = True
        else:
            self.ui.brake_button_2.setText("Service Brake")
            self.ui.brake_button_2.setStyleSheet("background-color: gray; color: white;")
            self.controller.driver_serv_brake = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    c = TrainControllerMain()
    app.exec_()
