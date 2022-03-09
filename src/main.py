from User import User
from Device import Device
from Database import Database
from Login import Login
from Controller import Controller

def main():

    myController    = Controller()
    myLoginView     = Login(myController)

    # Registering UserCase
    #uid = db.existUsername( my_user.getUsername() )
    #if uid == -1:
   #     print("Username avaiable, registering...")
    #    uid = db.addUser( my_user.getUsername(), my_user.getPassword() )
  #  else:
 #       print("Username not avaiable!")
                
#    my_user.setUserId(uid)

    # Generic Login UserCase
    #if db.checkLogin(my_user.getUsername(), my_user.getPassword()):
    #    print("Valid Login!")
    #else:
    #    print("Invalid Login")
    
    # choose wich agent to run analytics or create new profile(new agent)
    # create Session for the chosen agent
    # perform analytics
    # display result
    ## store in db

    # ....skiping first 3 steps
    # device chosen somehow:
    #device = Device('Device-01', '192.168.0.106', ('MD5DESUser','The Net-SNMP Demo Password'), ('MD5User', 'The Net-SNMP Demo Password'))

    #device.createSession()
    # prob gonna change this function to return a tuple wich will feed some graphical engine
    #device.performAnalytics()


if __name__ == '__main__':
    main()
