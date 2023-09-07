import pandas as pd
from lookups import PandasFunctions, Errors
from logging_handler import display_error

def pandas_function(df,function):
    try:
        if function == PandasFunctions.REMOVE_DUPLICATES:
            return df.drop_duplicates()
        elif function == PandasFunctions.REMOVE_NULLS:
            return df.dropna()
        elif function == PandasFunctions.GET_BLANKS:
            return df[df.isna()]
        elif function == PandasFunctions.GET_SHAPE:
            return df.shape
        elif function == PandasFunctions.GET_LENGTH:
            return df.count()
        else:
            raise Exception("Failed. Use pandas function manually.")
    except Exception as e:
        error_msg = str(e)
        if function == PandasFunctions.REMOVE_DUPLICATES:
            enum_error = Errors.REMOVE_DUPLICATES_ERROR.value
        elif function == PandasFunctions.REMOVE_NULLS:
            enum_error = Errors.REMOVE_NULLS_ERROR.value
        elif function == PandasFunctions.GET_BLANKS:
            enum_error = Errors.GET_BLANKS_ERROR.value
        elif function == PandasFunctions.GET_SHAPE:
            enum_error = Errors.GET_SHAPE_ERROR
        elif function == PandasFunctions.GET_LENGTH:
            enum_error = Errors.GET_LENGTH_ERROR
        display_error(enum_error,error_msg)

    