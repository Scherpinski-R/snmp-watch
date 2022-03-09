import sqlite3

class Database:
    def __init__(self, databaseName)
        self._databaseName = ""
        self.setDatabaseName(databaseName)
        
        self.conn = None
        self.connect()

        cursor = self.conn.cursor()

        cursor.execute(""" 
                    CREATE TABLE IF NOT EXISTS login (
                        user_Id INTEGER PRIMARY KEY,
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
                        user_Id INTEGER PRIMARY KEY,
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
                    INSERT INTO login (user_Id, user, password) VALUES (0, root, toor)
                    """)

        self.conn.commit()
   
        self.close()

    def connect(self):
        self.conn = sqlite3.connect( getDatabaseName() )
    
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
            SELECT password FROM login WHERE user = ?
            """, username) 
        
        # will change to return some boolean if valid
        for linha in cursor.fetchall():
            print(linha)
        
        return True
        

