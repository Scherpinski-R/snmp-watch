class User:
    def __init__(self):
        self._userId    = -1
        self._username   = ''
        self._password   = ''

    def getUsername(self):
        return self._username

    def setUsername(self, username):
        # validate
        self._username = username

    def getPassword(self):
        return self._password

    def setPassword(self, password):
        # validate
        self._password = password

    def getUserId(self):
        return self._userId

    def setUserId(self, user_id):
        self._userId = user_id