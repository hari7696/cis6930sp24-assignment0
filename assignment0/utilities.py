import pandas as pd
import urllib.request
from pypdf import PdfReader
import io
import pickle
import re

def download_pdf(url):

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          
    data = io.BytesIO(urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read())   

    #pickle.dump(data, open('filename', 'wb'))                                                                            

    return data 

def split_line_regex(line):

    lst_str =  re.split(r'\s{2,}', line)
    lst_str = [item.strip() for item in lst_str]
    return lst_str


# unit test
#https://stackoverflow.com/questions/66870366/pypdf2-extracting-all-pages-and-converting-to-csv

def pdf_parser(pdf_stream):

    PAGE_ONE = True
    EXPECTED_FIELDS = 5
    NUMBER_OF_JUNK_LINES = 3
    FIELD_NAMES_ROW = 2

    lst_lines = []
    #pdf_file = PdfReader(pickle.load(open('filename', 'rb')))
    pdf_file = PdfReader(pdf_stream)
    pdf_file.pages[0].extract_text()
    for page in pdf_file.pages:
        
        # extracting the context with layout method, the behavior can be truly unpredictable if the pdf format/structure changes
        page_extract = page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False).split('\n')
    
        if PAGE_ONE is True:

            # extracting the field names
            field_names = split_line_regex(page_extract[FIELD_NAMES_ROW])[1:]
            # removing the junk lines
            page_extract = page_extract[NUMBER_OF_JUNK_LINES:]
            PAGE_ONE = False
        
        # splitting the extracted line for respective field values
        lst_lines.extend([split_line_regex(item) for item in page_extract])
        
        # there might be some junk rows which might not have all the fields, so removing them
        lst_lines = [item for item in lst_lines if len(item) == EXPECTED_FIELDS]

    # creating the dataframe
    df = pd.DataFrame(lst_lines, columns = field_names)

    #df.to_csv('resources/temp.csv')

    return df







if __name__ == '__main__':
    #pdf_stream = download_pdf('https://www.normanok.gov/sites/default/files/documents/2024-01/2023-12-31_daily_incident_summary.pdf', '/tmp/test.pdf')
    
    print(pdf_parser('pdf_stream'))