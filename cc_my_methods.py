import pandas as pd
import numpy as np


def drop_if_many_missing(df):
    """
    Drop rows if more than half of the columns are missing.
    """
    return df.dropna(thresh=len(df.columns)//2, axis=1)


