import pandas as pd

df = pd.DataFrame(data)

# Function to drop rows with empty values using dropna
def drop_empty(df):
    df_cleaned = df.dropna()
    return df_cleaned

# Function to fill empty values in a given column with the mean
def fill_empty(df, column_name):
    df[column_name] = df[column_name].fillna(df[column_name].mean())
    return df

# Function to drop a specific column
def drop_column(df, column_name):
    df = df.drop(columns=[column_name])
    return df

# Function to reset the DataFrame index
def fix_index(df):
    df_reset = df.reset_index(drop=True)
    return df_reset

# Function to change the data type of a column to datetime
def fix_dates(df, column_name):
    df[column_name] = pd.to_datetime(df[column_name])
    return df

# Testing the functions
print("Original DataFrame:")
print(df)

print("\nAfter dropping rows with empty values:")
df_dropped = drop_empty(df)
print(df_dropped)

print("\nAfter filling empty values in column 'C' with mean:")
df_filled = fill_empty(df, 'C')
print(df_filled)

print("\nAfter dropping column 'B':")
df_dropped_column = drop_column(df, 'B')
print(df_dropped_column)

print("\nAfter resetting the index:")
df_reset = fix_index(df)
print(df_reset)

print("\nAfter changing data type of 'Date_Column' to datetime:")
df_fixed_dates = fix_dates(df, 'Date_Column')
print(df_fixed_dates)
