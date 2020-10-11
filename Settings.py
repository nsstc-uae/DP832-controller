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
    def setALL(self,v,c,ovp,ocp):
        self.ocp = ocp
        self.ovp = ovp
        self.current = c
        self.voltage = v
