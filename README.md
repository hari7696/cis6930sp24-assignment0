# cis6930sp24-assignment0

Name: Hari Kirshna Reddy Golamari

# Project Description

The project involes fetching and processing a PDF file from the Norman Police Department website [here](https://www.normanok.gov/) and generating a summary report. The PDF file contains information about incidents reported to the department. 

Once the data from the PDF file is converted into a structured format, it will be inserted into a database. I am using SQLite as the database for this project. 

Finally, a summary query will be executed on the SQLite database to provide insights and analysis on the nature of the reported incidents.

### project implementation Steps

1. Data Acquisition
2. Data Extraction and Transformation
3. Database Insertion
4. Summary report

### Expected outcomes
1. Automated retrieval and processing of the latest police reports from the Norman Police Department.
2. A reliable database containing data in a structured format.
3. a standard out report contianing summary on incidents nature

### Environment setup
Run the follwing pipenv command to create the required environment
```pipenv install```

### How to run


https://github.com/hari7696/cis6930sp24-assignment0/assets/148893192/c1983b85-14fe-4263-9af0-cec14cd52c0a

Run the follwing pipenv commands to execute the program


```pipenv install```
```pipenv run python assignment0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2024-01/2023-12-31_daily_incident_summary.pdf```
### Test cases run

The test doesnt need any explicit inputs, running following pipenv command run the pytest cases. The project have 6 test cases.

```pipenv run python -m pytest```

## Functions


main()
    
    The is the caller function, it calls different modules in a sequence. The output of the function is a report printed via stdout
    
    Downloads a PDF file from the given URL, parses it, creates a database, populates the database with data from the PDF,
    executes a query on the database, and prints the query results.

    Parameters:
    url (str): The URL of the PDF file to download.

    Returns:
    None

download_pdf()
    
    Function to download a PDF file from a given URL.

    Parameters:
    url (str): The URL of the PDF file to be downloaded.

    Returns:
    io.BytesIO: A BytesIO object containing the downloaded PDF file.

    Raises:
    urllib.error.URLError: If there is an error while opening the URL.

pdf_parser()

    Function to parse the pdf file and return the dataframe.

    Parameters:
    pdf_stream (bytes): The byte stream of the PDF file.

    Returns:
    pandas.DataFrame: The parsed data as a DataFrame.

    Details:
    This function takes a byte stream of a PDF file and extracts the data from it. It assumes that the PDF file
    has a specific structure with field names in a certain row and a fixed number of fields per row. The function
    uses the PyPDF2 library to read the PDF file and extract the text from each page. It then splits the extracted
    text into lines and processes each line to extract the field values. Junk lines that do not have the expected
    number of fields are removed. Finally, the extracted data is converted into a pandas DataFrame and returned.

    Note:
    - The behavior of this function can be unpredictable if the PDF format/structure changes.
    - The PyPDF2 library is required to run this function.


split_line_regex()

    """
    Split the line based on the regex pattern.

    Parameters:
    line (str): The input line to be split.

    Returns:
    list: A list of strings after splitting the line based on the regex pattern."""

createdb()
   
    Creates a new SQLite database and returns a connection object.

    Returns:
        conn (sqlite3.Connection): Connection object representing the newly created database.
    

create_table()
    
    Creates a table named 'incidents' in the database.

    Parameters:
    conn (Connection): The database connection object.

    Returns:
    None

populate_db()
    
    Populates the database with data from a DataFrame.

    Parameters:
    conn (Connection): The database connection object.
    df (DataFrame): The DataFrame containing the data to be inserted into the database.

    Returns:
    None

    Details:
    - Renames the columns of the DataFrame to ['incident_time', 'incident_number', 'incident_location', 'nature', 'incident_ori'].
    - Inserts the data from the DataFrame into the 'incidents' table in the database.
    - If the 'incidents' table already exists, the data is appended to it.
    - Logs a debug message with the column names of the DataFrame.
    - Logs an info message indicating that the database has been populated.

query_db()
    
    Execute a database query.

    Parameters:
    conn (connection): The database connection object.
    query (str): The SQL query to be executed.

    Returns:
    result (object): The result of the query execution.
    """

## Database Development

SQLite is used in this project for database development due to its lightweight nature and ease of use. 
SQLite is a self-contained, serverless, and zero-configuration database engine that allows for easy integration into applications. 

In the context of this project, SQLite is a suitable choice because it provides a simple and efficient way to store and query data. 
It does not require a separate database server to be installed or configured, making it convenient for development and deployment. 
Additionally, SQLite supports standard SQL syntax, making it compatible with existing SQL-based tools and libraries.

In this project a simple table 'indicents' with five fileds 
['incident_time', 'incident_number', 'incident_location', 'nature', 'incident_ori'] is created and the datatypes for all the fields is TEXT

```
        CREATE TABLE incidents (
                incident_time TEXT,
                incident_number TEXT,
                incident_location TEXT,
                nature TEXT,
                incident_ori TEXT
            );
```
During the data insertion, the inbuit functionality of pandas dataFrame ```to_sql``` is used, 
as its the quickest way with out the need of any explicit code that require iterations.
The pandas library automatically matches the field names present in dataframe with the table fields and performs the records insertion

The following SQL query is developed to get the summary on the incidents nature

```SELECT nature, count(*) as num_incidents FROM incidents GROUP BY nature ORDER BY num_incidents DESC, nature;```

## Bugs and Assumption

1. Extracting data pdf is really complicated, so if the structure of the changes from the given incident file, 
    the behaviour od the code can be unpredicatable, it may even break
2. For the expected outcome, its assumed that the structure of the pdf file remains same as given in assignment
3. The code should have write access to the resources directory
4. Assumption: the fields present in pdf will be in the order ['incident_time', 'incident_number', 'incident_location', 'nature', 'incident_ori']
5. Asuumption: the first 2 rows of the pdf is junk data, so it gets removed everytime
6. The last row of the pdf have a time stamp, so its ignroed as junk value



