import pandas as pd

def file_reader(fileName):
    df = pd.read_csv(fileName)
    print(df.columns)
    print(df.sex.unique())
    print(df.age_group.unique())
    print(df.race_ethnicity_combined.unique())
    print(df.medcond_yn.unique())
    print(df.death_yn.unique())
    return df