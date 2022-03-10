import sqlite3

class Database:
    def __init__(self, databaseName):
        self._databaseName = ""
        self.setDatabaseName(databaseName)
        
        self.conn = None
        self.connect()

        cursor = self.conn.cursor()

        cursor.execute(""" 
                    CREATE TABLE IF NOT EXISTS login (
                        user_id INTEGER PRIMARY KEY,
                        user TEXT not null,
                        password TEXT
                    ); """)

        cursor.execute(""" 
                    CREATE TABLE IF NOT EXISTS agent (
                        user_id INTEGER,
                        agent_id INTEGER,
                        ip_addr TEXT,
                        auth_user TEXT,
                        auth_cred TEXT,
                        priv_user TEXT,
                        priv_cred TEXT, 
                        FOREIGN KEY (user_id) REFERENCES login (user_id),
                        CONSTRAINT pk_UA primary key(user_id, agent_id)
                    ); """)

        cursor.execute(""" 
                    CREATE TABLE IF NOT EXISTS log (
                        log_id INTEGER,
                        user_id INTEGER,
                        data DATE,
                        hora TIME,
                        min REAL,
                        average REAL,
                        max REAL,
                        FOREIGN KEY (user_id) REFERENCES login (user_id),
                        CONSTRAINT pk_UL primary key(user_id, log_id)
                    ); """)

        #Created default user to test if DB works properly
        cursor.execute("""
                    INSERT OR REPLACE INTO login (user_id, user, password) VALUES (0, 'root', 'toor')
                    """)

        self.conn.commit()
   
        self.close()

    def connect(self):
        self.conn = sqlite3.connect( self.getDatabaseName() )
    
    def close(self):
        #self.conn value after close is None? need to check
        self.conn.close()

    def setDatabaseName(self, databaseName):
        ##do some checking with database name
        self._databaseName = databaseName
    
    def getDatabaseName(self):
        return self._databaseName

    def checkLogin(self, username, password):
        #test self.conn value
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT password FROM login WHERE user = ?;
            """, (username,)) 
        
        login_list           = cursor.fetchall()
        # if 0, no user with this username, if more than 1 there's 2 users with same username(not user_id)
        # but not a desirable behavior 
        if len(login_list) == 0:                    
            return False

        password_line       = login_list[0]          # assuming there is 1 valid user      
        password_correct    = password_line[0]

        print("User Input password: " + password)
        print("DB correct password: " + password_correct)
        
        return password == password_correct

    def existUsername(self, username):
        invalid_user_id = -1

        cursor = self.conn.cursor()

        cursor.execute(""" 
            SELECT user_id FROM login WHERE user=?
        """, (username,))

        login_list = cursor.fetchall() 

        if len(login_list) == 0:
            return invalid_user_id          # invalid user_id - no such user
        else:
            login_line = login_list[0]
            return login_line[0]            # user_id

    def addUser(self, username, password):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT count(user_id) FROM login
        """)

        login_list = cursor.fetchall()
        login_line  = login_list[0]
        
        newUID = (int)(login_line[0]) # if there is 2 users, uid: 0 and 1, next will be 2 = count(user_id)

        print(str(newUID) + ' ' + username + ' ' + password)

        cursor.execute("""
            INSERT INTO login (user_id, user, password) VALUES (?,?,?)
        """, (newUID, username, password))

        self.conn.commit()

        return newUID

    def addAgent(self, device, user_id):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT count(user_id) FROM agent WHERE user_id = ?      
        """, (user_id,))

        agent_list  = cursor.fetchall()
        agent_line  = agent_list[0]
        agent_id    = (int)(agent_line[0])

        print("id: " + str(user_id) + " has " + str(numero_agentes) + "agents.")

        cursor.execute("""
            INSERT INTO agent (user_id, agent_id, ip_addr, auth_user, auth_cred, priv_user, priv_cred) VALUES (?,?,?,?,?,?,?)
        """, (user_id, agent_id, device.ip_addr, device.auth[0], device.auth[1], device.auth[0], device.auth[1]))

        self.conn.commit()

    def searchAgentsFromUser(self, user):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT * FROM agent WHERE user_id = ?
        """, (user.getUserId(),))

        agent_list = cursor.fetchall()

        return agent_list