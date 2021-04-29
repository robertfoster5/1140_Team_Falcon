from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from tnc_power_system import PowerSystem
from power_ui import Ui_PowerUi
from signals import signals


class TrainController(QObject):

    stations = ["Pioneer","EdgeBrook","Falcon","Whited","South Bank","Central","Inglewood","Overbrook","Glenbury","Dormont","Mt Lebanon","Poplar","Castle Shannon","Shady Side","Herron Ave","Penn Station","Steel Plaza","First Ave","Station Square","South Hills","Swissville"]

    doors = [0,0,2,2,0,1,1,1,1,1,2,0,0,2,2,2,2,2,2,2,2]

    def __init__(self,num):
        super().__init__()

        self.train_num = num
        self.start = False
        self.auto_mode = True
        self.authority = False
        self.at_station = False
        self.in_tunnel = False
        self.direction = 0
        self.station_side = 0
        self.emergency_brake = False
        self.service_brake = False
        self.driver_serv_brake = False
        self.driver_emer_brake = False
        self.pass_brake = False
        self.tunnel_light = False
        self.cabin_light = False
        self.high_beam_light = False
        self.left_door = False
        self.right_door = False
        self.signal_fail = False
        self.engine_fail = False
        self.brake_fail = False
        self.powsys = PowerSystem()
        self.station = ""
        self.stopping = False
        self.station_stop = False
        self.announcement = ""
        self.count = 0

        self.Window = QtWidgets.QWidget()
        self.powui = Ui_PowerUi()
        self.powui.setupUi(self.Window)
        self.powui.label.setText("KP and KI for Train " + str(self.train_num) + ":")

        signals.time.connect(self.run)
        self.powui.pushButton.clicked.connect(self.set_coeff)

        self.init_periph()


    def init_periph(self):
        self.tunnel_light = False;
        self.cabin_light = True;
        self.high_beam_light = False;

        signals.tnc_cab_light.emit(True,self.train_num)
        signals.tnc_tunnel_light.emit(False,self.train_num)
        signals.tnc_high_beam_light.emit(False,self.train_num)

        self.right_door = False;
        self.left_door = False;

        signals.tnc_left_door.emit(False)
        signals.tnc_right_door.emit(False)

    def set_coeff(self):
        kp = 5000
        ki = 0
        kp_text = self.powui.kp_enter.text()
        ki_text = self.powui.ki_enter.text()

        if(kp_text.isdigit()):
            if(int(kp_text) > 0):
                kp = int(kp_text)

        if(ki_text.isdigit()):
            if(int(ki_text) > 0):
                ki = int(ki_text)

        self.powsys.set_coeffs(kp,ki)

        self.Window.hide()


    def set_command_speed(self,num):
        self.powsys.command_speed = num
        if(self.powsys.set_speed > num):
            self.powsys.set_speed = num
        if(self.auto_mode):
            self.powsys.set_speed = num

    def set_curr_speed(self,num):
        self.powsys.current_speed = num

    def set_authority(self,on):
        self.authority = on
        if(self.start == False and on == True):
            self.start = True
            self.Window.show()

    def set_pass_brake(self,on):
        self.pass_brake = on

    def set_set_speed(self,num):
        if(self.auto_mode or (num > self.powsys.command_speed)):
            self.powsys.set_speed = self.powsys.command_speed
        else:
            self.powsys.set_speed = num

    def toggle_mode(self):
        self.powsys.set_speed = self.powsys.command_speed
        if(self.auto_mode):
            self.auto_mode = False
        else:
            self.auto_mode = True

    def set_station(self,name):
        self.station = name
        if(self.stations.count(self.station) > 0):
            side = doors[self.stations.index(self.station)]
            if((not self.direction) or (side == 2)):
                self.station_side = side
            elif(side == 1):
                self.station_side = 0
            else:
                self.station_side = 1

        self.at_station = True

    def set_side(self,direction):
        self.direction = direction

    def set_tunnels(self,beaconID):
        beacon = bin(beaconID)
        if(len(beacon)>3):
            tunnel = beacon[3]
            if(self.auto_mode and tunnel == "1"):
                if(not self.tunnel_light):
                    self.tunnel_light = True;
                    self.high_beam_light = False;

                    signals.tnc_tunnel_light.emit(True,self.train_num)
                    signals.tnc_high_beam_light.emit(False,self.train_num)
                else:
                    self.tunnel_light = False;

                    signals.tnc_tunnel_light.emit(False,self.train_num)

    def failure(self,fail):
        if(fail):
            self.emergency_brake = True
            signals.tnc_emergency_brake.emit(True,self.train_num)
        elif(not self.driver_emer_brake):
            self.emergency_brake = False
            signals.tnc_emergency_brake.emit(False,self.train_num)
        else:
            self.emergency_brake = False

    def announce_emergency(self,on):
        if(on):
            self.announcement = "EMERGENCY BRAKING!\nPLEASE STAY SEATED"
            signals.tnc_announcement.emit(self.announcement,self.train_num)
        else:
            self.announcement = ""
            signals.tnc_announcement.emit(self.announcement,self.train_num)


    def run(self):
        if(self.auto_mode):
            if(self.count >= 60):
                self.announcement = ""
                signals.tnc_announcement.emit(self.announcement,self.train_num)
                self.count = 0
                self.station_stop = False
                self.left_door = False
                signals.tnc_left_door.emit(False)
                self.right_door = False
                signals.tnc_right_door.emit(False)
            elif(self.count > 0):
                self.count+=1

            if (self.at_station and (not self.authority) and self.powsys.current_speed == 0 and self.count == 0):
                self.announcement = "Now Arriving at:\n" + self.station + " Station"
                print("NOW ARRIVING AT A STATION")
                self.at_station = False
                signals.tnc_announcement.emit(self.announcement,self.train_num)
                self.count+=1
                self.station_stop = True
                if(self.station_side == 0):
                    self.left_door = True
                    signals.tnc_left_door.emit(True)
                elif(self.station_side == 1):
                    self.right_door = True
                    signals.tnc_right_door.emit(True)
                else:
                    self.left_door = True
                    signals.tnc_left_door.emit(True)
                    self.right_door = True
                    signals.tnc_right_door.emit(True)
            else:
                if(self.at_station):
                    self.count = 0
                    self.station_stop = False
                    self.left_door = False
                    signals.tnc_left_door.emit(False)
                    self.right_door = False
                    signals.tnc_right_door.emit(False)

    def power_calc(self):
        if(not self.authority):
            self.service_brake = True
            print("no authority brake for train " + str(self.train_num))
        #elif(self.powsys.command_speed == 0 and self.authority):
        #    if(self.powsys.current_speed > 5):
        #        self.service_brake = True
        #    else:
        #        self.service_brake = False
        #        self.set_command_speed(5)
        elif(self.station_stop):
            self.service_brake = True
            print("station stop brake for train " + str(self.train_num))
        elif(self.driver_serv_brake):
            self.service_brake = True
            print("driver brake for train " + str(self.train_num))
        else:
            self.service_brake = False

        if(self.emergency_brake or self.service_brake or self.pass_brake or self.station_stop):
            self.powsys.braking = True
        else:
            self.powsys.braking = False

        #print(str(round(self.powsys.command_speed,1)) + " comm speed in m/s")
        print(str(round(self.powsys.command_speed,2)) + " comm speed train " + str(self.train_num) + " in mph")
        #print(round(self.powsys.set_speed,1))

        self.powsys.update_power()

        if(self.powsys.power == 0 and (self.powsys.command_speed != self.powsys.current_speed)):
            print("no power brake for train " + str(self.train_num))
            self.service_brake = True

        signals.tnc_service_brake.emit(self.service_brake,self.train_num)

        signals.tnc_power.emit(self.powsys.power,self.train_num)


if __name__ == '__main__':
    a = TrainController(3)
    a.set_command_speed(10)
    a.set_authority(True)
    a.run()
    a.power_calc()










