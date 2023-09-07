import pandas as pd
from lookups import PandasFunctions

def pandas_function(df,function):
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
    