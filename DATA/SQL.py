import sqlite3

def create_connection(db_file = "logged.db"):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logs 
                  (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                   log TEXT NOT NULL,message TEXT NOT NULL,
                   time_spent INTEGER NOT NULL,
                    timestamp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    module TEXT NOT NULL)'''
    )

    conn.commit()



