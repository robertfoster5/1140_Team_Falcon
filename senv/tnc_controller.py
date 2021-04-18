from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from tnc_power_system import PowerSystem
from signals import signals


class TrainController(QObject):
    updated = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.auto_mode = True
        self.authority = False
        self.at_station = False
        self.in_tunnel = False
        self.left_side = False
        self.emergency_brake = False
        self.service_brake = False
        self.driver_serv_brake = False
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

        signals.time.connect(self.run)
        signals.tnm_comm_speed.connect(self.set_command_speed)
        signals.tnm_curr_speed.connect(self.set_curr_speed)
        signals.tnm_authority.connect(self.set_authority)
        signals.tnm_ebrake.connect(self.set_pass_brake)

        self.init_periph()

    def init_periph(self):
        self.tunnel_light = False;
        self.cabin_light = True;
        self.high_beam_light = False;

        signals.tnc_cab_light.emit(True)
        signals.tnc_tunnel_light.emit(False)
        signals.tnc_high_beam_light.emit(False)

        self.right_door = False;
        self.left_door = False;

        signals.tnc_left_door.emit(False)
        signals.tnc_right_door.emit(False)

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

    #def read_beacon(int):


    def run(self):
        if(self.auto_mode):
            if (self.at_station and (not self.authority) and self.powsys.current_speed == 0):
                self.left_door = True

        if(self.emergency_brake or self.pass_brake):
            self.announcement = "EMERGENCY BRAKING!\nPLEASE REMAIN SEATED"
        elif(not self.authority):
            self.service_brake = True
        elif(self.powsys.command_speed == 0 and self.authority):
            if(self.powsys.current_speed > 5):
                self.service_brake = True
            else:
                self.service_brake = False
                self.set_command_speed(5)
        else:
            self.service_brake = False

        if(self.driver_serv_brake):
            self.service_brake = True

        signals.tnc_service_brake.emit(self.service_brake)

        if(self.emergency_brake or self.service_brake or self.pass_brake):
            self.powsys.braking = True
        else:
            self.powsys.braking = False

            #if(self.in_tunnel):
            #    self.tunnel_light = True
            #else:
            #    self.tunnel_light = False

        #print(str(round(self.powsys.command_speed,1)) + " comm speed in m/s")
        print(str(int(self.powsys.command_speed * 2.237)) + "comm speed in mph")
        #print(round(self.powsys.set_speed,1))

        self.powsys.update_power()
        self.updated.emit()

if __name__ == '__main__':
    a = TrainController()
    a.set_command_speed(10)
    a.set_authority(True)
    a.run()










