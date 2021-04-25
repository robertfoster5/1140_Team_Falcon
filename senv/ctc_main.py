#from PyQt5 import uic
#from PyQt5.QtWidgets import QApplication

#Form, Window = uic.loadUiType(r"C:\Users\Robert\QT_Designer\ctc_qtui_test.ui")

#app = QApplication([])
#window = Window()
#form = Form()
#form.setupUi(window)
#window.show()
#app.exec()

import sys
import xlrd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
from ctc_qtui_test import Ui_CTC_Office
import csv
import tkinter as tk
from tkinter import filedialog
from tkm_class import Block
import math
from signals import signals


global_schedule_display = [[0,0,0]]
global_dispatched_trains = 0

global_order_path_hold = []
# [Train Name, Destination Station, Arrival Time(seconds),Start Time(seconds), Authority(meters), Suggested Speed(meters/second), Red or Green Line, Destination Block]
global_dispatch_orders = [
                           ["","",0,0,[0],[0],"skip",0] 
                         ]

global_dispatch_file = ""
global_expected_train_location = [0]
global_train_blocks = []
global_expected_train_location_hold = 0

def upX(x):
    x = x+62
    return x

def loadTrack(fileN):
    File = xlrd.open_workbook(fileN)
    j = 1
    
    t_file = File.sheet_by_index(0)
    
    track = []
    
    
    while t_file.cell(j,2).value != 0:
        if t_file.cell(j,6).value == xlrd.empty_cell.value:
            track.append(Block(t_file.cell(j,2).value,t_file.cell(j,3).value,t_file.cell(j,4).value,t_file.cell(j,5).value,0,0,0,t_file.cell(j,8).value,t_file.cell(j,9).value,0))
        else:    
            name = str(t_file.cell(j,6).value)
            name = name.split()
            if name[0] == "Station":
                n = name[1]
                #stat = Station(n,int(t_file.cell(j,2).value))
                track.append(Block(int(t_file.cell(j,2).value),int(t_file.cell(j,3).value),int(t_file.cell(j,4).value),int(t_file.cell(j,5).value),n,0,0,int(t_file.cell(j,8).value),int(t_file.cell(j,9).value),0))
            elif name[0] == "Switch":
                n = name[len(name)-1]

                if len(n)> 2:
                    n = n[0:2]
                else:
                    n = n[0]
                    
                track.append(Block(int(t_file.cell(j,2).value),int(t_file.cell(j,3).value),int(t_file.cell(j,4).value),int(t_file.cell(j,5).value),0,int(n),0,int(t_file.cell(j,8).value),int(t_file.cell(j,9).value),0))
        
        j = j+1
        #print(j)
        
    return track;

class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data,header):
        super(TableModel, self).__init__()
        self._data = data
        self.header = header

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])
        
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None


