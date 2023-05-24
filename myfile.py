'''
'''
import pandas as pd


def thisismymethod(param):
    '''
    '''
    print("in the other file")
    df = pd.read_csv("Pokemon.csv")
    print(df)
    return df.to_json(orient='records')
