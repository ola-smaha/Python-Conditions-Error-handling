from enum import Enum

class Errors(Enum):
    CONNECTION_ERROR = "Error connecting to the database, "
    RETURN_QUERY_ERROR = "Error: Cannot return query, "
    CSV_RETURN_ERROR = "Error: can't return csv file, "
    SQL_RETURN_ERROR = "Error: can't return sql query, "
    EXCEL_RETURN_ERROR = "Error: can't return excel file, "
    UNDEFINED_DATA_ERROR = "Error: data type is undefined,"
    NO_ERROR = "Executed Successfully,"
    EXECUTION_ERROR = "Error executing query, "
    REMOVE_DUPLICATES_ERROR = "Error removing duplicates, "
    REMOVE_NULLS_ERROR = "Error removing null values, "
    GET_BLANKS_ERROR = "Error getting nan values, "
    GET_SHAPE_ERROR = "Error getting dataframe shape, "
    GET_LENGTH_ERROR = "Error getting counts, "


class Types(Enum):
    SQL = 'sql'
    EXCEL = 'xlsx'
    CSV = 'csv'

class PandasFunctions(Enum):
    REMOVE_DUPLICATES = "remove duplicated rows."
    REMOVE_NULLS = "delete rows containing null values."
    GET_BLANKS = "find instances with nan values."
    GET_SHAPE = "get dataframe shape (rows,columns)."
    GET_LENGTH = "find the length of each dataframe column."