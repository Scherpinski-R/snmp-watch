from User import User
from Database import Database
from Device import Device

class Controller:
    def __init__(self):
        self.my_user = User()
        self.db = Database('snmp-watch.db')
        
    def LoginSetUserCredentials(self, username, password):
        self.my_user.setUsername(username)
        self.my_user.setPassword(password)

        self.db.connect()

        login_id = self.db.checkLogin(self.my_user.getUsername(), self.my_user.getPassword())
        self.my_user.setUserId(login_id)

        invalid_id = -1                 #constant invalid_id
    
        self.db.close()
        return login_id != invalid_id
    
    def RegisterSetUserCredentials(self, username, password):
        self.my_user.setUsername(username)
        self.my_user.setPassword(password)

        self.db.connect()

        if self.db.existUsername( self.my_user.getUsername() ) != -1:
            print("Username already in use")
            sucess = False
        else:
            newUID = self.db.addUser( self.my_user.getUsername(), self.my_user.getPassword() )
            self.my_user.setUserId( newUID )
            sucess = True

        self.db.close()
        return sucess

    def createAppView(self):
        print("Going to create an App view")

        self.db.connect()
        #usuario forneceria numa entry os dados abaixo
        device = Device('Device-01', '192.168.0.106', ('MD5DESUser','The Net-SNMP Demo Password'), ('MD5User', 'The Net-SNMP Demo Password'))
        self.db.addAgent(device, self.my_user)
        #essa lista alimentaria um canvas com varias opcoes de sessoes
        list_agents = self.db.searchAgentsFromUser(self.my_user)
        #ao usuario apertar um botao, receberiamos o agent_id + user_id e preencheriamos uma estrutura device   
        device.createSession()
        #apos receber feedBack da perform analytics adicionaria o ultimo resultado ao DB e mostraria ao usuario as ultimas N analises
        device.performAnalytics()


        self.db.close()
        print(list_agents)