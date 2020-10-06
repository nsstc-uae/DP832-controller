#unfinished file
import datetime
import time, sys

class Settings:
    voltage = 0.0
    current= 0.0
    ovp = 0.0
    ocp= 0.0
    state= False
    def _init_(self, voltage, current, ovp, ocp, state):
        self.voltage=voltage
        self.current=current
        self.ovp=ovp
        self.ocp=ocp
        self.state=state

    def getVolt(self):
        return self.voltage
    def getCurr(self):
        return self.current
    def getOVP(self):
        return self.ovp
    def getOCP(self):
        return self.ocp
    def setVolt(self,volt):
        self.voltage=volt
    def setCurr(self,curr):
        self.current=curr
    def setOVP(self,ovp):
        self.ovp=ovp
    def setOCP(self,ocp):
        self.ocp=ocp

class PlotParameters:
    voltage =0.0
    current =0.0
    def _init_(self, voltage, current):
        self.voltage=voltage
        self.current=current



class Plot:
    time= datetime
    parameters=PlotParameters
    def _init_(self, time , parameters):
        self.time=time
        self.parameters=parameters
    def plotBase(self):
        pass
    def startPlot(self):
        pass
    def plotChange(self):
        pass
    def stopPlot(self):
        pass
    def savePlot(self):
        pass




class Channel:
    id =1
    userSettings = Settings
    lastAppliedSettings = Settings
    readingsSettings = Settings
    #plotParameters =PlotParameters
    #plot=Plot

    def _init_(self, id, userSettings):
        self.id=id
        self.userSettings=userSettings

    """Attempt to connect to instrument via files"""
    def conn(self,device):

        self.fpwrite = open(device,"w")
        self.fpread = open(device, "r")

    """write into instrument"""
    def mywrite(self, message):
        self.fpwrite.write(message)
        self.fpwrite.flush()
        time.sleep(0.1)
    """read from instrument"""
    def myread(self):
        time.sleep(0.01)
        result = self.fpread.read()
        return result

    """resets the insterument"""
    def reset(self):
        self.mywrite("*RST")
        time.sleep(0.2)

    def close_instrument(self):
        self.fpwrite.close()

    def set_bias(self, channel=1, i=0.1, i_protection_level=0.1, v_protection_level=0.9, v=0.5):
        self.mywrite(':INST CH{channel}'.format(channel=int(channel)))
        self.mywrite(':CURR {i}'.format(i=i))
        self.mywrite(':CURR:PROT {i_level}'.format(i_level=i_protection_level))
        self.mywrite(':CURR:PROT:STAT ON')
        self.mywrite(':VOLT {0}'.format(v))
        self.mywrite(':VOLT:PROT {v_level}'.format(v_level=v_protection_level))
        self.mywrite(':VOLT:PROT:STAT ON')

    def turn_off(self, channel=1):
        self.mywrite(':OUTP CH{channel},OFF'.format(channel=channel))
        self.mywrite(':VOLT:PROT:STAT OFF')
        self.mywrite(':CURR:PROT:STAT OFF')

    def turn_on(self, channel=1):
        self.mywrite(':OUTP CH{channel},ON'.format(channel=channel))

    def uservoltage(self):
        self.mywrite(':INST CH{channel}'.format(channel=int(id)))
        self.mywrite(':VOLT {0}'.format(self.userSettings.getVolt()))

    def usercurrent(self):
        self.mywrite(':INST CH{channel}'.format(channel=int(id)))
        self.mywrite(':CURR {c}'.format(c=self.userSettings.getCurr()))

    def userOVP(self):
        self.mywrite(':INST CH{channel}'.format(channel=int(id)))
        self.mywrite(':VOLT:PROT {ovp}'.format(self.userSettings.getOVP()))
        self.mywrite(':VOLT:PROT:STAT ON')

    def userOCP(self):
        self.mywrite(':INST CH{channel}'.format(channel=int(id)))
        self.mywrite(':CURR:PROT {ocp}'.format(ocp=self.userSettings.getOCP()))
        self.mywrite(':CURR:PROT:STAT ON')


    def readVolt(self):
        self.mywrite(':INST CH{channel}'.format(channel=int(id)))
        self.mywrite(':MEAS:VOLT? CH{channel}'.format(channel=int(id)))
        print(':MEAS:VOLT? CH{channel}'.format(channel=int(id)))
        volt = self.myread()
        self.readingsSettings.setVolt(volt)

    def readCurrent(self):
        self.mywrite(':INST CH{channel}'.format(channel=int(id)))
        self.mywrite(':MEAS:CURR? CH{channel}'.format(channel=int(id)))
        current = self.myread()
        self.readingsSettings.setCurr(current)

    def readovp(self):
        self.mywrite(':INST CH{channel}'.format(channel=int(id)))
        self.mywrite(':MEAS:VOLT:PROT:? CH{channel}'.format(channel=int(id)))
        ovp = self.myread()
        self.readingsSettings.setOVP(ovp)

    def readocp(self):
        self.mywrite(':INST CH{channel}'.format(channel=int(id)))
        self.mywrite(':MEAS:CURR:PROT:? CH{channel}'.format(channel=int(id)))
        ocp = self.myread()
        self.readingsSettings.setOCP(ocp)





class PSUManager:
    channels = []
    def _init_(self):
        pass

    def initUI(self):
        pass
    def initChannels(self):
        pass
    def swichChannelOn(self):
        pass
    def swichChannelOff(self):
        pass
    def savePresets(self):
        pass
    def browseFiles(self):
        pass
    def loadPresets(self):
        pass
    def readChannels(self):
        pass
    def plot(self):
        pass
    def configureChannel(self):
        pass
    def sendToBB(self):
        pass
