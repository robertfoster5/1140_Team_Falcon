from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class Signal(QObject):
    #ctc signals
    ctc_authority = pyqtSignal(list)
    ctc_suggested_speed = pyqtSignal(list)
    ctc_maintenance = pyqtSignal(list)

    #wayside signals
    wayside_occupancy = pyqtSignal(list)
    wayside_cross_state = pyqtSignal(list)
    wayside_switch_state = pyqtSignal(list)
    wayside_authority = pyqtSignal(list)
    wayside_speed = pyqtSignal(list)

    #track model signals
    tkm_get_occ = pyqtSignal(list)
    tkm_get_speed = pyqtSignal(int)
    tkm_get_auth = pyqtSignal(list)
    tkm_get_beacon = pyqtSignal(int)
    tkm_get_envi_temp = pyqtSignal(int)
    tkm_get_sales = pyqtSignal(int)
    tkm_get_pass_count = pyqtSignal(int)

    #train model signals
    tnm_comm_speed = pyqtSignal(float)
    tnm_authority = pyqtSignal(int)
    tnm_beacondID = pyqtSignal(list)
    tnm_ebrake = pyqtSignal(bool)
    tnm_sendyard = pyqtSignal(bool)
    tnm_cab_temp = pyqtSignal(int)

    #train controller signals
    tnc_emergency_brake = pyqtSignal(bool)
    tnc_service_brake = pyqtSignal(bool)
    tnc_announcement = pyqtSignal(str)
    tnc_power = pyqtSignal(float)


signals = Signal()