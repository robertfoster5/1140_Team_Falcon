from tnc_power_system import PowerSystem

class TrainController(QObject):

    def __init__(self):
        super().__init__()
        self.auto_mode = True
        self.authority = False
        self.at_station = False
        self.in_tunnel = False
        self.left_side = False
        self.emergency_brake = False
        self.service_brake = False
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


    def set_command_speed(self,num):
        self.powsys.command_speed = num
        if(self.powsys.set_speed > num):
            self.powsys.set_speed = num
        self.powsys.update_power()

    def set_set_speed(self,num):
        if(self.auto_mode or (num > self.powsys.command_speed)):
            self.powsys.set_speed = self.powsys.command_speed
        else:
            self.powsys.set_speed = num
        self.powsys.update_power()

    def toggle_mode(self):
        self.powsys.set_speed = self.powsys.command_speed
        if(self.auto_mode):
            self.auto_mode = False
        else:
            self.auto_mode = True

    #def read_beacon(int):


    def run(self):
        if(self.auto_mode):
            if (self.at_station and not self.authority and self.powsys.current_speed == 0):
                self.left_door = True

            if(self.emergency_brake):
                self.powsys.braking = True
                self.announcement = "EMERGENCY BRAKING!\nPLEASE REMAIN SEATED"
            elif(not self.authority):
                self.powsys.braking = True
                self.service_brake = True
            elif(self.powsys.command_speed == 0 and self.authority):
                self.at_station = True
                if(self.powsys.current_speed > 10):
                    self.powsys.braking = True
                    self.service_brake = True
                else:
                    self.powsys.braking = False
                    self.service_brake = False
                    self.set_command_speed(10)
            else:
                self.powsys.braking = False
                self.service_brake = False

            if(self.in_tunnel):
                self.tunnel_light = True
            else:
                self.tunnel_light = False








