import pytest
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from assignment0.utilities import download_pdf, pdf_parser, split_line_regex
from assignment0.db_components import createdb, create_table, populate_db, query_db

def test_download_pdf():
    url = 'https://www.normanok.gov/sites/default/files/documents/2024-01/2023-12-31_daily_incident_summary.pdf'
    pdf_stream = download_pdf(url)
    assert pdf_stream is not None

def test_split_line_regex():
    line = '12/31/2023 00:00:00         2023-00000001       100 Blk W Boyd St      Traffic Stop         OK0140200'
    lst_str = split_line_regex(line)
    assert lst_str == ['12/31/2023 00:00:00', '2023-00000001', '100 Blk W Boyd St', 'Traffic Stop', 'OK0140200']

def test_pdf_parser():
    pdf_stream = download_pdf('https://www.normanok.gov/sites/default/files/documents/2024-01/2023-12-31_daily_incident_summary.pdf')
    df = pdf_parser(pdf_stream)
    assert len(df) > 0

def test_createdb():
    conn = createdb()
    assert conn is not None
    conn.close()

def test_create_table():
    conn = createdb()
    create_table(conn)
    assert conn.execute('''SELECT count(*) FROM incidents;''').fetchone()[0] == 0
    conn.close()

def test_populate_db():
    conn = createdb()
    pdf_stream = download_pdf('https://www.normanok.gov/sites/default/files/documents/2024-01/2023-12-31_daily_incident_summary.pdf')
    df = pdf_parser(pdf_stream)
    populate_db(conn, df)
    assert conn.execute('''SELECT count(*) FROM incidents;''').fetchone()[0] > 0
    conn.close()

