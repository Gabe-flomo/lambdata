"""
utility for working with DataFrames
"""

import pandas as pd

def get_data():
    print("Options")
    print("1) URL")
    print("2) file upload")
    print("3) use dummy data")
    ans = eval(input("Choose an option by selecting the corresponding number: "))
    print()

    if ans == 1:
        url = input("enter the URL: ")
        df = pd.read_csv(url)
        return df
    elif ans == 2:
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