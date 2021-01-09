import pandas as pd

def file_reader(fileName):
    df = pd.read_csv(fileName)
    print(df.columns)
    print(df['age_group'])
    print(df.head())