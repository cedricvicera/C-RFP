from filereader import file_reader
from riskcalculator import filter_df, calculator

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_name = 'COVID-19_Case_Surveillance_Public_Use_Data.csv'
    df = file_reader(file_name)
    df_filter = df.copy()
    df_filter = filter_df(df, 'male', '50-59', 'Latino')
    print(calculator(df_filter))




