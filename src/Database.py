import sqlite3

class Database:
    def __init__(self, databaseName)
        self._databaseName = ""
        self.setDatabaseName(databaseName)
        
        self.conn = None
        self.connect()

        self.cursor = self.conn.cursor()

        self.cursor.execute(""" 
                    CREATE TABLE IF NOT EXISTS login (
                        user_Id INTEGER PRIMARY KEY,
                        user TEXT not null,
                        password TEXT
                    ); """)

        self.cursor.execute(""" 
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

        self.cursor.execute(""" 
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
    
        self.conn.commit()
        self.close()

    def connect(self):
        self.conn = sqlite3.connect( getDatabaseName() )
    
    def close(self):
        self.conn.close()

    def setDatabaseName(self, databaseName):
        ##do some checking with database name
        self._databaseName = databaseName
    
    def getDatabaseName(self):
        return self._databaseName