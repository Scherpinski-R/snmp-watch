class DeviceParameter:
    def __init__ (self, stringIdentifier, parameterName, parameterMaxName=None):
        self.identifier = stringIdentifier  # User Friendly Name of the parameter, e.g.: RAM, SWAP
        self.name_cur = parameterName       # Current Value of parameter
        self.name_max = parameterMaxName    # Max Resource avaiable of parameter

        self.value = ( -1, -1, -1)             # (min, avg, max) values aquired
        self.maxValue = -1

        self._numSample = 0
        self._sumSample = 0

    def setMaxValue(self, maxSystem):
        if self.isParameterLimited():
            self.maxValue = maxSystem
        else:
            print("LOG: Trying to Set a max value for ilimited parameter")

    def getParameterIdentifier(self):
        return self.identifier

    def getParameterName(self):
        return self.name_cur

    def isParameterLimited(self):
        if self.name_max:
            return True
        else:
            return False

    def getParameterMaxName(self):
        if self.isParameterLimited():
            return self.name_max
        else:
            printf("LOG: Trying to Get max value for ilimited parameter")            

    def sumValue(self, newValue):
        self._numSample += 1
        self._sumSample += newValue

    def setValue(self, minValue, maxValue):
        if(self._numSample == 0):
            print("LOG: no samples for " + self.getParameterName())
        else:
            avgValue    = (self._sumSample)/(self._numSample)
            self.value  = (minValue, avgValue, maxValue)
    
    def getValue(self):
        return self.value
