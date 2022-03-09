from Device import Device
from Database import Database

def main():

    # login
    username = 'root'
    password = 'toor'
    # check in db login credentials
    db = Database('snmp-watch.db')

    db.connect()
    
    if db.checkLogin(username, password):
        print("Valid Login!")
    else:
        print("Invalid Login")
    
    db.close()

    # choose wich agent to run analytics or create new profile(new agent)
    # create Session for the chosen agent
    # perform analytics
    # display result
    ## store in db

    # ....skiping first 3 steps
    # device chosen somehow:
    device = Device('Device-01', '192.168.0.106', ('MD5DESUser','The Net-SNMP Demo Password'), ('MD5User', 'The Net-SNMP Demo Password'))

    device.createSession()
    # prob gonna change this function to return a tuple wich will feed some graphical engine
    device.performAnalytics()


if __name__ == '__main__':
    main()
