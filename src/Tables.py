import sqlite3


class Tables:
    conn = sqlite3.connect('snmp.sqlite')

    cursor = conn.cursor()

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
    
    conn.commit()
    
    conn.close()
