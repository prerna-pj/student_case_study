This is a data engineering case study for a sample students dataset


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
9. `./config/`: Stores the configuration


## How you use the sqlite database
The data is currently being stored in a sqlite database `student.db`. You can view the database and tables using below steps:
1. Download any DB browser App for SQLite
2. Open the database file `student.db` in the above app
3. Query any run your sql. For sample queries, please use the one from `./sql/sql_query.sql`

## Assumptions
1. As per the schema definition in the Student Course link (https://archive.ics.uci.edu/dataset/320/student+performance), there isn't any null/missing values. So, I am not handling it.
2. Since there is not id defining the uniqueness in the source data. I am considering the date to be unique and non-duplicate, since two or more students can have same information.
3. As per the sql queries, it seems that the table is mostly used for student analysis, so I have kept it in a single table as it is. But id its not the case we, can remodel the original data into smaller tables as:
    
    a. student_course_details:
    ```
    Columns schema: id, school, reason, traveltime, studytime, failures, schoolsup, famsup, paid, 
        activities, nursery, higher, absences, G1, G2, G3, student_id
    Primary Key: id
    Foreign Key: student_id <> id.student_personal_details
    ```

    b. student_personal_details:
    ```
    Columns schema: id, sex, age, address, famsize, Pstatus, Medu, Fedu, Mjob, Fjob, guardian,
        internet, romantic, famrel, freetime, goout, Dalc, Walc, health, 
    Primary Key: id
    Foreign_id: Mjob <> job_id.job_details, 
        Fjob <> job_id.job_details, 
        Medu <> id.parent_education_details, 
        Fedu <> id.parent_education_details
    ```

    c. job_details: Contains the list of all the different possible jobs for Mjob and Fjob attribute
    ```
    Columns schema: job_id, job_name
    Primary Key: job_id
    ```

    d. parent_education_details
    ```
    Columns schema: id, education_level
    Primary Key: id
    ```

    e. [Optional] score : We can also have this table to store the score of the status against each value
    eg: To store the numeric: from 1 - very low to 5 - very high
    ```
    Columns schema: score_id, description
    Primary Key: score_id
    
    score_id| description
    1       | Very Low
    2       | Low
    3       | Average
    4       | High
    5       | Very High
    ```
