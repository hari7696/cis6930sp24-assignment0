from utilities import *
from db_components import *
import argparse

def main(url):

    # downloading the pdf file
    pdf_byte_stream = download_pdf(url)

    # parsing the pdf file
    df = pdf_parser(pdf_byte_stream)

    # creating the database
    conn = createdb()
    create_table(conn)

    # populating the database
    populate_db(conn, df)
    conn.commit()

    #querying db
    query = '''SELECT Nature, count(*) as num_incidents FROM incidents GROUP BY Nature ORDER BY num_incidents DESC, Nature;'''

    query_output = query_db(conn, query)
    for row in query_output:
        print("|".join(map(str, row)))

    conn.close()

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)