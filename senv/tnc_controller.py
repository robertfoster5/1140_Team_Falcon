from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from tnc_power_system import PowerSystem
from signals import signals


class TrainController(QObject):

    updated = pyqtSignal()

    stations = ["Pioneer","EdgeBrook","Falcon","Whited","South Bank","Central","Inglewood","Overbrook","Glenbury","Dormont","Mt Lebanon","Poplar","Castle Shannon","Shady Side","Herron Ave","Penn Station","Steel Plaza","First Ave","Station Square","South Hills","Swissville"]

    doors = [0,0,2,2,0,1,1,1,1,1,2,0,0,2,2,2,2,2,2,2,2]

    def __init__(self):
        super().__init__()
        self.auto_mode = True
        self.authority = False
        self.at_station = False
        self.in_tunnel = False
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

        signals.time.connect(self.run)
        signals.tnm_comm_speed.connect(self.set_command_speed)
        signals.tnm_curr_speed.connect(self.set_curr_speed)
        signals.tnm_authority.connect(self.set_authority)
        signals.tnm_ebrake.connect(self.set_pass_brake)
        signals.tnm_curr_station.connect(self.set_station)
        signals.tnm_beaconID.connect(self.set_tunnels)
        signals.tnm_TrainDir.connect(self.set_side)
        signals.tnm_sendyard.connect(self.failure)
        signals.tnc_emergency_brake.connect(self.announce_emergency)

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

    def set_station(self,name):
        self.station = name

    def set_side(self,direction):
        if(stations.count(self.station) > 0):
            side = doors[stations.index(self.station)]
            if((not direction) or (side == 2)):
                self.station_side = side
            elif(side == 1):
                self.station_side = 0
            else:
                self.station_side = 1

        if(not self.at_station):
            self.at_station = True
        else:
            self.at_station = False

    def set_tunnels(self,beaconID):
        beacon = bin(beaconID)
        if(len(beacon)>3):
            tunnel = beacon[3]
            if(self.auto_mode and tunnel == "1"):
                if(not self.tunnel_light):
                    self.tunnel_light = True;
                    self.high_beam_light = False;

                    signals.tnc_tunnel_light.emit(True)
                    signals.tnc_high_beam_light.emit(False)
                else:
                    self.tunnel_light = False;

                    signals.tnc_tunnel_light.emit(False)

    def failure(self,fail):
        if(fail):
            self.emergency_brake = True
            signals.tnc_emergency_brake.emit(True)
        elif(not self.driver_emer_brake):
            self.emergency_brake = False
            signals.tnc_emergency_brake.emit(False)
        else:
            self.emergency_brake = False

    def announce_emergency(self,on):
        if(on):
            self.announcement = "EMERGENCY BRAKING!\nPLEASE STAY SEATED"
            signals.tnc_announcement.emit(self.announcement)
        else:
            self.announcement = ""
            signals.tnc_announcement.emit(self.announcement)


    def run(self):
        if(self.auto_mode):
            if(self.count >= 60):
                self.announcement = ""
                signals.tnc_announcement.emit(self.announcement)
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
                signals.tnc_announcement.emit(self.announcement)
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


        if(not self.authority):
            self.service_brake = True
        #elif(self.powsys.command_speed == 0 and self.authority):
        #    if(self.powsys.current_speed > 5):
        #        self.service_brake = True
        #    else:
        #        self.service_brake = False
        #        self.set_command_speed(5)
        elif(self.station_stop):
            self.service_brake = True
        elif(self.driver_serv_brake):
            self.service_brake = True
        else:
            self.service_brake = False

        if(self.emergency_brake or self.service_brake or self.pass_brake or self.station_stop):
            self.powsys.braking = True
        else:
            self.powsys.braking = False

        #print(str(round(self.powsys.command_speed,1)) + " comm speed in m/s")
        print(str(int(self.powsys.command_speed)) + " comm speed in mph")
        #print(round(self.powsys.set_speed,1))

        self.powsys.update_power()

        if(self.powsys.power == 0 and (self.powsys.command_speed != self.powsys.current_speed)):
            self.service_brake = True

        if(self.service_brake):
            print("service brake on")

        signals.tnc_service_brake.emit(self.service_brake)

        signals.tnc_power.emit(self.powsys.power)

        self.updated.emit()

if __name__ == '__main__':
    a = TrainController()
    a.set_command_speed(10)
    a.set_authority(True)
    a.run()










