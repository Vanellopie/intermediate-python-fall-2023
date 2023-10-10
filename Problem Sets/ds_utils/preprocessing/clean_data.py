def remove_duplicates(data):
    """
    Remove duplicate rows from a pandas DataFrame.

    Args:
        data (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: A DataFrame with duplicate rows removed.
    """
    cleaned_data = data.drop_duplicates()
    return cleaned_data

def handle_missing_values(data):
    """
    Handle missing values in a pandas DataFrame by filling them with zeros.

    Args:
        data (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: A DataFrame with missing values filled with zeros.
    """
    cleaned_data = data.fillna(0)
    return cleaned_data
