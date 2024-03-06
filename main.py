import pandas as pd
from utils.load_config import config
from utils.sql_conn import SQLiteConnection
from utils.logger import setup_logger


# create a logger instance
logger = setup_logger()

# Load configuration
CONFIG = config("config/config.yaml", "yaml")
INPUT_PATH = CONFIG["input_path"]
TABLE_NAME = CONFIG["table_name"]
LOG_FILE = CONFIG["log_file"]


# create a sqlite db connection
sqlite_db = SQLiteConnection(db_name=CONFIG["sqlite_db"])
sqlite_db.connect()


def extract_csv_file(input_path:str, delimiter:str)-> pd.DataFrame:
    """
    Extract data from csv files
    Parameters
    - input_path: Source csv input file location
    - delimiter: Delimeter used in the input csv file to separate the column values
    Return
    - return df: pandas dataframe
    """
    df = pd.read_csv(input_path, delimiter=delimiter)
    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform the data
    Parameters:
    - df: Dataframe containing imported contracts data
    Return:
    df: Transformed df
    """
    return df


def load_to_dwh(table_name: str, df: pd.DataFrame, insert_type: str) -> None:
    """
    Load the data into a Sqlite darawarehouce
    Parameters:
    - tablename: Name of the table where data needs to be inserted
    - df: Pandas dataframe that needs to be inserted into the DWH
    - insert_type: Behavior of insert if the table already exists. ['fail', 'replace', 'append']
    """
    sqlite_db.insert_dataframe(table_name=table_name, df=df, insert_type=insert_type)
    logger.info(f"{table_name} data inserted into DWH")


def etl_pipeline():
    """
    To design the layout of the student etl pipeline
    """
    # Extract data
    print(f"INPUT_PATH = {INPUT_PATH}")
    input_df = extract_csv_file(input_path=INPUT_PATH, delimiter=';')
    logger.info(f"Step 1. Date extracted from source.")

    print(input_df.columns)
    print(input_df.dtypes)
    print(input_df.head(10))


    # Load the data in DWH
    load_to_dwh(table_name=TABLE_NAME, df=df, insert_type='replace')
    logger.info(f"Step 3. Date loaded into DWH.")

    sqlite_db.close_connection()


if __name__ == "__main__":

    etl_pipeline()
