import pandas as pd

def load_expenses(file_path):
    """
    Load expense data from a CSV file.
    Returns a pandas DataFrame if successful.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Expense file not found.")
        return None

