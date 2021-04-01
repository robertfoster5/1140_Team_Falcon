from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal

import time
from signals import signals


#def clock(env,mil):
#start = time.perf_counter()
#yield env.timeout(1)
#end = time.perf_counter()
#print('Duration of one simulation time unit: %.2fs' % (end - start))


class timing(QObject):
    def __init__(self):
        super().__init__()
        self.sec = 0
        self.mint = 0
        self.hr = 0
        self.run()

    def run(self):
        check = 0
        timer = 0
        while True:
            self.sec = timer - (check*60)
            if self.sec == 60:
                self.mint = self.mint+1
                self.sec = 0
                check = check+1
                if self.mint ==  60:
                    self.hr = self.hr+1
                    self.mint = 0
                    if self.hr == 24:
                        self.hr = 0
            print('The time is ' + str(self.hr)+ ':' + str(self.mint) + ':' +str(self.sec))
            signals.time.emit(self.sec,self.mint,self.hr,timer)
            timer += 1
            time.sleep(1)

if __name__ == '__main__':
    t = timing()
