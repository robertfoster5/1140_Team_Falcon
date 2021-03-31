

class PowerSystem():

    def __init__(self):
        self.braking = False
        self.power = 0
        self.error = 0
        self.u = 0
        self.set_speed = 0
        self.command_speed = 0
        self.current_speed = 0
        self.kp = 6000
        self.ki = 0
        self.time = 0

    def update_power(self):
        error_last = self.error
        u_last = self.u

        if(self.set_speed > self.command_speed):
            speed = self.command_speed
        else:
            speed = self.set_speed

        self.error = speed - self.current_speed

        self.u = u_last + float(self.error + error_last)/2

        if(self.braking):
            self.power = 0
        else:
            self.power = float(self.kp) * self.error + float(self.ki) * self.u

        if(self.power < 0):
            self.power = 0;


    def set_coeffs(self,p,i):
        self.kp = p
        self.ki = i