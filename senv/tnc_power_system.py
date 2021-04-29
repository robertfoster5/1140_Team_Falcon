from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal

from signals import signals


class PowerSystem():

    def __init__(self):
        self.braking = False
        self.power = 0
        self.error = 0
        self.u = 0
        self.set_speed = 0
        self.command_speed = 0
        self.current_speed = 0
        self.kp = 0
        self.ki = 0

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

        if(self.power > 120000):
            self.power = 120000


    def set_coeffs(self,p,i):
        self.kp = p
        self.ki = i

if __name__ == '__main__':
    a = PowerSystem()
    a.command_speed = 10
    a.set_speed = 10
    a.update_power()
