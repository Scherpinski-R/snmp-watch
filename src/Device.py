from easysnmp import Session

import DeviceParameter


class Device:
    def __init__(self, deviceAlias, deviceIp, authCred, cryptCred, privCred):
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
        self.parameterNameList = ['hrStorageSize.1',
                             'hrStorageSize.3', 'hrSystemProcesses']

        self.deviceList = []
        self.populateParameterList()

    def createSession(self):
        self._session = Session(hostname=self.ipAddr, version=3, security_level="auth_with_privacy", auth_protocol="MD5",
                                security_username=self.auth[0], auth_password=self.auth[1], privacy_protocol="DES", privacy_password=self.priv[1])

        if self._session == None:
            print("LOG: Failed to create Session")

    def populateParameterList(self):
        for parameter in self.parameterNameList:
            self.deviceList.append(DeviceParameter(parameter))

    def performAnalytics(self):
        if self._session == None:
            print("LOG: Session not Created")
            return

        for parameter in self.deviceList:
            value = self._session.get(parameter.getParameterName())

            # do smth with value - prob compare with min, max and add to create new avg with deviceParameter methods
            print(value)
