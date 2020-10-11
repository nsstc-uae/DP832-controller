import Settings
import Channel

class PSUManager:
    userSettingsCH1 = Settings()#get value from UI later
    userSettingsCH2 = Settings()
    userSettingsCH3 = Settings()
    channel01 = Channel(1, userSettingsCH1)
    channel02 = Channel(2, userSettingsCH2)
    channel03 = Channel(3, userSettingsCH3)
    def _init_(self):
        pass

    def initUI(self):
        pass
    def initChannels(self):
        self.channel01.conn()
        pass
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
    def readChannels(self):
        pass
    def plot(self):
        pass
    def configureChannel(self):
        pass
    def sendToDB(self):
        pass
