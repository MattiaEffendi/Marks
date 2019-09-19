import sqlite3
import config
import sys
from logbook import Logger
conn = sqlite3.connect(config.DATABASE_FILE_NAME + '.db')
c = conn.cursor()
log = Logger('First start')


def first_start():
    try:
        query = (
            "CREATE TABLE Utenti(IDU INTEGER PRIMARY KEY AUTOINCREMENT,"
            " ID INT, State TEXT)"
        )
        c.execute(query)
        conn.commit()
        info = (
            "Database has been created and setup! Please set the FIRST_START "
            "boolean in config.py as False and restart the bot!"
        )
        log.info(info)
        sys.exit(0)
    except sqlite3.OperationalError as e:
        warn = (
            "It means you have run the bot with the FIRST_START boolean "
            "in config.py as True even though it isn't the first start. "
            "Please set the flag as False in order to start the bot."
        )
        log.warn(warn)
        print(str(e))
        sys.exit(0)
