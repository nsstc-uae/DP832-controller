import Settings as s
import Channel as c
from datetime import datetime

class PSUManager:

    userSettingsCH1 = s.Settings() #get value from UI later
    userSettingsCH2 = s.Settings()
    userSettingsCH3 = s.Settings()
    userSettingsCH1.setAll(v=0,c=0,ovp=0,ocp=0)
    userSettingsCH2.setAll(v=0,c=0,ovp=0,ocp=0)
    userSettingsCH3.setAll(v=0,c=0,ovp=0,ocp=0)

    channel01 = c.Channel()
    channel01.setID(1)
    channel02 = c.Channel()
    channel02.setID(2)
    channel03 = c.Channel()
    channel03.setID(3)

    def _init_(self):
        pass

    def initUI(self):
        pass


    def initChannels(self,device):
        #starting connection to device channel
        self.channel01.conn(device)
        self.channel02.conn(device)
        self.channel03.conn(device)

        #reset channels
        self.channel01.reset()
        self.channel03.reset()
        self.channel02.reset()

        #set Bias
        self.channel01.set_bias(channel=1)
        self.channel01.getuserSettings(self.userSettingsCH1)


        self.channel02.set_bias(channel=2)
        self.channel02.getuserSettings(self.userSettingsCH2)

        self.channel03.set_bias(channel=3)
        self.channel03.getuserSettings(self.userSettingsCH3)

    def switchChannelOn(self,id):
        #turn on channels
        if id == 1:
            self.channel01.turn_on(channel=1)
        if id == 2:
            self.channel02.turn_on(channel=2)
        if id == 3:
            self.channel03.turn_on(channel=3)

    def switchOcpOFF(self):
        self.channel01.ocpOFF()
    def switchOvpOFF(self):
        self.channel01.ovpOFF()
    def switchOcpON(self):
        self.channel01.ocpON()
    def switchOvpON(self):
        self.channel01.ovpON()

    def connect(self,device):
        self.channel01.conn(device)
        self.channel02.conn(device)
        self.channel03.conn(device)


    def switchChannelOff(self,id):
        #turn off channels
        if id == 1:
            self.channel01.turn_off(channel=1)
        if id == 2:
            self.channel02.turn_off(channel=2)
        if id == 3:
            self.channel03.turn_off(channel=3)

    def readChannels(self):
        #get values from device
        readCH1= self.channel01.getreadingsSettings()
        readCH2 = self.channel02.getreadingsSettings()
        readCH3 = self.channel03.getreadingsSettings()

        readings = [readCH1, readCH2, readCH3]
        now = datetime.now()

        f = open("plots/Channel1.txt", 'a')
        f.write(now.strftime("%H:%M:%S") + ", " +readCH1.getCurr())
        f.write("\n")
        f.close()
        f = open("plots/Channel2.txt", 'a')
        f.write(now.strftime("%H:%M:%S") + ", " +readCH2.getCurr())
        f.write("\n")
        f.close()
        f = open("plots/Channel3.txt", 'a')
        f.write(now.strftime("%H:%M:%S") + ", " +readCH3.getCurr())
        f.write("\n")
        f.close()


        return readings

    def configureChannel(self,v,c,ovp,ocp,id):
        #send user configurations to device
        if id == 1:
            self.userSettingsCH1.setAll(v, c, ovp, ocp)
            self.channel01.setuserSettings()
        if id == 2:
            self.userSettingsCH2.setAll(v, c, ovp, ocp)
            self.channel02.setuserSettings()
        if id == 3:
            self.userSettingsCH3.setAll(v, c, ovp, ocp)
            self.channel03.setuserSettings()

    def sendToDB(self):
        pass
