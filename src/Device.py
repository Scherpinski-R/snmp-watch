from easysnmp import Session

from DeviceParameter import DeviceParameter


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

            current_value   = self._session.get(parameter.getParameterName())

            # do smth with value - prob compare with min, max and add to create new avg with deviceParameter methods
            print(value)
