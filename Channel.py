
import Settings as s
import time


class Channel:
    id =1
    userSettings = s.Settings()
    readingsSettings = s.Settings()
    fpwrite=None
    fpread=None

    def _init_(self, id, userSettings):
        self.id=id
        self.userSettings=userSettings

    def setID(self,ID):
        self.id=ID

    """Attempt to connect to instrument via files"""
    def conn(self,device):

        print("connect")


    """write into instrument"""
    def mywrite(self, message):
        self.fpwrite = open("/dev/usbtmc0", "w")
        self.fpwrite.write(message)
        self.fpwrite.flush()
        time.sleep(0.1)
        self.fpwrite.close()
    """read from instrument"""
    def myread(self,n):
        try:
            self.fpread = open("/dev/usbtmc0", "r")
            time.sleep(0.5)
            result = self.fpread.read(n)
            self.fpread.close()
            return result
        except:
            return "0"
            print("read timeout")



    """resets the insterument"""
    def reset(self):
        self.mywrite("*RST")
        time.sleep(0.2)

    def close_instrument(self):
        self.fpwrite.close()

    def set_bias(self, channel):
        i = 0.1
        i_protection_level = 0.1
        v_protection_level = 0.9
        v = 0.5
        self.mywrite(':INST CH{channel}'.format(channel=int(channel)))
        self.mywrite(':CURR {i}'.format(i=i))
        self.mywrite(':CURR:PROT {i_level}'.format(i_level=i_protection_level))
        self.mywrite(':CURR:PROT:STAT ON')
        self.mywrite(':VOLT {0}'.format(v))
        self.mywrite(':VOLT:PROT {v_level}'.format(v_level=v_protection_level))
        self.mywrite(':VOLT:PROT:STAT ON')

    def turn_off(self, channel):
        self.mywrite(':OUTP CH{channel},OFF'.format(channel=channel))
        self.mywrite(':VOLT:PROT:STAT OFF')
        self.mywrite(':CURR:PROT:STAT OFF')

    def turn_on(self, channel):
        self.mywrite(':OUTP CH{channel},ON'.format(channel=channel))

        #user settings
    def uservoltage(self):
        self.mywrite(':INST CH{channel}'.format(channel=int(self.id)))
        self.mywrite(':VOLT {0}'.format(self.userSettings.getVolt()))

    def usercurrent(self):
        self.mywrite(':INST CH{channel}'.format(channel=int(self.id)))
        self.mywrite(':CURR {c}'.format(c=self.userSettings.getCurr()))

    def userOVP(self):
        self.mywrite(':INST CH{channel}'.format(channel=int(self.id)))
        self.mywrite(':VOLT:PROT {ovp}'.format(ovp=self.userSettings.getOVP()))
        #self.mywrite(':VOLT:PROT:STAT ON')

    def userOCP(self):
        self.mywrite(':INST CH{channel}'.format(channel=int(self.id)))
        self.mywrite(':CURR:PROT {ocp}'.format(ocp=self.userSettings.getOCP()))
        #self.mywrite(':CURR:PROT:STAT ON')


    def ocpOFF(self):
        self.mywrite(':OUTP:PROT:STAT OFF')

    def ocpON(self):
        self.mywrite(':CURR:PROT:STAT ON')

    def ovpOFF(self):
        self.mywrite(':VOLT:PROT:STAT OFF')

    def ovpON(self):
        self.mywrite(':VOLT:PROT:STAT ON')

        #reading output
    def readVolt(self):
        self.mywrite(':MEAS:VOLT? CH{channel}'.format(channel=int(self.id)))
        volt = self.myread(5)
        print("volt:"+volt)
        self.readingsSettings.setVolt(volt)

    def readCurrent(self):
        self.mywrite(':MEAS:CURR? CH{channel}'.format(channel=int(self.id)))
        current = self.myread(5)
        print("current:" +current)
        self.readingsSettings.setCurr(current)

    def readovp(self):
        self.mywrite(':OUTP:OVP:VAL? CH{channel}'.format(channel=int(self.id)))

        ovp = self.myread(5)
        print("ovp: "+ ovp)
        self.readingsSettings.setOVP(ovp)

    def readocp(self):
        self.mywrite(':OUTP:OCP:VAL? CH{channel}'.format(channel=int(self.id)))
        ocp = self.myread(5)
        print("ocp: "+ocp)
        self.readingsSettings.setOCP(ocp)

    def readChannelState(self):
        self.mywrite(':OUTP? CH{channel}'.format(channel=int(self.id)))
        state = self.myread(3)
        print("state:"+ state)
        self.readingsSettings.setChannelState(state)

    def readOvpState(self):
        self.mywrite(':OUTP:OVP?')
        state = self.myread(3)
        self.readingsSettings.setOvpS(state)
        print("ovp state:"+ state)


    def readOcpState(self):
        self.mywrite(':OUTP:OCP?')
        state = self.myread(3)
        self.readingsSettings.setOcpS(state)
        print("ocp state:"+ state)
        #self.readingsSettings.setOcpS(state)

    def getuserSettings(self,settings):
        self.userSettings = settings

    def setuserSettings(self):
        self.uservoltage()
        self.usercurrent()
        self.userOCP()
        self.userOVP()

    def getreadingsSettings(self):
        self.readCurrent()
        self.readocp()
        self.readVolt()
        self.readovp()
        self.readChannelState()
        self.readOvpState()
        self.readOcpState()
        return self.readingsSettings

