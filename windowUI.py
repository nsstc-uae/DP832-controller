from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *

from main import *

import sys
import os

class WindowUI(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.browseBttn.clicked.connect(self.browseFiles)
        self.saveAsBttn.clicked.connect(self.saveAs)
        self.applySelectedBttn.clicked.connect(self.applySelected)
        self.loadBttn.clicked.connect(self.loadPreset)
        self.setBttn_ch1.clicked.connect(self.setChannels)
        self.setBttn_ch2.clicked.connect(self.setChannels)
        self.setBttn_ch3.clicked.connect(self.setChannels)

    def browseFiles(self):
        fname = QFileDialog.getOpenFileNames(None, 'Select preset file', os.getcwd(), 'All Files (*.*)')
        fn = fname[0][0]
        self.temp_uploadfileTF.setText(fn)
        filename= "preset.txt"
        #self.readFile(filename)
        print("browse file button")
        #print(fname)

#method to read file after opening.
    def readFile(fn):
        with open (fn, "r") as f:
            for line in f:
                contents = line.split()
                chID = contents[0]
                chVol = contents[1]
                chCurr = contents[2]
                chOVP = contents[3]
                chOCP = contents[4]
                print ('Channel ID: ' + chID + ', Voltage: ' + chVol + ', Current: '+ chCurr + ', OVP: '+chOVP+', OCP: '+chOCP)

    def writeFile(self):
        fn = "preset.txt"
        f = open (fn, "w")
        f.write("CH1, Voltage, Current, OVP, OCP")
        f.close()

    def saveAs(self):
        self.writeFile()
        print("Save as preset")

    def applySelected(self):
        print("Apply selected")

    def loadPreset(self):
        print("Preset Loaded")

    def setChannels(self):
        print("channel have been set")

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = WindowUI(MainWindow)

MainWindow.show()
app.exec_()