from src.data_loader import load_expenses
from src.analyzer import get_total_expense, get_expense_by_category

DATA_FILE = "data/expenses.csv"

def main():
    df = load_expenses(DATA_FILE)

    if df is None:
        return

    total = get_total_expense(df)
    category_totals = get_expense_by_category(df)

    print("📊 Student Expense Summary\n")
    print(f"Total Expense: ₹{total}\n")

    print("Expenses by Category:")
    for category, amount in category_totals.items():
        print(f"- {category}: ₹{amount}")

if __name__ == "__main__":
    main()
