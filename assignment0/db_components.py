import sqlite3
import os
def createdb():

    #chekcing if there as existing db
    if os.path.exists('resources/test.db'):
        os.remove('resources/test.db')
    conn = sqlite3.connect('resources/test.db')
    return conn 

def create_table(conn):

    conn.execute('''CREATE TABLE incidents
                 ("Date / Time" TEXT NOT NULL, 
                 "Incident Number" TEXT NOT NULL,  
                 Location TEXT NOT NULL, 
                 Nature TEXT NOT NULL, 
                 "Incident ORI" TEXT NOT NULL);''')
    
def populate_db(conn, df):
    df.to_sql('incidents', conn, if_exists='append', index=False)

def query_db(conn, query):
    return conn.execute(query)

if __name__ == '__main__':
    conn = createdb()
    create_table(conn)
    df = pd.read_csv('resources/temp.csv')
    populate_db(conn, df)
    conn.commit()
    conn.close()
    