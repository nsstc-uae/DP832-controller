import Plot
import Settings
import datetime
import time, sys
from multiprocessing import Process
class Channel:
    id =1
    userSettings = Settings
    lastAppliedSettings = Settings
    readingsSettings = Settings

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

    def setuserSettings(self):
        self.uservoltage()
        self.usercurrent()
        self.userOCP()
        self.userOVP()

    def writeFilePlot(self):
        state = True
        while state:
            fn = "Channel"+id+".txt"
            f = open(fn, "w")
            f.write(datetime.datetime.now().time()+","+self.readingsSettings.getCurr())
            time.sleep(5)
        f.close()

    def startPlot(self):
        Process(target=self.writeFilePlot().start())  # start now
        p = Plot(id)#start at the same time
        p.startPlot()#start after plot



