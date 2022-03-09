from User import User
from Database import Database

class Controller:
    def __init__(self):
        self.my_user = User()
        self.db = Database('snmp-watch.db')
        
    def LoginSetUserCredentials(self, username, password):
        self.my_user.setUsername()
        self.my_user.setPassword()

        self.db.connect()

        if self.db.checkLogin(self.my_user.getUsername(), self.my_user.getPassword()):
            sucess = True
            print("Valid Login!")
        else:
            sucess = False
            print("Invalid Login")
    
        db.close()
        return sucess

    def createAppView():
        print("Going to create an App view")