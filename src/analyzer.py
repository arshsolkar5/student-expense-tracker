def get_total_expense(df):
    """
    Calculate total expense amount.
    """
    return df["amount"].sum()


def get_expense_by_category(df):
    """
    Calculate total expenses grouped by category.
    Returns a dictionary.
    """
    return df.groupby("category")["amount"].sum().to_dict()
