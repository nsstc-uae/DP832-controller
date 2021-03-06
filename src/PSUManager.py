from src import Settings as s, Channel as c, DBconnection as dpconnect
from datetime import datetime


class PSUManager:
    userSettingsCH1 = s.Settings()  # get value from UI later
    userSettingsCH2 = s.Settings()
    userSettingsCH3 = s.Settings()
    userSettingsCH1.setAll(v=0, c=0, ovp=0, ocp=0)
    userSettingsCH2.setAll(v=0, c=0, ovp=0, ocp=0)
    userSettingsCH3.setAll(v=0, c=0, ovp=0, ocp=0)

    channel01 = c.Channel()
    channel01.setID(1)
    channel02 = c.Channel()
    channel02.setID(2)
    channel03 = c.Channel()
    channel03.setID(3)

    database = dpconnect.connection()

    def initChannels(self):

        # reset channels
        self.channel01.reset()
        self.channel03.reset()
        self.channel02.reset()

        # set Bias
        self.channel01.set_bias(channel=1)
        self.channel01.getUserSettings(self.userSettingsCH1)

        self.channel02.set_bias(channel=2)
        self.channel02.getUserSettings(self.userSettingsCH2)

        self.channel03.set_bias(channel=3)
        self.channel03.getUserSettings(self.userSettingsCH3)

    def switchChannelOn(self, id):
        # turn ON channels
        if id == 1:
            self.channel01.turn_on(channel=1)
        if id == 2:
            self.channel02.turn_on(channel=2)
        if id == 3:
            self.channel03.turn_on(channel=3)

    def switchChannelOff(self, id):
        # turn OFF channels
        if id == 1:
            self.channel01.turn_off(channel=1)
        if id == 2:
            self.channel02.turn_off(channel=2)
        if id == 3:
            self.channel03.turn_off(channel=3)

    # OCP/OVP ON/OFF
    def switchOcpOFF(self):
        self.channel01.ocpOFF()

    def switchOvpOFF(self):
        self.channel01.ovpOFF()

    def switchOcpON(self):
        self.channel01.ocpON()

    def switchOvpON(self):
        self.channel01.ovpON()

    def readChannels(self, connectState):
        # get values from device
        readCH1 = self.channel01.getReadingsSettings()
        readCH2 = self.channel02.getReadingsSettings()
        readCH3 = self.channel03.getReadingsSettings()

        readings = [readCH1, readCH2, readCH3]

        # get time and save time and current to file for the plot
        now = datetime.now()

        f = open("data/PlotParameters/Channel1.txt", 'a')
        f.write(now.strftime("%H:%M:%S") + ", " + readCH1.getCurr())
        f.write("\n")
        f.close()
        f = open("data/PlotParameters/Channel2.txt", 'a')
        f.write(now.strftime("%H:%M:%S") + ", " + readCH2.getCurr())
        f.write("\n")
        f.close()
        f = open("data/PlotParameters/Channel3.txt", 'a')
        f.write(now.strftime("%H:%M:%S") + ", " + readCH3.getCurr())
        f.write("\n")
        f.close()
        if connectState == True:
            try:
                info = self.readDBinfo()
                print("DB: "+info[0]+" pass: "+info[1]+" user: "+info[2]+" table: "+info[3])
                self.database.connect(current=readCH1.getCurr(), channel="1", voltage=readCH1.getVolt(), db = info[0], passw = info[1], user = info[2], table = info[3])
                self.database.connect(current=readCH2.getCurr(), channel="2", voltage=readCH2.getVolt(), db = info[0], passw = info[1], user = info[2], table = info[3])
                self.database.connect(current=readCH3.getCurr(), channel="3", voltage=readCH3.getVolt(), db = info[0], passw = info[1], user = info[2], table = info[3])
            except:
                print("somthing wrong happened when connecting to DB")
        else:
            print("connect State OFF")
        return readings

    def configureChannel(self, v, c, ovp, ocp, id):
        # send user configurations to device
        if id == 1:
            self.userSettingsCH1.setAll(v, c, ovp, ocp)
            self.channel01.setUserSettings()
        if id == 2:
            self.userSettingsCH2.setAll(v, c, ovp, ocp)
            self.channel02.setUserSettings()
        if id == 3:
            self.userSettingsCH3.setAll(v, c, ovp, ocp)
            self.channel03.setUserSettings()

    def readDBinfo(self):
        fn = "data/DatabaseInformation/DBinfo.txt"
        f = open(fn, 'r')
        dt = f.read()
        dd = dt.splitlines()
        f.close()
        for line in dd:
            contents = line.split(',')  # each line represents a channel
            try:
                dbName = contents[0]
                password = contents[1]
                username = contents[2]
                tableName = contents[3]
            except:
                print("invalid Database file")

        return contents
