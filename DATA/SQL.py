import sqlite3
from DATA.class_methods import Logging

def create_connection(db_file = "logged.db"):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logs 
                  (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                   log TEXT NOT NULL,message TEXT NOT NULL,
                   timespent INTEGER NOT NULL,
                    timestamp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    module TEXT NOT NULL)'''
    )

    conn.commit()

def add_logs(conn, logs):
    cursor = conn.cursor()

    data = Logging.from_list_to_tuple(logs)

    cursor.executemany("""INSERT INTO logs (log, message, module, timespent) 
                      VALUES (?, ?, ?, ?)""", data)

    conn.commit()