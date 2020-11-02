class Settings:
    voltage = ""
    current = ""
    ovp = ""
    ocp = ""
    state = ""
    ovpState = ""
    ocpState = ""

    def _init_(self, voltage, current, ovp, ocp, state):
        self.voltage = voltage
        self.current = current
        self.ovp = ovp
        self.ocp = ocp
        self.state = state

    # getters
    def getChannelState(self):
        return self.state

    def getVolt(self):
        return self.voltage

    def getCurr(self):
        return self.current

    def getOVP(self):
        return self.ovp

    def getOCP(self):
        return self.ocp

    def getOcpS(self):
        return self.ocpState

    def getOvpS(self):
        return self.ovpState

    # setters
    def setChannelState(self, state):
        self.state = state

    def setVolt(self, volt):
        self.voltage = volt

    def setCurr(self, curr):
        self.current = curr

    def setOVP(self, ovp):
        self.ovp = ovp

    def setOCP(self, ocp):
        self.ocp = ocp

    def setOcpS(self, ocpState):
        self.ocpState = ocpState

    def setOvpS(self, ovpState):
        self.ovpState = ovpState

    def setAll(self, v, c, ovp, ocp):
        self.ocp = ocp
        self.ovp = ovp
        self.current = c
        self.voltage = v
