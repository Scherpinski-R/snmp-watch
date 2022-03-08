class DeviceParameter:
    def __init__ (self, parameterName):
        self.name = parameterName
        self.value = ( -1, -1, -1)             # (min, avg, max) values aquired
        
        self._numSample = 0
        self._sumSample = 0

    def getParameterName(self):
        return self.parameterName

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
