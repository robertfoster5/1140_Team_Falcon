from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class Signal(QObject):
    #global
    time = pyqtSignal(int,int,int,int) #sec, min, hour, total time
    time_multiplier = pyqtSignal(int)
    pause = pyqtSignal()

    #ctc signals
    ctc_authority_green = pyqtSignal(list)
    ctc_suggested_speed_green = pyqtSignal(list)
    ctc_authority_red = pyqtSignal(list)
    ctc_suggested_speed_red = pyqtSignal(list)
    ctc_maintenance = pyqtSignal(list)
    ctc_make_train_red = pyqtSignal(str)
    ctc_make_train_green = pyqtSignal(str)
    ctc_destroy_train_green = pyqtSignal(int)
    ctc_destroy_train_red = pyqtSignal(int)


    #wayside signals
    #green line
    way_green_occupancy = pyqtSignal(list)
    way_green_occupancy_ctc = pyqtSignal(list)
    way_green_cross_state = pyqtSignal(list)
    way_green_switch_state = pyqtSignal(list)
    way_green_authority = pyqtSignal(list)
    way_green_speed = pyqtSignal(list)
    way_green_health = pyqtSignal(list)
    #red line
    way_red_occupancy = pyqtSignal(list)
    way_red_occupancy_ctc = pyqtSignal(list)
    way_red_cross_state = pyqtSignal(list)
    way_red_switch_state = pyqtSignal(list)
    way_red_authority = pyqtSignal(list)
    way_red_speed = pyqtSignal(list)
    way_red_health = pyqtSignal(list)

    #track model signals
    tkm_get_occ = pyqtSignal(list)
    tkm_get_speed = pyqtSignal(int,int)
    tkm_get_auth = pyqtSignal(list)
    tkm_get_train_auth = pyqtSignal(int,int)
    tkm_get_beacon = pyqtSignal(int,int)
    tkm_get_envi_temp = pyqtSignal(float)
    tkm_get_sales = pyqtSignal(int)
    tkm_get_pass_count = pyqtSignal(int,int)
    tkm_get_block = pyqtSignal(int,int)
    tkm_get_blength = pyqtSignal(int,int)
    tkm_get_train_num = pyqtSignal(int,str)
    tkm_get_elev = pyqtSignal(float,int)
    tkm_get_destroy = pyqtSignal(int)

    #train model signals
    tnm_comm_speed = pyqtSignal(float, int)
    tnm_curr_speed = pyqtSignal(float, int)
    tnm_authority = pyqtSignal(bool, int)
    tnm_beaconID = pyqtSignal(int, int)
    tnm_ebrake = pyqtSignal(bool, int)
    tnm_sendyard = pyqtSignal(bool, int)
    tnm_cab_temp = pyqtSignal(list)
    tnm_block_finished_green = pyqtSignal(int)
    tnm_block_finished_red = pyqtSignal(int)
    tnm_curr_station = pyqtSignal(str, int)
    tnm_TrainDir = pyqtSignal(bool, int)
    tnm_train_stop_num = pyqtSignal(int)

    #train controller signals
    tnc_emergency_brake = pyqtSignal(bool,int)
    tnc_service_brake = pyqtSignal(bool,int)
    tnc_announcement = pyqtSignal(str,int)
    tnc_power = pyqtSignal(float,int)
    tnc_cab_light = pyqtSignal(bool,int)
    tnc_tunnel_light = pyqtSignal(bool,int)
    tnc_high_beam_light = pyqtSignal(bool,int)
    tnc_left_door = pyqtSignal(bool,int) #1 for open 0 for closed
    tnc_right_door = pyqtSignal(bool,int) #1 for open 0 for closed


signals = Signal()
