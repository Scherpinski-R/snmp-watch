from User import User
from Database import Database

class Controller:
    def __init__(self):
        self.my_user = User()
        self.db = Database('snmp-watch.db')
        
    def LoginSetUserCredentials(self, username, password):
        self.my_user.setUsername(username)
        self.my_user.setPassword(password)

        self.db.connect()

        if self.db.checkLogin(self.my_user.getUsername(), self.my_user.getPassword()):
            sucess = True
            print("Valid Login!")
        else:
            sucess = False
            print("Invalid Login")
    
        self.db.close()
        return sucess
    
    def RegisterSetUserCredentials(self, username, password):
        self.my_user.setUsername(username)
        self.my_user.setPassword(password)

        self.db.connect()

        if self.db.existUsername( self.my_user.getUsername() ) != -1:
            print("Username already in use")
            return False
        else:
            newUID = self.db.addUser( self.my_user.getUsername(), self.my_user.getPassword() )
            self.my_user.setUserId( newUID )
            return True

    def createAppView(self):
        print("Going to create an App view")