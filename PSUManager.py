import Settings as s
import Channel as c

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
    def initChannels(self,devic):
        self.channel01.conn(devic)
        self.channel02.conn(devic)
        self.channel03.conn(devic)

        self.channel01.reset()
        self.channel03.reset()
        self.channel02.reset()

        self.channel01.set_bias(channel=1)
        self.channel01.getuserSettings(self.userSettingsCH1)


        self.channel02.set_bias(channel=2)
        self.channel02.getuserSettings(self.userSettingsCH2)

        self.channel03.set_bias(channel=3)
        self.channel03.getuserSettings(self.userSettingsCH3)

    def swichChannelOn(self,id):
        if id == 1:
            self.channel01.turn_on(channel=1)
        if id == 2:
            self.channel02.turn_on(channel=2)
        if id == 3:
            self.channel03.turn_on(channel=3)

    def swichChannelOff(self,id):
        if id == 1:
            self.channel01.turn_off(channel=1)
        if id == 2:
            self.channel02.turn_off(channel=2)
        if id == 3:
            self.channel03.turn_off(channel=3)
    def savePresets(self):
        pass
    def browseFiles(self):
        pass
    def loadPresets(self):
        pass
    def readChannels(self,id):
        readCH1= s.Settings
        readCH2 = s.Settings
        readCH3 = s.Settings
        if id == 1:
           readCH1= self.channel01.getreadingsSettings()
        if id == 2:
            readCH2 = self.channel02.getreadingsSettings()
        if id == 3:
            readCH3 = self.channel03.getreadingsSettings()

        readings = [readCH1, readCH2, readCH3]

        return readings
    def plot(self):
        pass

    def configureChannel(self,v,c,ovp,ocp,id):
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
