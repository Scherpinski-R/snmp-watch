from easysnmp import Session
from DeviceParameter import DeviceParameter
import time

class Device:
    def __init__(self, deviceAlias, deviceIp, authCred, privCred):
        self.alias = deviceAlias
        self.ipAddr = deviceIp

        # (user, pass) for authenticating user
        self.auth = authCred
        # (user, pass) for cryptographing data
        self.priv = privCred

        self._session = None
        

        # Const:
        # TO-DO: add ifSpeed if there is time left
        # RAM - SWAP - Number Processes
        self.parameterNameList = ['hrStorageSize.1', 'hrStorageSize.3', 'hrSystemProcesses']

        self.deviceList = []

        self.deviceList.append( DeviceParameter('RAM', 'hrStorageUsed.1', 'hrStorageSize.1') )
        self.deviceList.append( DeviceParameter('SWAP', 'hrStorageUsed.10', 'hrStorageSize.10') )
        self.deviceList.append( DeviceParameter('Number Processes', 'hrSystemProcesses.0', 'hrSystemMaxProcesses.0') )
        
        ## if more parameters are going to be added put them above

        self.TIME = 1 # constant to show how many minutes will be sampled

    def createSession(self):
        self._session = Session(hostname=self.ipAddr, version=3, security_level="auth_with_privacy", auth_protocol="MD5",
                                security_username=self.auth[0], auth_password=self.auth[1], privacy_protocol="DES", privacy_password=self.priv[1])

        if self._session == None:
            print("LOG: Failed to create Session")

    def performAnalytics(self):
        if self._session == None:
            print("LOG: Session not Created")
            return

        for parameter in self.deviceList:
            if parameter.isParameterLimited():
                max_value   = self._session.get(parameter.getParameterMaxName())
                max_value   = max_value.value               #shadowing variable SNTP Var -> Value
                parameter.setMaxValue(max_value)

        for i in range(self.TIME * 3):
            for parameter in self.deviceList:
                current_value   = self._session.get(parameter.getParameterName())
                current_value   = current_value.value
                
                parameter.sumValue(current_value)
                parameter.checkAndSetIfBiggestOrLowest(current_value)

                print(current_value)

            time.sleep(20)  # wait 60s to get more samples

        for parameter in self.deviceList:
            print("The max value is: " + parameter.maxValue + "\n")
            print("Biggest: " + parameter.value[2] + "\n")
            print("Average: " + parameter.value[1] + "\n")
            print("Lowest: " + parameter.value[0] + "\n")