import pandas as pd

def file_reader(fileName):
    df = pd.read_csv(fileName)
    return df