class ctc_qtui_test(QObject):
    def __init__(self):
        print("running ctc")
        super().__init__()
        self.ctc_main_window = QtWidgets.QMainWindow()
        self.ui = Ui_CTC_Office()
        self.ui.setupUi(self.ctc_main_window)
        self.ctc_main_window.show()
        
        header = ['Train', 'Destination Station', 'Arrival Time (2400)']
        

        
        # Dummy track occupancy that would be gotten from the wayside controller
        current_track_occupancy = "0000000000000000"
        
        # Dummy time (seconds) that would be gotten from the main system handler
        current_time = 0
        
        # Dummy throughput displayed in the main window
        test_throughput = 0
        
        # Dummy blue-track block information to be used in calculation
        test_block_info = [
         [50,-1,1,-1], # track length, left-neighbor-index (-1 if none),right-neighbor-index (-1 if none), switch-neighbor-index (-1 if none)
         [50,0,2,-1],
         [50,1,3,-1],
         [50,2,4,-1],
         [50,3,5,10],
         [50,4,6,-1],
         [50,5,7,-1],
         [50,6,8,-1],
         [50,7,9,-1],
         [50,8,-1,-1],
         [50,4,11,-1],
         [50,10,12,-1],
         [50,11,13,-1],
         [50,12,14,-1],
         [50,13,-1,-1]
        ]
        
        # Green Line Block Information
        green_block_info = [ # block length (m), block speed limit (km/hr), next-block-index (-1 if none),bidirectional-block-index (-1 if none), switch-neighbor-index (-1 if none)
         [100,55,12,-1,-1], # Section A (Unidirectional)
         [100,55,0,-1,-1],
         [100,55,1,-1,-1],
         [100,55,2,-1,-1], # Section B (Unidirectional)
         [100,55,3,-1,-1],
         [100,55,4,-1,-1],
         [100,55,5,-1,-1], # Section C (Unidirectional)
         [100,55,6,-1,-1],
         [100,55,7,-1,-1],
         [100,55,8,-1,-1],
         [100,55,9,-1,-1],
         [100,55,10,-1,-1],
         [150,70,11,13,-1], # Section D (Bidirectional)
         [150,70,12,14,-1],
         [150,70,13,15,-1],
         [150,70,14,16,-1],
         [150,60,15,17,-1], # Section E (Bidirectional)
         [150,60,16,18,-1],
         [150,60,17,19,-1],
         [150,60,18,20,-1],
         [300,70,19,21,-1], # Section F (Bidirectional)
         [300,70,20,22,-1],
         [300,70,21,23,-1],
         [300,70,22,24,-1],
         [200,70,23,25,-1],
         [100,70,24,26,-1],
         [50,70,25,27,-1],
         [50,70,26,28,-1],
         [50,70,29,-1,-1], # Section G (Unidirectional)
         [50,70,30,-1,-1],
         [50,70,31,-1,-1],
         [50,70,32,-1,-1],
         [50,70,33,-1,-1], # Section H (Unidirectional)
         [50,70,34,-1,-1],
         [50,70,35,-1,-1],
         [50,70,36,-1,-1], # Section I (Unidirectional)
         [50,70,37,-1,-1],
         [50,70,38,-1,-1],
         [50,70,39,-1,-1],
         [50,70,40,-1,-1],
         [50,70,41,-1,-1],
         [50,70,42,-1,-1],
         [50,70,43,-1,-1],
         [50,70,44,-1,-1],
         [50,70,45,-1,-1],
         [50,70,46,-1,-1],
         [50,70,47,-1,-1],
         [50,70,48,-1,-1],
         [50,70,49,-1,-1],
         [50,70,50,-1,-1],
         [50,70,51,-1,-1],
         [50,70,52,-1,-1],
         [50,70,53,-1,-1],
         [50,70,54,-1,-1],
         [50,70,55,-1,-1],
         [50,70,56,-1,-1],
         [50,70,57,-1,-1],
         [50,60,58,-1,-1], # Section J (Unidirectional) (To Yard)
         [50,60,59,-1,-1],
         [50,60,60,-1,-1],
         [50,60,61,-1,-1],
         [50,60,62,-1,-1], # (From Yard)
         [100,70,63,-1,-1], # Section K (Unidirectional)
         [100,70,64,-1,-1], 
         [200,70,65,-1,-1], 
         [200,70,66,-1,-1], 
         [100,70,67,-1,-1], 
         [100,70,68,-1,-1], 
         [100,60,69,-1,-1], # Section L (Unidirectional) 
         [100,60,70,-1,-1], 
         [100,60,71,-1,-1], 
         [100,60,72,-1,-1], 
         [100,60,73,-1,-1],
         [100,60,74,-1,-1], # Section M (Unidirectional)
         [100,60,75,-1,-1],
         [100,60,76,-1,-1],
         [300,70,100,77,-1], # Section N (Bidirectional)
         [300,70,76,78,-1],
         [300,70,77,79,-1],
         [300,70,78,80,-1],
         [300,70,79,81,-1],
         [300,70,80,82,-1],
         [300,70,81,83,-1],
         [300,70,82,84,-1],
         [300,70,83,85,-1],
         [100,55,86,-1,-1], # Section O (Unidirectional)
         [86.6,55,87,-1,-1],
         [100,55,88,-1,-1],
         [75,55,89,-1,-1], # Section P (Unidirectional)
         [75,55,90,-1,-1],
         [75,55,91,-1,-1],
         [75,55,92,-1,-1],
         [75,55,93,-1,-1],
         [75,55,94,-1,-1],
         [75,55,95,-1,-1],
         [75,55,96,-1,-1],
         [75,55,97,-1,-1],
         [75,55,98,-1,-1], # Section Q (Unidirectional)
         [75,55,99,-1,-1],
         [75,55,84,-1,-1],
         [35,55,101,-1,-1], # Section R (Unidirectional)
         [100,60,102,-1,-1], # Section S (Unidirectional)
         [100,60,103,-1,-1],
         [80,60,104,-1,-1],
         [100,60,105,-1,-1], # Section T (Unidirectional)
         [100,60,106,-1,-1],
         [90,60,107,-1,-1],
         [100,60,108,-1,-1],
         [100,60,109,-1,-1],
         [100,70,110,-1,-1], # Section U (Unidirectional)
         [100,70,111,-1,-1],
         [100,70,112,-1,-1],
         [100,70,113,-1,-1],
         [162,70,114,-1,-1],
         [100,70,115,-1,-1],
         [100,70,116,-1,-1],
         [50,60,117,-1,-1], # Section V (Unidirectional)
         [50,60,118,-1,-1],
         [40,60,119,-1,-1],
         [50,60,120,-1,-1],
         [50,60,121,-1,-1],
         [50,70,122,-1,-1], # Section W (Unidirectional)
         [50,70,123,-1,-1],
         [50,70,124,-1,-1],
         [50,70,125,-1,-1],
         [50,70,126,-1,-1],
         [50,70,127,-1,-1],
         [50,70,128,-1,-1],
         [50,70,129,-1,-1],
         [50,70,130,-1,-1],
         [50,70,131,-1,-1],
         [50,70,132,-1,-1],
         [50,70,133,-1,-1],
         [50,70,134,-1,-1],
         [50,70,135,-1,-1],
         [50,70,136,-1,-1],
         [50,70,137,-1,-1],
         [50,70,138,-1,-1],
         [50,70,139,-1,-1],
         [50,70,140,-1,-1],
         [50,70,141,-1,-1],
         [50,70,142,-1,-1],
         [50,70,143,-1,-1],
         [50,70,144,-1,-1], # Section X (Unidirectional)
         [50,70,145,-1,-1],
         [50,70,146,-1,-1],
         [50,70,147,-1,-1], # Section Y (Unidirectional)
         [184,70,148,-1,-1],
         [40,70,149,-1,-1],
         [35,70,27,-1,-1], # Section Z (Unidirectional)
        ]
        
        # Green-track station information
        green_station_info = [
         TrainStation([1],[[8,7,6,5,4,3,2]]), # Edgebrook
         TrainStation([2],[[1,0,12,13,14]]), # Pioneer
         TrainStation([0,3],[[15,14,13,12,11,10,9],[15,16,17,18,19,20]]), # Falcon
         TrainStation([2,4],[[21,20,19,18,17,16],[21,22,23,24,25,26,27,28,29]]), # Whited
         TrainStation([5],[[30,31,32,33,34,35,36,37]]), # South Bank
         TrainStation([3,6],[[140,141,142,143,144,145,146,147,148,149,28,27,26,25,24,23,22],[38,39,40,41,42,43,44,45,46]]), # Central
         TrainStation([5,7],[[131,132,133,134,135,136,137,138,139],[47,48,49,50,51,52,53,54,55]]), # Inglewood
         TrainStation([6,8,14],[[122,123,124,125,126,127,128,129,130],[56,57,58,59,60,61],[56,57]]), # Overbrook
         TrainStation([9],[[62,63]]), # From Yard
         TrainStation([7,10],[[113,114,115,116,117,118,119,120,121],[64,65,66,67,68,69,70,71]]), # Glenbury
         TrainStation([9,11],[[104,105,106,107,108,109,110,111,112],[72,73,74,75]]), # Dormont
         TrainStation([10,12],[[76,100,101,102,103],[76,77,78,79,80,81,82,83,84,85,86]]), # Mt Lebanon
         TrainStation([13],[[87,88,89,90,91,92,93,94]]), # Poplar
         TrainStation([11],[[95,96,97,98,99,84,83,82,81,80,79,78,77]]), # Castle Shannon
        ] # Station-index Block-index position
        
        
        green_station_pathway = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,11,10,9,7,6,5,3,2] 
        
        
        # Green Line Block Information
        red_block_info = [ # block length (m), block speed limit (km/hr), next-block-index (-1 if none),bidirectional-block-index (-1 if none), switch-neighbor-index (-1 if none)
         [50,40,15,1,-1], # Section A (Bidirectional)
         [50,40,0,2,-1],
         [50,40,1,3,-1],
         [50,40,2,4,-1], # Section B (Bidirectional)
         [50,40,3,5,-1],
         [50,40,4,6,-1],
         [75,40,5,7,-1], # Section C (Bidirectional)
         [75,40,6,8,-1],
         [75,40,7,9,-1],
         [75,40,8,10,-1], # Section D (Bidirectional)
         [75,40,9,11,-1],
         [75,40,10,12,-1],
         [70,40,11,13,-1], # Section E (Bidirectional)
         [60,40,12,14,-1],
         [60,40,13,15,-1],
         [50,40,14,16,0], # Section F (Bidirectional)
         [200,55,15,17,-1],
         [400,70,16,18,-1],
         [400,70,17,19,-1],
         [200,70,18,20,-1],
         [100,55,19,21,-1], # Section G (Bidirectional)
         [100,55,20,22,-1],
         [100,55,21,23,-1],
         [50,70,22,24,-1], # Section H (Bidirectional)
         [50,70,23,25,-1],
         [50,70,24,26,-1],
         [50,70,25,27,75],
         [50,70,26,28,-1],
         [60,70,27,29,-1],
         [60,70,28,30,-1],
         [50,70,29,31,-1],
         [50,70,30,32,71],
         [50,70,31,33,-1],
         [50,70,32,34,-1],
         [50,70,33,35,-1],
         [50,70,34,36,-1],
         [50,70,35,37,-1],
         [50,70,36,38,70],
         [50,70,37,39,-1],
         [60,70,38,40,-1],
         [60,70,39,41,-1],
         [50,70,40,42,-1],
         [50,70,41,43,66],
         [50,70,42,44,-1],
         [50,70,43,45,-1],
         [75,70,44,46,-1], # Section I (Bidirectional)
         [75,70,45,47,-1],
         [75,70,46,48,-1],
         [50,60,47,49,-1], # Section J (Bidirectional)
         [50,60,48,50,-1],
         [50,55,49,51,-1],
         [43.2,55,50,52,65],
         [50,55,51,53,-1],
         [50,55,52,54,-1],
         [75,55,53,55,-1], # Section K (Bidirectional)
         [75,55,54,56,-1],
         [75,55,55,57,-1],
         [75,55,56,58,-1], # Section L (Bidirectional)
         [75,55,57,59,-1],
         [75,55,58,60,-1],
         [75,55,59,61,-1], # Section M (Bidirectional)
         [75,55,60,62,-1],
         [75,55,61,63,-1],
         [75,55,62,64,-1], # Section N (Bidirectional)
         [75,55,63,65,-1],
         [75,55,64,51,-1],
         [50,55,42,67,-1], # Section O (Bidirectional)
         [50,55,66,68,-1], # Section P (Bidirectional)
         [50,55,67,69,-1],
         [50,55,68,70,-1],
         [50,55,69,37,-1], # Section Q (Bidirectional)
         [50,55,31,72,-1], # Section R (Bidirectional)
         [50,55,71,73,-1], # Section S (Bidirectional)
         [50,55,72,74,-1],
         [50,55,73,75,-1],
         [50,55,74,26,-1] # Section T (Bidirectional)
        ]
        
        
        # Red track station information
        red_station_info = [
         TrainStation([1,2],[[6,7],[6,5,4,3,2,1,0]]), # Shadyside
         TrainStation([0,2],[[8,7],[8,9,10,11,12,13,14]]), # Yard
         TrainStation([0,1,3],[[15,14,13,12,11,10,9],[15,0,1,2,3,4,5],[15,16,17,18,19]]), # Herron Ave
         TrainStation([2,4],[[20,19,18,17,16],[20,21,22,23]]), # Swissville
         # Add Extra Cases where the path goes through the alt tracks
         TrainStation([3,5],[[24,23,22,21],[24,25,26,27,28,29,30,31,32,33]]), # Penn Station
         TrainStation([4,6],[[34,33,32,31,71,72,73,74,75,26,25],[34,35,36,37,38,39,40,41,42,43]]), # Steel Plaza
         TrainStation([5,7],[[44,43,42,66,67,68,69,70,37,36,35],[44,45,46]]), # First Ave
         #
         TrainStation([6,8],[[47,46,45],[47,49,50,51,52,53,54,55,56,57,58]]), # Station Square
         TrainStation([7],[[59,60,61,62,63,64,65,51,50,49,48]]), # South Hills Junction
         
        ] # Station-index Block-index position
        
        red_station_pathway = [2,1,0,2,3,4,5,6,7,8,7,6,5,4,3] 
        
        
        self.ui.model = TableModel(global_schedule_display,header)
        
        
        
        
        self.ui.tableView_schedule.setModel(self.ui.model)
        
        self.ui.tableView_schedule.hideRow(0)

        
        
        #draw track code start
        #scene = QtWidgets.QGraphicsScene()
        #self.ui.graphicsView.setScene(scene)
        #pen = QtGui.QPen(QtCore.Qt.black)

        #i = 0
        #s = 0
        #x = -800
        
        #r=QtCore.QRectF(x,0,60,30)
        #scene.addRect(r,pen)
        
        
        #while i <= len(track)-1:
        #    if track[i].station != 0:
        #        pen = QtGui.QPen(QtCore.Qt.red)
        #        r=QtCore.QRectF(x,-32,60,30)
        #        scene.addRect(r,pen)
        #        
        #    elif track[i].switch !=0:
        #        s = track[i].switch-1
        #        check = s
        #        flag = 0
        #        
        #        i = i+1
        #        
        #        while 1:#track[i].switch == 0 and track[s].switch == 0:
        #            if i > check or s >= len(track):
        #                i = s
        #                break;
        #            #top
        #            x = upX(x)
        #                
        #            r=QtCore.QRectF(x,-40,60,30)
        #            scene.addRect(r,pen)
        #            
        #            #check if top station
        #            if track[i].station != 0:
        #                pen = QtGui.QPen(QtCore.Qt.red)
        #                r=QtCore.QRectF(x,-72,60,30)
        #                scene.addRect(r,pen)
        #                pen = QtGui.QPen(QtCore.Qt.black)
        #            
        #            #bottom block
        #            r=QtCore.QRectF(x,40,60,30)
        #            scene.addRect(r,pen)
        #            
        #            #check for bottom station
        #            if track[s].station != 0:
        #                pen = QtGui.QPen(QtCore.Qt.red)
        #                r=QtCore.QRectF(x,72,60,30)
        #                scene.addRect(r,pen)
        #                pen = QtGui.QPen(QtCore.Qt.black) 
        #                                
        #            i = i + 1
        #            s = s + 1
            #add block
        #    if i+1 < len(track):
        #        x = upX(x)
        #        pen = QtGui.QPen(QtCore.Qt.black)
        #        r=QtCore.QRectF(x,0,60,30)
        #        scene.addRect(r,pen)
        #        
        #    i = i + 1
        
        #r=QtCore.QRectF(0,0,60,30)
        #scene.addRect(r,pen)
        
        
        
        #draw track code end
        




        # ui.setCentralWidget(self.table)
        
        # ui.tableView_schedule.setModel(data)
        # self.tableView_schedule.data = data
        # self.tableView_schedule.setData()
        # self.tableView_schedule.resizeColumnsToContents()
        # self.tableView_schedule.resizeRowsToContents()
        # Connect "add" button with a custom function (addInputTextToListbox)
        
        # ui.pushButton.clicked.connect(lambda: self.change_data(ui))
        # ui.pushButton_7.clicked.connect(lambda: self.change_combobox(ui))
        # ui.pushButton_6.clicked.connect(lambda: self.change_throughput(ui,test_throughput))
        
        # -----------------------------
        # DISPATCH ACTIONS
        # -----------------------------
        
        # Manually dispatch train into the system (GREEN LINE)
        self.ui.btnDispatchMan.clicked.connect(lambda: self.dispatch_manual(self.ui,green_block_info,green_station_info,green_station_pathway,current_time))        
        
        # Choose file for automatic dispatch (GREEN LINE)
        self.ui.btnImportSchedFile.clicked.connect(lambda: self.import_schedule_file(self.ui))
        
        # Automatically dispatch train into the system (GREEN LINE)
        self.ui.btnDispatchAuto.clicked.connect(lambda: self.dispatch_automatic(self.ui,green_block_info,green_station_info,green_station_pathway,current_time))        
        
        # NEED TO IMPLEMENT
        # Manually dispatch train into the system (RED LINE)
        self.ui.btnDispatchMan_2.clicked.connect(lambda: self.dispatch_manual(self.ui,red_block_info,red_station_info,red_station_pathway,current_time))        
        
        # NEED TO IMPLEMENT
        # Choose file for automatic dispatch (RED LINE)
        self.ui.btnImportSchedFile_2.clicked.connect(lambda: self.import_schedule_file(self.ui))
        
        # NEED TO IMPLEMENT
        # Automatically dispatch train into the system (RED LINE)
        self.ui.btnDispatchAuto_2.clicked.connect(lambda: self.dispatch_automatic(self.ui,red_block_info,red_station_info,red_station_pathway,current_time))        
        
        
        # -----------------------------
        # MAINTENANCE ACTIONS
        # -----------------------------
        
        # Display information on the default block/switch chosen
        #self.display_state_switch(self.ui,current_track_occupancy)
        #self.display_state_block(self.ui,current_track_occupancy)
        
        # Send a switch maintenance request
        self.ui.btnToggleSwitch.clicked.connect(lambda: self.send_maintenance_request_switch(self.ui,current_track_occupancy))
        
        # Send a block maintenance request
        self.ui.btnToggleBlock.clicked.connect(lambda: self.send_maintenance_request_block(self.ui,current_track_occupancy))

        # Update display of current switch state
        #self.ui.comboBlock.currentIndexChanged.connect(lambda: self.display_state_switch(self.ui,current_track_occupancy))
        
        # Update display of current block state
        #self.ui.comboBlock.currentIndexChanged.connect(lambda: self.display_state_block(self.ui,current_track_occupancy))
       
       
        # -----------------------------
        # SIGNAL ACTIONS
        # -----------------------------
        
        signals.time.connect(self.update_time)
        signals.time.connect(lambda: self.send_dispatch_order())
        signals.time.connect(lambda: self.update_ctc_displays(self.ui))
        signals.way_green_occupancy_ctc.connect(self.update_order_authority)
        signals.way_red_occupancy_ctc.connect(self.update_order_authority)
        
            
    def change_data(self, ui):
        #print("In Data Def")
        # ui = Ui_MainWindow()
        # ui.setupUi(MainWindow)
        
        new_data = [
          [4, 9, 2]
        ]
        
        header = ['Train', 'Destination Station', 'Arrival Time (2400)']
        
        ui.model = TableModel(new_data, header)
        ui.tableView_schedule.setModel(ui.model)
        
    def change_combobox(self,ui):
        #print("In Combobox Def")
        _translate = QtCore.QCoreApplication.translate
        
        # ui = Ui_MainWindow()
        # ui.setupUi(MainWindow)
        ui.comboBox_6.addItem("TestTestTest1")
        ui.comboBox_6.addItem("TestTestTest2")
        
    def change_throughput(self,ui,throughput):
        #print("In change_thoughput")
        ui.label_19.setText(str(throughput))
        throughput += 50
        
    def send_maintenance_request_switch(self, ui, track_occ):
        request_str = ["g","s"]
        toggle_position = ui.comboSwitch.currentIndex()
        for i in range(ui.comboSwitch.count()):
            if i == toggle_position:
                request_str.append("1")
            else:
                request_str.append("0")
        signals.ctc_maintenance.emit(request_str)
        #print("Sending To Wayside Controller:")
        #print(request_str)
        #print("")

    def send_maintenance_request_block(self, ui, track_occ):
        request_str = ["g","b"]
        toggle_position = ui.comboBlock.currentIndex()
        for i in range(ui.comboBlock.count()):
            if i == toggle_position:
                request_str.append("1")
            else:
                request_str.append("0")
        signals.ctc_maintenance.emit(request_str)
       # print("Sending To Wayside Controller:")
        #print(request_str)
        #print("")

    #def display_state_switch(self,ui,track_occ):
    #    display_curr_str = ""
    #    display_next_str = ""
    #    switch_position = ui.comboBlock.count() + ui.comboSwitch.currentIndex()
        #if track_occ[switch_position] == "0":
        #    display_curr_str += "To Block 6"
        #    display_next_str += "To Block 11"
        #else:
        #    display_curr_str += "To Block 11"
        #    display_next_str += "To Block 6" 
        #ui.labelCurrSwitchPos.setText(display_curr_str)
        #ui.labelNewSwitchPos.setText(display_next_str)

    #def display_state_block(self,ui,track_occ):
    #    display_curr_str = ""
    #    display_next_str = ""
    #    block_position = ui.comboBlock.currentIndex()
    #    if track_occ[block_position] == "0":
    #        display_curr_str += "Unoccupied"
    #        display_next_str += "Occupied"
    #    else:
    #        display_curr_str += "Occupied"
    #        display_next_str += "Unoccupied"
        #ui.labelCurrBlockPos.setText(display_curr_str)
        #ui.labelNewBlockPos.setText(display_next_str)
        
    def dispatch_manual(self,ui,test_block_info,test_station_info,test_station_pathway,current_time):
        global global_dispatch_orders
        global global_order_path_hold
        global global_dispatched_trains
        global global_train_blocks
        
        global_order_path_hold = []
        ui.labelManError.setText("")
        # Dispatch a train using values inputted in the main window
        
        # Get info inputted in the main window
        if len(test_block_info) == 150:
            train = ui.comboTrain.currentIndex()
            destination_station = ui.comboStation.currentIndex()
            arrival_time = ui.lineEditTime.text()
        else:
            train = ui.comboTrain_2.currentIndex()
            destination_station = ui.comboStation_2.currentIndex()
            arrival_time = ui.lineEditTime_2.text()
        # print(train)
        # print(destination_station)
        # print(arrival_time)
        
        if arrival_time == "":
            ui.labelManError.setText("*Please input arrival time.")
            return
        
        # Calculate initial authority and suggested speed
        train_metrics = self.calculate_train_metrics(test_block_info,test_station_info,test_station_pathway,train,destination_station,arrival_time,current_time)
        #print(train_metrics[0])
        #print(train_metrics[1])
        
        # valid_train_metrics = [authority, suggested_speed, start_time]
        valid_train_metrics = self.validate_dispatch(ui,train_metrics,train,current_time,arrival_time,test_block_info,test_station_info)
        
        #print("Initial Values")
        #print(valid_train_metrics[0])
        #print(valid_train_metrics[1])
        #print(valid_train_metrics[2])
        
        # validate_dispatch() will make suggested_speed = -1 if dispatch is invalid
        # Otherwise, it will adjust the train_metrics to make sure it is valid
        if valid_train_metrics[1] != [-1] and valid_train_metrics[0] != [-1]:
            if ui.comboTrain.currentIndex() == 0:
                global_dispatched_trains = global_dispatched_trains + 1
                valid_train_name = "Train " + str(global_dispatched_trains)
                if len(test_block_info) == 150:
                    ui.comboTrain.addItem(valid_train_name)
                else:
                    ui.comboTrain_2.addItem(valid_train_name)
                    
                global_expected_train_location.append(global_expected_train_location_hold)
                
            else:
                if len(test_block_info) == 150:
                    valid_train_name = ui.comboTrain.currentText()
                else:
                    valid_train_name = ui.comboTrain_2.currentText()
                global_expected_train_location[int(train)] = global_expected_train_location_hold
            # for i in global_expected_train_location:
                    # print(i)
            if len(test_block_info) == 150:
                global_schedule_display.append([valid_train_name,ui.comboStation.currentText(),arrival_time])
            else:
                global_schedule_display.append([valid_train_name,ui.comboStation_2.currentText(),arrival_time])
            header = ['Train', 'Destination Station', 'Arrival Time (2400)']
            ui.model = TableModel(global_schedule_display, header)
            ui.tableView_schedule.setModel(ui.model)
            # for i in global_order_path_hold:
            #     print(i)
            
            if len(test_block_info) == 150:
                fin_destination_station = ui.comboStation.currentText()
                lin_spec = "g"
            else:
                fin_destination_station = ui.comboStation_2.currentText()
                lin_spec = "r"
                
            if (test_block_info[valid_train_metrics[0][-1]][2] != -1 and test_block_info[valid_train_metrics[0][-1]][2] != valid_train_metrics[0][-2]):
                fin_dest_block = test_block_info[valid_train_metrics[0][-1]][2]
            elif (test_block_info[valid_train_metrics[0][-1]][3] != -1 and test_block_info[valid_train_metrics[0][-1]][3] != valid_train_metrics[0][-2]):
                fin_dest_block = test_block_info[valid_train_metrics[0][-1]][3]
            elif (test_block_info[valid_train_metrics[0][-1]][4] != -1 and test_block_info[valid_train_metrics[0][-1]][4] != valid_train_metrics[0][-2]):
                fin_dest_block = test_block_info[valid_train_metrics[0][-1]][4]
            else:
                fin_dest_block = -1
            
            #print(valid_train_name + " = " + str(valid_train_metrics[0]))
            
            global_dispatch_orders.append([valid_train_name,fin_destination_station,self.military_to_seconds(str(arrival_time)),valid_train_metrics[2],valid_train_metrics[0],valid_train_metrics[1],lin_spec,fin_dest_block])
            
            
            #print(valid_train_metrics[0])
            #print(valid_train_metrics[1])
            #print(valid_train_metrics[2])
            
            # [Train Name, Destination Station, Arrival Time(seconds),Start Time(seconds) Authority(meters), Suggested Speed(meters/second), Order Path]
            #print("Train Name: " + global_dispatch_orders[len(global_dispatch_orders)-1][0])
            # print("Destination Station: " + global_dispatch_orders[len(global_dispatch_orders)-1][1])
            # print("Arrival Time: " + str(global_dispatch_orders[len(global_dispatch_orders)-1][2]))
            # print("Start Time: " + str(global_dispatch_orders[len(global_dispatch_orders)-1][3]))
            #print("Authority: " + str(global_dispatch_orders[len(global_dispatch_orders)-1][4]) + " meters")
            #print("Suggested Speed: " + str(global_dispatch_orders[len(global_dispatch_orders)-1][5]) + " meters/second")
            #print("")
            # order_path_string = ""
            # for i in global_dispatch_orders[len(global_dispatch_orders)-1][6]:
            #     order_path_string += str(i) + " "
            # print("Order Path: [ " + order_path_string + "]")
        else:
            
            if len(test_block_info) == 150:
                ui.labelManError.setText("*Invalid Dispatch.")
            else:
                ui.labelManError_2.setText("*Invalid Dispatch.")
            return
            
        #print(global_expected_train_location)
            # Put the dispatch in the system internally and display it on the "Schedule" Tab
        #     print("It's a working dispatch")
        # else:
            
            # Tell the user that the inputted dispatch cannot work
        #     print("It's not a working dispatch")
            
    def calculate_train_metrics(self,test_block_info,test_station_info,test_station_pathway,train,destination_station,arrival_time,current_time):
        global global_expected_train_location
        global global_expected_train_location_hold
        # Calculate authority (distance from the start position to end position)
        
        # Assume start station is index 8
        if train == 0:
            if len(test_block_info) == 150:
                curr_station_path = 8
            else:
                curr_station_path = 1
        else:
            curr_station_path = global_expected_train_location[train]
        # print(curr_block)
        #print ("Current_statiion = " + str(curr_station_path))
        
        exp_dest_path_hold = curr_station_path
        
        while test_station_pathway[exp_dest_path_hold] != destination_station:
            if exp_dest_path_hold == len(test_station_pathway) -1:
                exp_dest_path_hold = 0
            else:
                exp_dest_path_hold = exp_dest_path_hold + 1
        
        global_expected_train_location_hold = exp_dest_path_hold
        
        
        
        
        # if train != 0:
            # Start at the chosen train's position once all its dispatch orders are fulfilled
            # print("An existing train was chosen")
        # print(end_block)
        authority = self.find_authority([],curr_station_path,destination_station,test_station_info,test_station_pathway)

        global global_order_path_hold
        global_order_path_hold = authority 

        # print("Authority: " + str(authority))
        
        # Calculate suggested speed
        arrival_time_seconds = self.military_to_seconds(str(arrival_time))
        suggested_speed = self.find_suggested_speed(authority,0.75,test_block_info)
        # print("Suggested Speed: " + str(suggested_speed))
        
        # print(authority)
        # print(suggested_speed)
        
        return [authority,suggested_speed]
        
    def military_to_seconds(self,military_time):
        # Given a string containing military time, output the corresponding seconds passed
        return int(60*(60*int(military_time[:2]) + int(military_time[-2:])))
        
    def kmph_to_mps(self,kmph):
        return (5/18)*kmph
      
    def find_suggested_speed(self,authority,speed_mod,track_info):
        sugg_speed = []
        for i in range(len(authority)):
            sugg_speed.append(self.kmph_to_mps(speed_mod*track_info[authority[i]][1]))
        
        # Slow down speed as the train reaches destination
        if len(sugg_speed) >= 3:
            sugg_speed[-3] = 4
        if len(sugg_speed) >= 2:
            sugg_speed[-2] = 4
        if len(sugg_speed) >= 1:
            sugg_speed[-1] = 4
        
        return sugg_speed
        
    def find_start_time(self,authority,sugg_speed,arrival_time,track_info):
        dispatch_time = 0
        
        #print("Authority: " + str(authority))
        #print("Sugg Speed: " + str(sugg_speed))
        for i in range(len(authority)):
            dispatch_time += (track_info[authority[i]][0])/(sugg_speed[i])
        
        return math.ceil(arrival_time - dispatch_time)
        
    def find_authority(self,curr_auth,curr_station_path,destination_station,test_station_info,test_station_pathway):
        global global_order_path_hold
        # print("")
        # print("Current block index: " + str(curr_block))
        # print("Current authority: " + str(authority))
        
        curr_station = test_station_pathway[curr_station_path]
        # print("Current Station: " + str(curr_station))
        # print(curr_auth)
        
        #print("Current Path")
        #print(curr_auth)
        
        if curr_station == destination_station:
            return curr_auth
        if len(curr_auth) > 200:
            # Chose 200 for no good reason, choose a better number later
            #print("EXCEED SIZE")
            return [-1]

        if curr_station_path == len(test_station_pathway) -1:
            next_station_path = 0
        else:
            next_station_path = curr_station_path + 1
        
        next_station = test_station_pathway[next_station_path]

        res_auth = []

        for i in range(len(test_station_info[curr_station].conn_index)):
            if test_station_info[curr_station].conn_index[i] == next_station:
                res_index = len(res_auth)
                res_auth.append([])
                res_auth[res_index] = self.find_authority((curr_auth + test_station_info[curr_station].connections[i]),next_station_path,destination_station,test_station_info,test_station_pathway)

        final_auth = [-1]
        
        #print("res_auth:")
        #print(res_auth)
        
        for i in res_auth:
            if i != [-1] and i != []:
                if final_auth == [-1]:
                    final_auth = i
                if len(i) < len(final_auth):
                    final_auth = i

        
        return final_auth
    
        # if block_info[curr_block][1] != -1 and block_info[curr_block][1] != prev_block:
            # print("Block Index " + str(curr_block) + " can go left!")
        #     samp_authority1 = self.find_authority(curr_block,block_info[curr_block][1],dest_block,authority+block_info[curr_block][0],block_info)
        # else:
        #     samp_authority1 = -1
            # print("Block Index " + str(curr_block) + " CANNOT go left!")
        # if block_info[curr_block][2] != -1 and block_info[curr_block][2] != prev_block:
            # print("Block Index " + str(curr_block) + " can go right!")
        #     samp_authority2 = self.find_authority(curr_block,block_info[curr_block][2],dest_block,authority+block_info[curr_block][0],block_info)
        # else:
        #     samp_authority2 = -1
            # print("Block Index " + str(curr_block) + " CANNOT go right!")
        # if block_info[curr_block][3] != -1 and block_info[curr_block][3] != prev_block:
            # print("Block Index " + str(curr_block) + " can go switch!")
        #     samp_authority3 = self.find_authority(curr_block,block_info[curr_block][3],dest_block,authority+block_info[curr_block][0],block_info)
        # else:
        #     samp_authority3 = -1
            # print("Block Index " + str(curr_block) + " CANNOT go switch!")
            

        # print("Block Index " + str(curr_block) + " returning: " + str((samp_authority1 + samp_authority2 + samp_authority3) + 2))
        # if (samp_authority1 + samp_authority2 + samp_authority3) + 2 != -1:
        #     global_order_path_hold.append(curr_block)
        # return (samp_authority1 + samp_authority2 + samp_authority3) + 2
        
    def validate_dispatch(self,ui,initial_train_metrics,train,current_time,arrival_time,test_block_info,test_station_info):
        global global_order_path_hold
        global global_dispatch_orders
        global global_expected_train_location
        # Outputs new_train_metrics[authority,suggested_speed,start_time]
        authority = initial_train_metrics[0]
        suggested_speed = initial_train_metrics[1]
        min_start_time = current_time
        if authority == [-1]:
            return [authority,suggested_speed,min_start_time]
        
        
        if len(test_block_info) == 150:
            curr_station_path = 8
        else:
            curr_station_path = 1
        # check if the current train has a dispatch outgoing
        #for i in global_dispatch_orders:
        #    if train != 0 and ui.comboTrain.itemText(train) == i[0] and len(global_expected_train_location) < train:
        #        # make the start time equal to the last dispatch arrival time + 60 seconds
        #        min_start_time = i[2] + 60
        #        # print("TRAIN IS OUT BEFORE! NEW START TIME: " + str(start_time))
        #        # print("NEW SUGGESTED SPEED: " + str(suggested_speed))
        
        for order_num in global_dispatch_orders:
            if order_num[0] != "" and train == int(order_num[0].rsplit(' ', 1)[1]):
                min_start_time = order_num[2] + 60
                
        
        isValid = True
        
        # for i in global_expected_train_location:
        #     if i != global_expected_train_location[0]:
        #         if i == global_order_path_hold[len(global_order_path_hold)-1]:
        #             return [authority,-1,start_time]
        temp_speed_mod = 1.05
           
        while temp_speed_mod > 0:
            isValid = True
            

            temp_start_time = self.find_start_time(authority,suggested_speed,self.military_to_seconds(arrival_time),test_block_info)
            if temp_start_time < min_start_time:
				
                print("temp_start_time = " + str(temp_start_time))
                print("min_start_time = " + str(min_start_time))
                isValid = False
            
            if isValid:
                for i in range(temp_start_time, self.military_to_seconds(arrival_time) + 1):
                    current_block = self.find_train_position(authority,temp_start_time,suggested_speed,i,test_block_info)
                    for j in global_dispatch_orders:
                        if j[3] <= i and j[2] > i:
                            if current_block == self.find_train_position(j[4],j[3],j[5],i,test_block_info):
                                # print("There is a collision at Block")
                                isValid = False
                            
            if isValid:
                
                return [authority,suggested_speed,temp_start_time]
            else:
                temp_speed_mod -= 0.05
                suggested_speed = self.find_suggested_speed(authority,temp_speed_mod,test_block_info)
                
                # print("Train is in Block " + str(self.find_train_position(global_order_path_hold,start_time,suggested_speed,i,test_block_info)))
                
        return [authority,[-1],temp_start_time]
        
    def find_train_position(self,block_path,start_time,sugg_speed,curr_time,test_block_info):
        if start_time >= curr_time:
            return block_path[0]
        dispatch_time = curr_time - start_time
        travel_time = 0
        for i in range(len(block_path)):
            travel_time += test_block_info[block_path[i]][0]/sugg_speed[i]
            if travel_time >= dispatch_time:
                return block_path[i]
        return block_path[len(block_path)-1]

    def dispatch_automatic(self,ui,test_block_info,test_station_info,test_station_pathway,current_time):
        global global_dispatch_orders
        global global_order_path_hold
        global global_dispatched_trains
        global global_dispatch_file
        global global_schedule_display
        global global_expected_train_location
        global global_expected_train_location_hold
        
        
        
        ui.labelAutoError.setText("")
        
        if global_dispatch_file == "":
            ui.labelAutoError.setText("*Please select a file.")
            return
        
        with open(global_dispatch_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            
            if len(test_block_info) == 150:
            
                # GREEN LINE IMPLEMENTATION  
                for row in csv_reader:
                    global_order_path_hold = []
                    if line_count == 0:
                        line_count += 1
                    else:
                        
                        train_name = int(row[0].rsplit(' ', 1)[1])
                        if global_dispatched_trains < train_name:
                            train = 0
                        else:
                            train = train_name
                            
                        if row[1] == "Edgebrook":
                            destination_station = 0
                        elif row[1] == "Pioneer":
                            destination_station = 1
                        elif row[1] == "Falcon":
                            destination_station = 2
                        elif row[1] == "Whited":
                            destination_station = 3
                        elif row[1] == "South Bank":
                            destination_station = 4
                        elif row[1] == "Central":
                            destination_station = 5
                        elif row[1] == "Inglewood":
                            destination_station = 6
                        elif row[1] == "Overbrook":
                            destination_station = 7
                        elif row[1] == "Yard":
                            destination_station = 8
                        elif row[1] == "Glenbury":
                            destination_station = 9
                        elif row[1] == "Dormont":
                            destination_station = 10
                        elif row[1] == "Mt Lebanon":
                            destination_station = 11
                        elif row[1] == "Poplar":
                            destination_station = 12
                        elif row[1] == "Castle Shannon":
                            destination_station = 13
                            
                        arrival_time = row[2]
                        
                        # print(train)
                        train_metrics = self.calculate_train_metrics(test_block_info,test_station_info,test_station_pathway,train,destination_station,arrival_time,current_time)
            
            
                        valid_train_metrics = self.validate_dispatch(ui,train_metrics,train,current_time,arrival_time,test_block_info,test_station_info)
            
                        # validate_dispatch() will make suggested_speed = -1 if dispatch is invalid
                        # Otherwise, it will adjust the train_metrics to make sure it is valid
                        if valid_train_metrics[1] != [-1] and valid_train_metrics[0] != [-1]:
                            if global_dispatched_trains < train_name:
                                global_dispatched_trains = global_dispatched_trains + 1
                                valid_train_name = row[0]
                                ui.comboTrain.addItem(valid_train_name)
                                global_expected_train_location.append(global_expected_train_location_hold)
                            else:
                                valid_train_name = row[0]
                                global_expected_train_location[int(train_name)] = global_expected_train_location_hold
                            # for i in global_expected_train_location:
                                    # print(i)
                            print([row[0],row[1],row[2]])
                            global_schedule_display.append([row[0],row[1],row[2]])
                            header = ['Train', 'Destination Station', 'Arrival Time (2400)']
                            ui.model = TableModel(global_schedule_display, header)
                            ui.tableView_schedule.setModel(ui.model)
                            
                            
                            
                            if (test_block_info[valid_train_metrics[0][-1]][2] != -1 and test_block_info[valid_train_metrics[0][-1]][2] != valid_train_metrics[0][-2]):
                                fin_dest_block = test_block_info[valid_train_metrics[0][-1]][2]
                            elif (test_block_info[valid_train_metrics[0][-1]][3] != -1 and test_block_info[valid_train_metrics[0][-1]][3] != valid_train_metrics[0][-2]):
                                fin_dest_block = test_block_info[valid_train_metrics[0][-1]][3]
                            elif (test_block_info[valid_train_metrics[0][-1]][4] != -1 and test_block_info[valid_train_metrics[0][-1]][4] != valid_train_metrics[0][-2]):
                                fin_dest_block = test_block_info[valid_train_metrics[0][-1]][4]
                            else:
                                fin_dest_block = -1
                                
                            #print("Authority: " + str(valid_train_metrics[0]))
                            #print("Suggested Speed: " + str(valid_train_metrics[1]))
                            global_dispatch_orders.append([row[0],row[1],self.military_to_seconds(str(arrival_time)),valid_train_metrics[2],valid_train_metrics[0],valid_train_metrics[1],"g",fin_dest_block])
                            # [Train Name, Destination Station, Arrival Time(seconds),Start Time(seconds), Authority(meters), Suggested Speed(meters/second)]
                            #print("Train Name: " + global_dispatch_orders[len(global_dispatch_orders)-1][0])
                            # print("Destination Station: " + global_dispatch_orders[len(global_dispatch_orders)-1][1])
                            # print("Arrival Time: " + str(global_dispatch_orders[len(global_dispatch_orders)-1][2]))
                            # print("Start Time: " + str(global_dispatch_orders[len(global_dispatch_orders)-1][3]))
                            #print("Authority: " + str(global_dispatch_orders[len(global_dispatch_orders)-1][4]) + " meters")
                            #print("Suggested Speed: " + str(global_dispatch_orders[len(global_dispatch_orders)-1][5]) + " meters/second")
                            #print("")
                            # order_path_string = ""
                            # for i in global_dispatch_orders[len(global_dispatch_orders)-1][6]:
                            #     order_path_string += str(i) + " "
                            # print("Order Path: [ " + order_path_string + "]")
                        else:
                            ui.labelAutoError.setText("*NOTICE: There Was An Invalid Dispatch.")
                        # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                        # line_count += 1
            
                    
            else:
                
                # RED LINE FILE
                for row in csv_reader:
                    global_order_path_hold = []
                    if line_count == 0:
                        line_count += 1
                    else:
                        train_name = int(row[0][len(row[0]) - 1])
                        if global_dispatched_trains < train_name:
                            train = 0
                        else:
                            train = train_name
                            
                        if row[1] == "Shadyside":
                            destination_station = 0
                        elif row[1] == "Yard":
                            destination_station = 1
                        elif row[1] == "Herron Ave":
                            destination_station = 2
                        elif row[1] == "Swissville":
                            destination_station = 3
                        elif row[1] == "Penn Station":
                            destination_station = 4
                        elif row[1] == "Steel Plaza":
                            destination_station = 5
                        elif row[1] == "First Ave":
                            destination_station = 6
                        elif row[1] == "Station Square":
                            destination_station = 7
                        elif row[1] == "South Hills Junction":
                            destination_station = 8
                                
                        arrival_time = row[2]
                        
                        # print(train)
                        train_metrics = self.calculate_train_metrics(test_block_info,test_station_info,test_station_pathway,train,destination_station,arrival_time,current_time)
                        #print("Authority: " + str(train_metrics[0]))
                        #print("Suggested Speed: " + str(train_metrics[1]))
            
                        valid_train_metrics = self.validate_dispatch(ui,train_metrics,train,current_time,arrival_time,test_block_info,test_station_info)
            
                        # validate_dispatch() will make suggested_speed = -1 if dispatch is invalid
                        # Otherwise, it will adjust the train_metrics to make sure it is valid
                        if valid_train_metrics[1] != [-1] and valid_train_metrics[0] != [-1]:
                            if global_dispatched_trains < train_name:
                                global_dispatched_trains = global_dispatched_trains + 1
                                valid_train_name = row[0]
                                ui.comboTrain_2.addItem(valid_train_name)
                                global_expected_train_location.append(global_expected_train_location_hold)
                            else:
                                valid_train_name = row[0]
                                global_expected_train_location[int(train_name)] = global_expected_train_location_hold
                            # for i in global_expected_train_location:
                                    # print(i)
                            print([row[0],row[1],row[2]])
                            global_schedule_display.append([row[0],row[1],row[2]])
                            header = ['Train', 'Destination Station', 'Arrival Time (2400)']
                            ui.model = TableModel(global_schedule_display, header)
                            ui.tableView_schedule.setModel(ui.model)
                            
                            
                            if (test_block_info[valid_train_metrics[0][-1]][2] != -1 and test_block_info[valid_train_metrics[0][-1]][2] != valid_train_metrics[0][-2]):
                                fin_dest_block = test_block_info[valid_train_metrics[0][-1]][2]
                            elif (test_block_info[valid_train_metrics[0][-1]][3] != -1 and test_block_info[valid_train_metrics[0][-1]][3] != valid_train_metrics[0][-2]):
                                fin_dest_block = test_block_info[valid_train_metrics[0][-1]][3]
                            elif (test_block_info[valid_train_metrics[0][-1]][4] != -1 and test_block_info[valid_train_metrics[0][-1]][4] != valid_train_metrics[0][-2]):
                                fin_dest_block = test_block_info[valid_train_metrics[0][-1]][4]
                            else:
                                fin_dest_block = -1
                            
                            #print("Authority: " + str(valid_train_metrics[0]))
                            #print("Suggested Speed: " + str(valid_train_metrics[1]))
                            global_dispatch_orders.append([row[0],row[1],self.military_to_seconds(str(arrival_time)),valid_train_metrics[2],valid_train_metrics[0],valid_train_metrics[1],"r",fin_dest_block])
                            # [Train Name, Destination Station, Arrival Time(seconds),Start Time(seconds), Authority(meters), Suggested Speed(meters/second)]
                            #print("Train Name: " + global_dispatch_orders[len(global_dispatch_orders)-1][0])
                            # print("Destination Station: " + global_dispatch_orders[len(global_dispatch_orders)-1][1])
                            # print("Arrival Time: " + str(global_dispatch_orders[len(global_dispatch_orders)-1][2]))
                            # print("Start Time: " + str(global_dispatch_orders[len(global_dispatch_orders)-1][3]))
                            #print("Authority: " + str(global_dispatch_orders[len(global_dispatch_orders)-1][4]) + " meters")
                            #print("Suggested Speed: " + str(global_dispatch_orders[len(global_dispatch_orders)-1][5]) + " meters/second")
                            #print("")
                            # order_path_string = ""
                            # for i in global_dispatch_orders[len(global_dispatch_orders)-1][6]:
                            #     order_path_string += str(i) + " "
                            # print("Order Path: [ " + order_path_string + "]")
                        else:
                            
                            ui.labelAutoError_2.setText("*NOTICE: There Was An Invalid Dispatch.")
                        # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                        # line_count += 1
            
                    
            
            
        # Dispatch a train using values inputted in the main window
        
        # Get info inputted in the main window
        # print(train)
        # print(destination_station)
        # print(arrival_time)
        
        #Calculate initial authority and suggested speed
        
            # Put the dispatch in the system internally and display it on the "Schedule" Tab
        #     print("It's a working dispatch")
        # else:
            
            # Tell the user that the inputted dispatch cannot work
        #     print("It's not a working dispatch")

    def send_example_data(self):
        ["Train 1","Dormont",120,0,[150,61,62,63,64,65,66,67,68,69,70,71,72],[13,13,13,13,13,13,13,13,13,13,13,13,13]]
        

    def import_schedule_file(self,ui):
        global global_dispatch_file
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        ui.labelSchedFile.setText(str(file_path).split('/')[len(str(file_path).split('/')) - 1])
        ui.labelSchedFile_2.setText(str(file_path).split('/')[len(str(file_path).split('/')) - 1])
        global_dispatch_file = str(file_path)
        
        
    def send_dispatch_order(self):
        global global_dispatch_orders
        
        make_green_train = False
        make_red_train = False
        
        sendable_sugg_speed_green = [0] * 151
        sendable_sugg_speed_green[0] = "g"
        sendable_auth_green = [0] * 151
        sendable_auth_green[0] = "g"
        
        sendable_sugg_speed_red = [0] * 77
        sendable_sugg_speed_red[0] = "r"
        sendable_auth_red = [0] * 77
        sendable_auth_red[0] = "r"
        
        if len(global_dispatch_orders) > 1:
            #print("Wait for t = " + str(global_dispatch_orders[1][3]))
            
            for order_num in reversed(global_dispatch_orders):
                #print(order_num[4])
                #print(order_num[5])
                #print("Destination Block : " + str(order_num[7]))
                #print(order_num[0] + " will start at t = " + str(order_num[3]))
                if self.current_time >= order_num[3] and order_num[6] != "skip":
                    #if self.current_time >= 0:
                    if order_num[6] == "g":
                        if self.current_time == order_num[3] and int(order_num[0].rsplit(' ', 1)[1]) > len(global_train_blocks):
                            #print("SENDING GREEN TRAIN")
                            make_green_train = True
                            global_train_blocks.append(order_num[4][0])
                        #print(order_num[4])
                        for i in range(150):
                            if i in order_num[4]:
                                
                                #print("Authority: " + str(order_num[4]))
                                #print("Suggested Speed: " + str(order_num[5]))
                                sendable_auth_green[i+1] = "1"
                                sendable_sugg_speed_green[i+1] = order_num[5][order_num[4].index(i)]
                                #print(str(sendable_sugg_speed[i+1]) + " Curr Speed")
                                #print("Index w/ Authority: " + str(i))
                            else:
                                sendable_auth_green[i+1] = "0"
                                
                            if i == order_num[7]:
                                sendable_auth_green[i+1] = "0"
                    else:
                        if self.current_time == order_num[3] and int(order_num[0].rsplit(' ', 1)[1]) > len(global_train_blocks):
                            #print("SENDING RED TRAIN")
                            make_red_train = True
                            global_train_blocks.append(order_num[4][0])
                        #print(order_num[4])
                        for i in range(76):
                            if i in order_num[4]:
                                sendable_auth_red[i+1] = "1"
                                sendable_sugg_speed_red[i+1] = order_num[5][order_num[4].index(i)]
                                #print(str(sendable_sugg_speed[i+1]) + " Curr Speed")
                                #print("Index w/ Authority: " + str(i))
                            else:
                                sendable_auth_red[i+1] = "0"
                            
                            
                            if i == order_num[7]:
                                sendable_auth_red[i+1] = "0"
                    #print(sendable_auth_green)
                    #print(sendable_sugg_speed_green)
                    #print(sendable_auth_red)
                    #print(sendable_sugg_speed_red)

                #print("Authority")
                #print(len(sendable_auth))
                #print(sendable_auth)
                #print(sendable_sugg_speed)
                #print(sendable_sugg_speed_green)
                #print(sendable_auth_green)
                #print(sendable_sugg_speed_red)
                #print(sendable_auth_red)
                
            #print(sendable_auth_green)
            #print(sendable_sugg_speed_green)
            #print(sendable_auth_red)
            #print(sendable_sugg_speed_red)
                
            print("Authority for Block 65: " + str(sendable_auth_green[65]))
            print("Suggested_Speed fir Block 65: " + str(sendable_sugg_speed_green[65]))
            signals.ctc_suggested_speed_green.emit(sendable_sugg_speed_green)
            signals.ctc_authority_green.emit(sendable_auth_green)
            signals.ctc_suggested_speed_red.emit(sendable_sugg_speed_red)
            signals.ctc_authority_red.emit(sendable_auth_red)
            
            if make_green_train:
                signals.ctc_make_train_green.emit("g")
            if make_red_train:
                signals.ctc_make_train_red.emit("r")
           
            
    def update_time(self,seconds,minutes,hours,total_time):
        self.current_time = total_time
    
    
    def update_order_authority(self,track_state):
        global global_dispatch_orders
        global global_schedule_display
        global global_train_blocks
        
        
        checked_train = []
        
        if int(track_state[0]) == 1: # Green Line
            for order_num in global_dispatch_orders:
                #print("Starting Time = " + str(order_num[3]))
                if order_num[6] != "skip" and order_num[6] == "g" and order_num[3] < self.current_time:
                    if order_num[0] not in checked_train:
                        checked_train.append(order_num[0])
                        if len(order_num[4]) == 1:
                            if int(track_state[order_num[4][0] + 1]) == 0 and int(track_state[order_num[7] + 1]):
                                #print("DELETE THIS DUDE")
                                print(order_num[0])
                                print("Searching Element " + str(int(order_num[0].rsplit(' ', 1)[1]) - 1) + " in " + str(global_train_blocks))
                                global_train_blocks[int(order_num[0].rsplit(' ', 1)[1]) - 1] = order_num[7]
                                order_num[4] = [-1]
                                
                        else:
                            if int(track_state[order_num[4][0] + 1]) == 0 and int(track_state[order_num[4][1] + 1]) == 1:
                                order_num[4].pop(0)
                                order_num[5].pop(0)
                                if len(global_train_blocks) > int(order_num[0].rsplit(' ', 1)[1]) - 1:
                                    global_train_blocks[int(order_num[0].rsplit(' ', 1)[1]) - 1] = order_num[4][0]
                                        
        if int(track_state[0]) == 0: # Red Line
            for order_num in global_dispatch_orders:
                if order_num[6] != "skip" and order_num[6] == "r" and order_num[3] < self.current_time:
                    if order_num[0] not in checked_train:
                        checked_train.append(order_num[0])
                        if len(order_num[4]) == 1:
                            if int(track_state[order_num[4][0] + 1]) == 0 and int(track_state[order_num[7] + 1]):
                                #print("DELETE THIS DUDE")
                                global_train_blocks[int(order_num[0].rsplit(' ', 1)[1]) - 1] = order_num[7]
                                order_num[4] = [-1]
                        else:
                            if int(track_state[order_num[4][0] + 1]) == 0 and int(track_state[order_num[4][1] + 1]) == 1:
                                order_num[4].pop(0)
                                order_num[5].pop(0)
                                if len(global_train_blocks) > int(order_num[0].rsplit(' ', 1)[1]) - 1:
                                    global_train_blocks[int(order_num[0].rsplit(' ', 1)[1]) - 1] = order_num[4][0]
        
        #print("for loop length" + str(len(global_dispatch_orders) + 1))
        i = 0
        while i < len(global_dispatch_orders):
            #print("i = " + str(i))
            print(global_dispatch_orders[i])
            #print("Dispatch " + str(i) + ": " + str(global_dispatch_orders[i][4]))
            if i != 0 and global_dispatch_orders[i][4] == [-1]:
                global_dispatch_orders.pop(i)
                global_schedule_display.pop(i)
                i = i - 1
            i = i+1
        print("Length of global_dispatch_orders: " + str(len(global_dispatch_orders)))
        
        
    def update_ctc_displays(self,ui):
        global global_schedule_display
        global global_train_blocks
        
        header = ['Train', 'Destination Station', 'Arrival Time (2400)']
        ui.model = TableModel(global_schedule_display, header)
        ui.tableView_schedule.setModel(ui.model)
        
        if len(global_train_blocks) == 1:
            ui.labelTrain_1.setText("Block " + str(global_train_blocks[0] + 1))
        if len(global_train_blocks) == 2:
            ui.labelTrain_2.setText("Block " + str(global_train_blocks[1] + 1))
        if len(global_train_blocks) == 3:
            ui.labelTrain_3.setText("Block " + str(global_train_blocks[2] + 1))
        if len(global_train_blocks) == 4:
            ui.labelTrain_4.setText("Block " + str(global_train_blocks[3] + 1))
        if len(global_train_blocks) == 5:
            ui.labelTrain_5.setText("Block " + str(global_train_blocks[4] + 1))
        if len(global_train_blocks) == 6:
            ui.labelTrain_6.setText("Block " + str(global_train_blocks[5] + 1))
        if len(global_train_blocks) == 7:
            ui.labelTrain_7.setText("Block " + str(global_train_blocks[6] + 1))
        if len(global_train_blocks) == 8:
            ui.labelTrain_8.setText("Block " + str(global_train_blocks[7] + 1))
        if len(global_train_blocks) == 9:
            ui.labelTrain_9.setText("Block " + str(global_train_blocks[8] + 1))
        if len(global_train_blocks) == 10:
            ui.labelTrain_10.setText("Block " + str(global_train_blocks[9] + 1))
            

class TrainStation:
    def __init__(self,conn_index,connections):
        self.conn_index = conn_index
        self.connections = connections



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    
    prog = ctc_qtui_test()
    
    
    
    sys.exit(app.exec_())
