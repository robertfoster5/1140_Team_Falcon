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

        #This builds and displays the Main Window for the Train Controller UI
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

        #initializes 10 different controllers representing each train
        self.curr_train = 1
        self.trains = [TrainController(1),TrainController(2),TrainController(3),TrainController(4),TrainController(5),TrainController(6),TrainController(7),TrainController(8),TrainController(9),TrainController(10)]

        #moves each train controller into a seperate thread
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

        #initializes UI into auto mode
        self.ui.speed_slider.hide()
        self.ui.listWidget.hide()

        #functions for update the Train Controller UI
        signals.time.connect(self.update_gui)
        self.ui.brake_button.clicked.connect(self.emergency_brake)
        self.ui.brake_button_2.clicked.connect(self.service_brake)
        signals.tnc_announcement.connect(self.display_announcement)
        self.ui.auto_check.stateChanged.connect(self.automatic_mode)
        self.ui.speed_slider.valueChanged.connect(self.change_set_speed)
        self.ui.in_light_check.stateChanged.connect(self.toggle_in_light)
        self.ui.tunnel_light_check.stateChanged.connect(self.toggle_tunnel_light)
        self.ui.beam_light_check.stateChanged.connect(self.toggle_beam_light)
        signals.tnc_emergency_brake.connect(self.announce_emergency)
        signals.tnc_cab_light.connect(self.set_in_light)
        signals.tnc_tunnel_light.connect(self.set_tunnel_light)
        signals.tnc_high_beam_light.connect(self.set_beam_light)
        self.ui.left_door_check.stateChanged.connect(self.toggle_left_door)
        self.ui.right_door_check.stateChanged.connect(self.toggle_right_door)
        signals.tnc_left_door.connect(self.set_left_door)
        signals.tnc_right_door.connect(self.set_right_door)
        self.ui.train_num.currentIndexChanged.connect(self.set_curr_train)

        #functions to send input signal to specific train
        signals.tnm_comm_speed.connect(self.set_command_speed)
        signals.tnm_curr_speed.connect(self.set_curr_speed)
        signals.tnm_curr_speed.connect(self.power_calc)
        signals.tnm_authority.connect(self.set_authority)
        signals.tnm_ebrake.connect(self.set_pass_brake)
        signals.tnm_curr_station.connect(self.set_station)
        signals.tnm_beaconID.connect(self.set_tunnels)
        signals.tnm_TrainDir.connect(self.set_side)
        signals.tnm_sendyard.connect(self.failure)

        #initializes cabin lights to be on
        self.set_in_light()

    #when a train from the drop-down menu is selected, reload the display with the values for the selected train
    def set_curr_train(self):
        self.curr_train = self.ui.train_num.currentIndex() + 1

        self.update_gui()

        self.set_in_light()
        self.set_tunnel_light()
        self.set_beam_light()
        self.set_right_door()
        self.set_left_door()

        self.ui.auto_check.setChecked(self.trains[self.curr_train-1].auto_mode)
        self.automatic_mode()

        self.set_fail_light()
        self.set_brake_light()

        self.display_announcement(self.trains[self.curr_train-1].announcement,self.curr_train)


    #these functions recieve an input from another module and sends it to the specified train (num)
    def set_command_speed(self,input,num):
        self.trains[num-1].set_command_speed(input)

    def set_curr_speed(self,input,num):
        self.trains[num-1].set_curr_speed(input)

    def power_calc(self,input,num):
        self.trains[num-1].power_calc()

    def set_authority(self,input,num):
        self.trains[num-1].set_authority(input)

    def set_pass_brake(self,input,num):
        self.trains[num-1].announce_emergency(input)
        self.trains[num-1].set_pass_brake(input)
        self.set_brake_light()

    def announce_emergency(self,input,num):
        self.trains[num-1].announce_emergency(input)

    def set_station(self,input,num):
        self.trains[num-1].set_station(input)

    def set_side(self,input,num):
        self.trains[num-1].set_side(input)

    def failure(self,input,num):
        self.trains[num-1].failure(input)
        self.set_fail_light()

    def set_tunnels(self,input,num):
        self.trains[num-1].set_tunnels(input)

    #this updated the set speed when the speed slider is changed
    def change_set_speed(self):
        self.trains[self.curr_train-1].set_set_speed(self.ui.speed_slider.value())

    #this updates the speed values in the UI every second as well as when a new train is viewed
    def update_gui(self):
        self.ui.curr_speed_text.setText(str(int(self.trains[self.curr_train-1].powsys.current_speed)) + " mph")
        self.ui.max_speed_text.setText(str(int(self.trains[self.curr_train-1].powsys.command_speed)) + " mph")
        self.ui.power_text.setText(str(int(self.trains[self.curr_train-1].powsys.power/1000.0)) + " kW")
        self.ui.set_speed_text.setText(str(int(self.trains[self.curr_train-1].powsys.set_speed)) + " mph")

    #this turns on or off the driver initiated emergency brake as well as update the UI
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

    #this turns on or off the driver initiated service brake as well as update the UI
    def service_brake(self):
        if not self.trains[self.curr_train-1].driver_serv_brake:
            self.ui.brake_button_2.setText("cancel")
            self.ui.brake_button_2.setStyleSheet("background-color: lightgray; color: white;")
            self.trains[self.curr_train-1].driver_serv_brake = True
        else:
            self.ui.brake_button_2.setText("Service Brake")
            self.ui.brake_button_2.setStyleSheet("background-color: gray; color: white;")
            self.trains[self.curr_train-1].driver_serv_brake = False


    def display_announcement(self,text,num):
        if(num == self.curr_train):
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

    def toggle_in_light(self):
        if(self.ui.in_light_check.isChecked()):
            self.trains[self.curr_train-1].cabin_light = True
            signals.tnc_cab_light.emit(True,self.curr_train)
        else:
            self.trains[self.curr_train-1].cabin_light = False
            signals.tnc_cab_light.emit(False,self.curr_train)

    def toggle_tunnel_light(self):
        if(self.ui.tunnel_light_check.isChecked()):
            self.trains[self.curr_train-1].tunnel_light = True
            signals.tnc_tunnel_light.emit(True,self.curr_train)
        else:
            self.trains[self.curr_train-1].tunnel_light = False
            signals.tnc_tunnel_light.emit(False,self.curr_train)

    def toggle_beam_light(self):
        if(self.ui.beam_light_check.isChecked()):
            self.trains[self.curr_train-1].high_beam_light = True
            signals.tnc_high_beam_light.emit(True,self.curr_train)
        else:
            self.trains[self.curr_train-1].high_beam_light = False
            signals.tnc_high_beam_light.emit(False,self.curr_train)

    def set_in_light(self):
        if(self.trains[self.curr_train-1].cabin_light):
            self.ui.in_light_check.setText("On")
            self.ui.in_light_check.setChecked(True)
        else:
            self.ui.in_light_check.setText("Off")
            self.ui.in_light_check.setChecked(False)

    def set_tunnel_light(self):
        if(self.trains[self.curr_train-1].tunnel_light):
            self.ui.tunnel_light_check.setText("On")
            self.ui.tunnel_light_check.setChecked(True)
        else:
            self.ui.tunnel_light_check.setText("Off")
            self.ui.tunnel_light_check.setChecked(False)

    def set_beam_light(self):
        if(self.trains[self.curr_train-1].high_beam_light):
            self.ui.beam_light_check.setText("On")
            self.ui.beam_light_check.setChecked(True)
        else:
            self.ui.beam_light_check.setText("Off")
            self.ui.beam_light_check.setChecked(False)

    def toggle_left_door(self):
        if(self.ui.left_door_check.isChecked()):
            self.trains[self.curr_train-1].left_door = True
            signals.tnc_left_door.emit(True,self.curr_train)
        else:
            self.trains[self.curr_train-1].left_door = False
            signals.tnc_left_door.emit(False,self.curr_train)

    def toggle_right_door(self):
        if(self.ui.right_door_check.isChecked()):
            self.trains[self.curr_train-1].right_door = True
            signals.tnc_right_door.emit(True,self.curr_train)
        else:
            self.trains[self.curr_train-1].right_door = False
            signals.tnc_right_door.emit(False,self.curr_train)

    def set_left_door(self):
        if(self.trains[self.curr_train-1].left_door):
            self.ui.left_door_check.setText("Open")
            self.ui.left_door_check.setChecked(True)
        else:
            self.ui.left_door_check.setText("Closed")
            self.ui.left_door_check.setChecked(False)

    def set_right_door(self):
        if(self.trains[self.curr_train-1].right_door):
            self.ui.right_door_check.setText("Open")
            self.ui.right_door_check.setChecked(True)
        else:
            self.ui.right_door_check.setText("Closed")
            self.ui.right_door_check.setChecked(False)

    def set_fail_light(self):
        if(self.trains[self.curr_train-1].fail_state):
            self.ui.brake_fail_led.setStyleSheet("border: 2px solid #555;border-radius: 15px;border-style: outset;background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #888);padding: 5px; background-color: red;")
        else:
            self.ui.brake_fail_led.setStyleSheet("border: 2px solid #555;border-radius: 15px;border-style: outset;background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #888);padding: 5px; background-color: rgb(122, 0, 0);")

    def set_brake_light(self):
        if(self.trains[self.curr_train-1].pass_brake):
            self.ui.pass_brake_led.setStyleSheet("border: 2px solid #555;border-radius: 15px;border-style: outset;background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #888);padding: 5px; background-color: red;")
        else:
            self.ui.pass_brake_led.setStyleSheet("border: 2px solid #555;border-radius: 15px;border-style: outset;background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #888);padding: 5px; background-color: rgb(122, 0, 0);")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    c = TrainControllerMain()
    app.exec_()
