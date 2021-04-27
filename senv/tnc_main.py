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

        self.curr_train = 1
        self.trains = [TrainController(1),TrainController(2),TrainController(3),TrainController(4),TrainController(5),TrainController(6),TrainController(7),TrainController(8),TrainController(9),TrainController(10)]

        self.controller_thread1 = QThread()
        self.trains[0].moveToThread(self.controller_thread1)
        self.controller_thread1.start()

        self.controller_thread2 = QThread()
        self.trains[1].moveToThread(self.controller_thread2)
        self.controller_thread2.start()

        self.controller_thread3 = QThread()
        self.trains[2].moveToThread(self.controller_thread3)
        self.controller_thread3.start()

        self.controller_thread4 = QThread()
        self.trains[3].moveToThread(self.controller_thread4)
        self.controller_thread4.start()

        self.controller_thread5 = QThread()
        self.trains[4].moveToThread(self.controller_thread5)
        self.controller_thread5.start()

        self.controller_thread6 = QThread()
        self.trains[5].moveToThread(self.controller_thread6)
        self.controller_thread6.start()

        self.controller_thread7 = QThread()
        self.trains[6].moveToThread(self.controller_thread7)
        self.controller_thread7.start()

        self.controller_thread8 = QThread()
        self.trains[7].moveToThread(self.controller_thread8)
        self.controller_thread8.start()

        self.controller_thread9 = QThread()
        self.trains[8].moveToThread(self.controller_thread9)
        self.controller_thread9.start()

        self.controller_thread10 = QThread()
        self.trains[9].moveToThread(self.controller_thread10)
        self.controller_thread10.start()

        self.ui.speed_slider.hide()
        self.ui.listWidget.hide()

        signals.time.connect(self.update_gui)
        self.ui.brake_button.clicked.connect(self.emergency_brake)
        self.ui.brake_button_2.clicked.connect(self.service_brake)
        signals.tnc_announcement.connect(self.display_announcement)
        self.ui.auto_check.stateChanged.connect(self.automatic_mode)

        signals.tnm_comm_speed.connect(self.set_command_speed)
        signals.tnm_curr_speed.connect(self.set_curr_speed)
        signals.tnm_curr_speed.connect(self.power_calc)
        signals.tnm_authority.connect(self.set_authority)
        signals.tnm_ebrake.connect(self.set_pass_brake)
        signals.tnm_curr_station.connect(self.set_station)
        signals.tnm_beaconID.connect(self.set_tunnels)
        signals.tnm_TrainDir.connect(self.set_side)
        signals.tnm_sendyard.connect(self.failure)

    def set_command_speed(self,input,num):
        self.trains[num-1].set_command_speed(input)

    def set_curr_speed(self,input,num):
        self.trains[num-1].set_curr_speed(input)

    def power_calc(self,input,num):
        self.trains[num-1].power_calc()

    def set_authority(self,input,num):
        self.trains[num-1].set_authority(input)

    def set_pass_brake(self,input,num):
        self.trains[num-1].set_pass_brake(input)

    def set_station(self,input,num):
        self.trains[num-1].set_station(input)

    def set_side(self,input,num):
        self.trains[num-1].set_side(input)

    def failure(self,input,num):
        self.trains[num-1].failure(input)

    def set_tunnels(self,input,num):
        self.trains[num-1].set_tunnels(input)


    def update_gui(self):
        self.ui.curr_speed_text.setText(str(int(self.trains[self.curr_train-1].powsys.current_speed)) + " mph")
        self.ui.max_speed_text.setText(str(int(self.trains[self.curr_train-1].powsys.command_speed)) + " mph")
        self.ui.power_text.setText(str(int(self.trains[self.curr_train-1].powsys.power/1000.0)) + " kW")
        if(self.trains[self.curr_train-1].auto_mode):
            self.ui.set_speed_text.setText(str(self.trains[self.curr_train-1].powsys.set_speed) + " mph")
            self.ui.speed_slider.setValue(int(self.trains[self.curr_train-1].powsys.command_speed))

    def emergency_brake(self):
        if not self.trains[self.curr_train-1].driver_emer_brake:
            self.ui.brake_button.setText("CANCEL")
            self.ui.brake_button.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
            self.trains[self.curr_train-1].driver_emer_brake = True
            signals.tnc_emergency_brake.emit(True,self.curr_train)
        else:
            self.ui.brake_button.setText("EMERGENCY BRAKE")
            self.ui.brake_button.setStyleSheet("background-color: red; color: white;")
            self.trains[self.curr_train-1].driver_emer_brake = False
            if(not self.trains[self.curr_train-1].emergency_brake):
                signals.tnc_emergency_brake.emit(False,self.curr_train)

    def service_brake(self):
        if not self.trains[self.curr_train-1].driver_serv_brake:
            self.ui.brake_button_2.setText("cancel")
            self.ui.brake_button_2.setStyleSheet("background-color: lightgray; color: white;")
            self.trains[self.curr_train-1].driver_serv_brake = True
        else:
            self.ui.brake_button_2.setText("Service Brake")
            self.ui.brake_button_2.setStyleSheet("background-color: gray; color: white;")
            self.trains[self.curr_train-1].driver_serv_brake = False

    def display_announcement(self,text):
        self.ui.announce_text.setPlainText(text)

    def automatic_mode(self):
        if(self.ui.auto_check.isChecked()):
            self.ui.speed_slider.hide()
            self.ui.listWidget.hide()
            self.ui.auto_check.setText("On")
            self.trains[self.curr_train-1].set_set_speed(self.trains[self.curr_train-1].powsys.command_speed)
            self.ui.speed_slider.setValue(int(self.trains[self.curr_train-1].powsys.command_speed))
            self.trains[self.curr_train-1].auto_mode = True
        else:
            self.ui.speed_slider.show()
            self.ui.listWidget.show()
            self.ui.auto_check.setText("Off")
            self.trains[self.curr_train-1].auto_mode = False

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    c = TrainControllerMain()
    app.exec_()
