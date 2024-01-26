import sqlite3
import os
import logging
logger = logging.getLogger(__name__)

def createdb():

    abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
    print(abs_path,)
    #chekcing if there as existing db
    if os.path.exists(os.path.join(abs_path, 'resources', 'test.db')):
        os.remove(os.path.join(abs_path, 'resources', 'test.db'))
        logger.debug("Removed the existing db")

    conn = sqlite3.connect(os.path.join(abs_path, 'resources', 'test.db'))
    logger.info("Created the db")
    return conn 

def create_table(conn):

    conn.execute('''CREATE TABLE incidents (
                    incident_time TEXT,
                    incident_number TEXT,
                    incident_location TEXT,
                    nature TEXT,
                    incident_ori TEXT
                );''')
    logger.info("table creation successful")
    
def populate_db(conn, df):

    df.columns = ['incident_time', 'incident_number', 'incident_location', 'nature', 'incident_ori']
    logger.debug("columns names {}".format(df.columns))
    df.to_sql('incidents', conn, if_exists='append', index=False)
    logger.info("Populated the db")

def query_db(conn, query):
    return conn.execute(query)

