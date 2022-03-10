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
                        user_Id INTEGER PRIMARY KEY,
                        user TEXT not null,
                        auth_user TEXT,
                        auth_cred TEXT,
                        priv_user TEXT,
                        priv_cred TEXT,
                        FOREIGN KEY (user_id)
                        REFERENCES login (user_id)
                    ); """)

        cursor.execute(""" 
                    CREATE TABLE IF NOT EXISTS log (
                        user_id INTEGER PRIMARY KEY,
                        data DATE,
                        hora TIME,
                        min REAL,
                        average REAL,
                        max REAL,
                        FOREIGN KEY (user_id)
                        REFERENCES login (user_id)
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

        return newUID