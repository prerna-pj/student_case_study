This is a data engineering case study a sample students dataset


## Create and activate a virtual environment (recommended but optional)
For windows:
1. Set up a virtual environment `python -m venv venv`
2. Activate the virtual environment `venv\Scripts\activate`

## How to run this python solution
1. When running for the first time, please install the required packages in the `requirements.txt` file using pip
```
pip install -r requirements.txt
```
2. Run the python script
```
python main.py
```


## Folder structure for this project
1. `./log/`: Location to store the log files
2. `./sql/`: Location to store all the sql queries that might be used in future
3. `./sql/sql_query.sql`: Contains sample sql queries against few business use cases
4. `./input/`: Location to store input source data
5. `./util/logger.py`: Common library designed for the purpose of logging
6. `./util/sqlite_conn.py`: Python DWH utility that uses sqlite database to store the files
7. `student.db`: SQLite Database file storing all the tables structure and data for this project
8. `requirements.txt`: A file containing all the python libraries used in this project that needs to be installed. Please check and keep this updated inorder to install all the libraries used at once using the command `pip install -r requirements.txt`
9. `./config/`: Stires the configuration

## Tables structure for the cocktail_drinks problem statement
### 1. student
This table contains the details of all the students with other details.
```
Primary key: id
```


## How you use the sqlite database
The data is currently being stored in a sqlite database `student.db`. You can view the database and tables using below steps:
1. Download any DB browser App for SQLite
2. Open the database file `student.db` in the above app
3. Query any run your sql. For sample queries, please use the one from `./sql/sql_query.sql`

## Assumptions

## Future Enhancement

