import psycopg2
from lookups import Errors, Types
from logging_handler import display_error
import time 
import pandas as pd

connection_dict = {
    'dbname' : 'dvd_rental',
    'user' : 'postgres',
    'host' : 'localhost',
    'password' : 'admin',
    'port' : 5432
}

def create_connection():
    session = None
    try:
        session = psycopg2.connect(
            database = connection_dict.get('dbname'),
            user = connection_dict.get('user'),
            host = connection_dict.get('host'),
            password = connection_dict.get('password'),
            port = connection_dict.get('port')
        )
    except Exception as e:
        error_enum = Errors.CONNECTION_ERROR.value
        error_message = str(e)
        display_error(error_enum, error_message)
    finally:
        return session


def refresh_connection(session):
    session.close()
    time.sleep(3)
    session = create_connection()
    return session


def close_connection(session):
    session.close()


def return_as_df(data_source, file_type, session = None):
    return_df = None
    try:
        if file_type == Types.SQL:
            return_df = pd.read_sql_query(con = session, sql = data_source)
        elif file_type == Types.CSV:
            return_df = pd.read_csv(data_source)
        elif file_type == Types.EXCEL:
            return_df = pd.read_excel(data_source)
        else:
            raise Exception('Undefined file type.')
    except Exception as e:
        error_msg = str(e)
        if file_type == Types.CSV:
            error_enum = Errors.CSV_RETURN_ERROR.value
        elif file_type == Types.EXCEL:
            error_enum = Errors.EXCEL_RETURN_ERROR.value
        elif file_type == Types.SQL:
            error_enum = Errors.SQL_RETURN_ERROR.value
        else:
            error_enum = Errors.UNDEFINED_DATA_ERROR.value
        display_error(error_enum, error_msg)
    finally:
        return return_df
    

def return_query(session,query):
    output = None
    try:
        cursor = session.cursor()
        cursor.execute(query)
        output = cursor.fetchall()
        session.commit()
    except Exception as e:
        error_enum = Errors.RETURN_QUERY_ERROR.value
        error_message = str(e)
        display_error(error_enum,error_message)
    finally:
        return output


def execute_query(session, query):
    try:
        cursor = session.cursor()
        cursor.execute(query)
        session.commit()
        print(Errors.NO_ERROR.value)
    except Exception as e:
        execute_enum = Errors.EXECUTION_ERROR.value
        error_msg = str(e)
        display_error(execute_enum,error_msg)


def get_schema_information(db_session):
    query = """
        SELECT *
        FROM information_schema.columns
        WHERE table_schema = 'public'
    """
    info_schema_df = return_as_df(data_source=query, file_type=Types.SQL, session = db_session)
    return info_schema_df

