import Settings
import Channel

class PSUManager:

    userSettingsCH1 = Settings()#get value from UI later
    userSettingsCH2 = Settings()
    userSettingsCH3 = Settings()
    userSettingsCH1.setAll(0,0,0,0)
    userSettingsCH2.setAll(0, 0, 0, 0)
    userSettingsCH3.setAll(0, 0, 0, 0)


    channel01 = Channel()
    channel02 = Channel()
    channel03 = Channel()
    def _init_(self):
        pass

    def initUI(self):
        pass
    def initChannels(self):
        self.channel01.conn()
        self.channel01.reset()
        self.channel01.set_bias()
        self.channel01.getuserSettings(self.userSettingsCH1)
        self.channel02.conn()
        self.channel02.reset()
        self.channel02.set_bias()
        self.channel02.getuserSettings(self.userSettingsCH2)
        self.channel03.conn()
        self.channel03.reset()
        self.channel03.set_bias()
        self.channel03.getuserSettings(self.userSettingsCH3)

    def swichChannelOn(self,id):
        if id == 1:
            self.userSettingsCH1.turn_on(1)
        if id == 2:
            self.userSettingsCH2.turn_on(2)
        if id == 3:
            self.userSettingsCH3.turn_on(3)

    def swichChannelOff(self):
        if id == 1:
            self.userSettingsCH1.turn_off(1)
        if id == 2:
            self.userSettingsCH2.turn_off(2)
        if id == 3:
            self.userSettingsCH3.turn_off(3)
    def savePresets(self):
        pass
    def browseFiles(self):
        pass
    def loadPresets(self):
        pass
    def readChannels(self,id):
        readCH1= Settings()
        readCH2 = Settings()
        readCH3 = Settings()
        if id == 1:
           readCH1= self.channel01.getreadingsSettings()
        if id == 2:
            readCH2 = self.channel02.getreadingsSettings()
        if id == 3:
            readCH3 = self.channel03.getreadingsSettings()

        readings = [readCH1, readCH2, readCH3]
        return readings
    def userinput(self,v,c,ovp,ocp,id):
        if id == 1:
            self.userSettingsCH1.setAll(v,c,ovp,ocp)
        if id==2:
            self.userSettingsCH2.setAll(v,c,ovp,ocp)
        if id ==3:
            self.userSettingsCH3.setAll(v, c, ovp, ocp)
    def plot(self):
        pass
    def configureChannel(self):
        self.channel01.setuserSettings()
        self.channel02.setuserSettings()
        self.channel03.setuserSettings()

    def sendToDB(self):
        pass
