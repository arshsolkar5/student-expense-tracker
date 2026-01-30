# Student Expense Tracker (Python)

## Overview
This project is a simple **Student Expense Tracker** built using Python.  
It reads daily expense data from a CSV file and generates useful summaries such as total spending and category-wise expenses.

The focus of this project is **clean project structure, modular code, and proper version control**, rather than complexity.

---

## Purpose of the Project
Many beginner projects are written as a single script.  
This project was intentionally structured to practice:

- Organizing Python code into modules
- Separating data loading, analysis, and execution logic
- Managing dependencies using a virtual environment
- Maintaining a clean GitHub repository with meaningful commits

---

## Project Structure
```text
student-expense-tracker/
├── data/
│   └── expenses.csv
├── src/
│   ├── data_loader.py
│   ├── analyzer.py
│   └── __init__.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```


## Features
- Load expense data from a CSV file
- Calculate total expenses
- Generate category-wise expense summaries
- Clean command-line output
- Modular and maintainable code structure

---

## What This Project Demonstrates
- Working with **structured CSV data**
- Writing **reusable Python functions**
- Applying **separation of concerns**
- Using **virtual environments** for dependency management
- Following **basic software engineering best practices**

---

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/arshsolkar5/student-expense-tracker.git
cd student-expense-tracker
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the program
```bash
python main.py
```

### Sample Output
```text
Student Expense Summary

Total Expense: ₹950

Expenses by Category:
- Food: ₹210
- Transport: ₹40
- Books: ₹350
- Entertainment: ₹150
- Utilities: ₹200
```

