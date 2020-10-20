from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *
from multiprocessing import Process
from main import *
import serial
import PSUManager as psu
# import Plot
import Settings as s
# import Channel
# import PlotParameters
import time
import datetime
import sys
import os


class WindowUI(Ui_MainWindow):

    psu = psu.PSUManager()

    def __init__(self, window):
        self.setupUi(window)

        ##PSUManager
        self.psu.initChannels(device="/dev/usbtmc0")
        ##SpinBox Configure
        self.voltageSP_ch1.setMaximum(30)
        self.voltageSP_ch2.setMaximum(30)
        self.voltageSP_ch3.setMaximum(5)

        self.currentSP_ch1.setMaximum(3)
        self.currentSP_ch2.setMaximum(3)
        self.currentSP_ch3.setMaximum(3)

        self.ovpVolSP_ch1.setMinimum(0.01)
        self.ovpVolSP_ch2.setMinimum(0.01)
        self.ovpVolSP_ch3.setMinimum(0.01)

        self.ovpVolSP_ch1.setMaximum(33)
        self.ovpVolSP_ch2.setMaximum(33)
        self.ovpVolSP_ch3.setMaximum(5.5)

        self.ocpCurrSP_ch1.setMinimum(0.001)
        self.ocpCurrSP_ch2.setMinimum(0.001)
        self.ocpCurrSP_ch3.setMinimum(0.001)

        self.ocpCurrSP_ch1.setDecimals(3)
        self.ocpCurrSP_ch2.setDecimals(3)
        self.ocpCurrSP_ch3.setDecimals(3)

        self.ocpCurrSP_ch1.setMaximum(3.3)
        self.ocpCurrSP_ch2.setMaximum(3.3)
        self.ocpCurrSP_ch3.setMaximum(3.3)

        ##Buttons
        self.browseBttn.clicked.connect(self.browseFiles)
        self.saveAsBttn.clicked.connect(self.saveAs)
        self.setBttn_ch1.clicked.connect(self.setCh1)
        self.setBttn_ch2.clicked.connect(self.setCh2)
        self.setBttn_ch3.clicked.connect(self.setCh3)
        self.switchBttn_channels.clicked.connect(self.switchChannels)
        #Process(target=self.readingOutput().start())
        # fpw=open("/dev/usbtmc0", "w")
        # #fpw.write(":OUTP CH1,ON")
        # fpw.write(":MEAS:VOLT? CH1")
        # time.sleep(1)
        # fp=open("/dev/usbtmc0", "r")
        # i=0;
        #
        # while(i<10):
        #     i=i+1
        #     try:
        #         val=fp.read(2)
        #         print("\nthe voltage is 1111111 : " +val)
        #     except:
        #         print("\nfailed111")
        #self.readingOutput()



    def readingOutput(self):

        readings = self.psu.readChannels()
        self.voltageReadingField_ch1.setText(str(readings[0].getVolt()))
        self.currentReadingField_ch1.setText(str(readings[0].getCurr()))
        self.ocpCurrTF_ch1.setText(str(readings[0].getOCP()))
        self.ovpVolTF_ch1.setText(str(readings[0].getOVP()))

        self.voltageReadingField_ch2.setText(str(readings[1].getVolt()))
        self.currentReadingField_ch2.setText(str(readings[1].getCurr()))
        self.ocpCurrTF_ch2.setText(str(readings[1].getOCP()))
        self.ovpVolTF_ch2.setText(str(readings[1].getOVP()))

        print(readings)

        self.voltageReadingField_ch3.setText(str(readings[2].getVolt()))
        self.currentReadingField_ch3.setText(str(readings[2].getCurr()))
        self.ocpCurrTF_ch3.setText(str(readings[2].getOCP()))
        self.ovpVolTF_ch3.setText(str(readings[2].getOVP()))

    def switchChannels(self):
        if self.channel1_rBttn.isChecked():
            self.psu.swichChannelOn(id=1)
            print("ch1 is on")

        if self.channel2_rBttn.isChecked():
            self.psu.swichChannelOn(id=2)
            print("ch2 is on")

        if self.channel3_rBttn.isChecked():
            self.psu.swichChannelOn(id=3)
            print("ch3 is on")

        if not self.channel1_rBttn.isChecked():
            self.psu.swichChannelOff(id=1)
            print("ch1 is off")

        if not self.channel2_rBttn.isChecked():
            self.psu.swichChannelOff(id=2)
            print("ch2 is off")

        if not self.channel3_rBttn.isChecked():
            self.psu.swichChannelOff(id=3)
            print("ch3 is off")

    def browseFiles(self):
        fname = QFileDialog.getOpenFileNames(None, 'Select preset file', os.getcwd(), 'All Files (*.*)')
        fpath = fname[0][0]
        self.uploadfileTF.setText(fpath)
        self.readF(fpath)
        print("browse file button")

    def readF(self, fn):
        if fn:
            f = open(fn, 'r')
        with f:
            data = f.read()
            self.readData(data)

    # method to read file after opening.
    def readData(self, dt):
        dd = dt.splitlines()
        for line in dd:
            contents = line.split(',')
            chID = contents[0]
            chVol = contents[1]
            chCurr = contents[2]
            chOVP = contents[3]
            chOCP = contents[4]
            if chID == "1":
                self.setStateBttn_ch1.setChecked(True)
                self.voltageSP_ch1.setValue(float(chVol))
                self.currentSP_ch1.setValue(float(chCurr))
                self.ovpStateBttn_ch1.setChecked(True)
                self.ovpVolSP_ch1.setValue(float(chOVP))
                self.ocpStateBttn_ch1.setChecked(True)
                self.ocpCurrSP_ch1.setValue(float(chOCP))

            if chID == "2":
                self.setStateBttn_ch2.setChecked(True)
                self.voltageSP_ch2.setValue(float(chVol))
                self.currentSP_ch2.setValue(float(chCurr))
                self.ovpStateBttn_ch2.setChecked(True)
                self.ovpVolSP_ch2.setValue(float(chOVP))
                self.ocpStateBttn_ch2.setChecked(True)
                self.ocpCurrSP_ch2.setValue(float(chOCP))

            if chID == "3":
                self.setStateBttn_ch3.setChecked(True)
                self.voltageSP_ch3.setValue(float(chVol))
                self.currentSP_ch3.setValue(float(chCurr))
                self.ovpStateBttn_ch3.setChecked(True)
                self.ovpVolSP_ch3.setValue(float(chOVP))
                self.ocpStateBttn_ch3.setChecked(True)
                self.ocpCurrSP_ch3.setValue(float(chOCP))

            print(
                'Channel ID: ' + chID + ', Voltage: ' + chVol + ', Current: ' + chCurr + ', OVP: ' + chOVP + ', OCP: ' + chOCP)
        # self.loadF(chID=chID, chVol=chVol, chCurr=chCurr, chOVP=chOVP, chOCP=chOCP)

    def writeFile(self):
        dt =str(datetime.datetime.now())
        fn = "preset"+dt+".txt"
        ### getting channel settings
        chVol_1 = str(self.voltageSP_ch1.value())
        chCurr_1 = str(self.currentSP_ch1.value())
        chOVP_1 = str(self.ovpVolSP_ch1.value())
        chOCP_1 = str(self.ocpCurrSP_ch1.value())

        chVol_2 = str(self.voltageSP_ch2.value())
        chCurr_2 = str(self.currentSP_ch2.value())
        chOVP_2 = str(self.ovpVolSP_ch2.value())
        chOCP_2 = str(self.ocpCurrSP_ch2.value())

        chVol_3 = str(self.voltageSP_ch3.value())
        chCurr_3 = str(self.currentSP_ch3.value())
        chOVP_3 = str(self.ovpVolSP_ch3.value())
        chOCP_3 = str(self.ocpCurrSP_ch3.value())
        ###

        f = open(fn, "w")
        f.write("1, " + chVol_1 + ", " + chCurr_1 + ", " + chOVP_1 + ", " + chOCP_1)
        f.write("\n")
        f.write("2, " + chVol_2 + ", " + chCurr_2 + ", " + chOVP_2 + ", " + chOCP_2)
        f.write("\n")
        f.write("3, " + chVol_3 + ", " + chCurr_3 + ", " + chOVP_3 + ", " + chOCP_3)
        f.close()

    def saveAs(self):
        self.writeFile()
        print("Save as preset")

    def applySelected(self):
        print("Apply selected")

    def setCh1(self):
        chVol_1 = self.voltageSP_ch1.value()
        chCurr_1 = self.currentSP_ch1.value()
        chOVP_1 = self.ovpVolSP_ch1.value()
        chOCP_1 = self.ocpCurrSP_ch1.value()
        # configureChannel(self,v,c,ovp,ocp,id):

        self.psu.configureChannel(chVol_1, chCurr_1, chOVP_1, chOCP_1, 1)
        print("channel 1 have been set")

    def setCh2(self):
        chVol_2 = self.voltageSP_ch2.value()
        chCurr_2 = self.currentSP_ch2.value()
        chOVP_2 = self.ovpVolSP_ch2.value()
        chOCP_2 = self.ocpCurrSP_ch2.value()
        # configureChannel(self,v,c,ovp,ocp,id):

        self.psu.configureChannel(chVol_2, chCurr_2, chOVP_2, chOCP_2, 2)
        print("channel 2 have been set")

    def setCh3(self):
        chVol_3 = self.voltageSP_ch3.value()
        chCurr_3 = self.currentSP_ch3.value()
        chOVP_3 = self.ovpVolSP_ch3.value()
        chOCP_3 = self.ocpCurrSP_ch3.value()
        # configureChannel(self,v,c,ovp,ocp,id):

        self.psu.configureChannel(chVol_3, chCurr_3, chOVP_3, chOCP_3, 3)
        print("channel 3 have been set")


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = WindowUI(MainWindow)

MainWindow.show()
app.exec_()
