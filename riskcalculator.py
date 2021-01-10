def filter_df(df, sex, age, race):
    """Parameters are dataframe"""
    #filter sex
    if sex == 'female':
        df = df[df['sex'] == 'Female']
    elif sex == 'male':
        df = df[df['sex'] == 'Male']
    else:
        df = df[df['sex'] == 'Other']

    #filter age
    if age == '0-9':
        df = df[df['age_group'] == '0 - 9 Years']
    elif age == '10-19':
        df = df[df['age_group'] == '10 - 19 Years']
    elif age == '20-39':
        df = df[df['age_group'] == '20 - 39 Years']
    elif age == '40-49':
        df = df[df['age_group'] == '40 - 49 Years']
    elif age == '50-59':
        df = df[df['age_group'] == '50 - 59 Years']
    elif age == '60-69':
        df = df[df['age_group'] == '60 - 69 Years']
    elif age == '70-79':
        df = df[df['age_group'] == '70 - 79 Years']
    else:
        df = df[df['age_group'] == '80+ Years']

    #filter
    if race == 'Latino':
        df = df[df['race_ethnicity_combined'] == 'Hispanic/Latino']
    elif race == 'American Indian':
        df = df[df['race_ethnicity_combined'] == 'American Indian/Alaska Native, Non-Hispanic']
    elif race == 'Asian':
        df = df[df['race_ethnicity_combined'] == 'Asian, Non-Hispanic']
    elif race == 'Black':
        df = df[df['race_ethnicity_combined'] == 'Black, Non-Hispanic']
    elif race == 'Native Hawaiian':
        df = df[df['race_ethnicity_combined'] == 'Native Hawaiian/Other Pacific Islander, Non-Hispanic']
    elif race == 'White':
        df = df[df['race_ethnicity_combined'] == 'White, Non-Hispanic']
    else:
        df = df[df['race_ethnicity_combined'] == 'Multiple/Other, Non-Hispanic']
    return df



def calculator(filtered_df):
    """Count the number of Yes & No in death_yn column. Yes/Total = Risk Factor. Returns the risk factor."""
    if filtered_df.empty:
        print("Your input information currently does not match any subset of our dataset.")
        return None
    else:
        yes_count = filtered_df.death_yn.value_counts()['Yes']
        no_count = filtered_df.death_yn.value_counts()['No']
        if yes_count+no_count == 0:
            print("Unfortunately we do not have enough information on the subset of information you provided to make "
                  "a prediction.")
            return None
        return yes_count/(yes_count+no_count)
