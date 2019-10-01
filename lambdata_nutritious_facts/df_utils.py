"""
utility for working with DataFrames
"""

import pandas as pd
import numpy as np

class Edit:
    """
    this class lets you edit a dataframe
    """

    def __init__(self,df = pd.DataFrame(np.ones(5))):
        self.df = df
    
    def add_col(self,df,lst,name = "New_column"):
        """
        this function will add a new column to the end of a dataframe

        Parameters:
        
        df: a dataframe
        lst: a list of values to use as column cells
        name: the name of the column

        """
        series = pd.Series(lst)
        df[name] = series
        return df


def get_data():
    """
    gives you options for loading a data frame
    """
    print("Options")
    print("1) URL")
    print("2) file upload")
    print("3) use dummy data")
    ans = eval(input("Choose an option by selecting the corresponding number: "))
    print()

    if ans == 1: #allows you to enter a url and use it as the dataframe
        url = input("enter the URL: ")
        df = pd.read_csv(url)
        return df
    elif ans == 2: # after directed to a file path uses it to load a file
        import os
        path = input("Provide the path to the directory where the file is located: ")
        os.chdir(path)
        filename = input("Enter the file name: ")
        df = pd.read_csv(filename)
        return df
    elif ans == 3:
        df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                   'C': [1, 2, 3]})
        return df
    
def remove_Nan(df):
    """
    this function removes nans from a dataframe
    """
    if df.isnull().sum() == 0:
        print("there were no null values")
    else:
        df = df.dropna()
        return df

#df = get_data()
#print(df.head(5))
#edit = Edit(df)
#new = [34,54,23,45]
#edit.add_col(df,new,name = "D")
#print(df.head())