import Settings
import Channel

class PSUManager:

    userSettingsCH1 = Settings #get value from UI later
    userSettingsCH2 = Settings
    userSettingsCH3 = Settings
    userSettingsCH1.Settings.setAll(userSettingsCH1,v=0,c=0,ovp=0,ocp=0)
    userSettingsCH2.Settings.setAll(userSettingsCH2,v=0,c=0,ovp=0,ocp=0)
    userSettingsCH3.Settings.setAll(userSettingsCH3,v=0,c=0,ovp=0,ocp=0)

    channel01 = Channel
    channel02 = Channel
    channel03 = Channel
    def _init_(self):
        pass

    def initUI(self):
        pass
    def initChannels(self,devic):

        self.channel01.Channel.reset()
        self.channel03.Channel.reset()
        self.channel02.Channel.reset()

        self.channel01.Channel.conn(devic)
        self.channel01.Channel.set_bias(channel=1)
        self.channel01.Channel.getuserSettings(self.userSettingsCH1)

        self.channel02.Channel.conn(devic)
        self.channel02.Channel.set_bias(channel=2)
        self.channel02.Channel.getuserSettings(self.userSettingsCH2)

        self.channel03.Channel.conn(devic)
        self.channel03.Channel.set_bias(channel=3)
        self.channel03.getuserSettings(self.userSettingsCH3)

    def swichChannelOn(self,id):
        if id == 1:
            self.channel01.Channel.turn_on(channel=1)
        if id == 2:
            self.channel02.Channel.turn_on(channel=2)
        if id == 3:
            self.channel03.Channel.turn_on(channel=3)

    def swichChannelOff(self,id):
        if id == 1:
            self.channel01.Channel.turn_off(channel=1)
        if id == 2:
            self.channel02.Channel.turn_off(channel=2)
        if id == 3:
            self.channel03.Channel.turn_off(channel=3)
    def savePresets(self):
        pass
    def browseFiles(self):
        pass
    def loadPresets(self):
        pass
    def readChannels(self,id):
        readCH1= Settings
        readCH2 = Settings
        readCH3 = Settings
        if id == 1:
           readCH1= self.channel01.Channel.getreadingsSettings()
        if id == 2:
            readCH2 = self.channel02.Channel.getreadingsSettings()
        if id == 3:
            readCH3 = self.channel03.Channel.getreadingsSettings()

        readings = [readCH1, readCH2, readCH3]
        return readings
    def plot(self):
        pass
    def configureChannel(self,v,c,ovp,ocp,id):
        if id == 1:
            self.userSettingsCH1.Settings.setAll(v, c, ovp, ocp)
            self.channel01.Channel.setuserSettings()
        if id == 2:
            self.userSettingsCH2.Settings.setAll(v, c, ovp, ocp)
            self.channel02.Channel.setuserSettings()
        if id == 3:
            self.userSettingsCH3.Settings.setAll(v, c, ovp, ocp)
            self.channel03.Channel.setuserSettings()

    def sendToDB(self):
        pass
