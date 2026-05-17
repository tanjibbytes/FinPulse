import csv
import os
from datetime import datetime

FILE_NAME = "finpulse_data.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount", "Description"])

def add_transaction(t_type, category, amount, description):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE_NAME, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([date, t_type, category, amount, description])
    print(f"✅ Successfully added {t_type}: ৳{amount} in '{category}'")

def view_report():
    if not os.path.exists(FILE_NAME):
        print("No data found! Add some transactions first.")
        return

    total_income = 0
    total_expense = 0

    print("\n--- FinPulse Financial Report ---")
    with open(FILE_NAME, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if not row: continue
            date, t_type, category, amount, desc = row
            amount = float(amount)
            if t_type == "Income":
                total_income += amount
            elif t_type == "Expense":
                total_expense += amount
            print(f"[{date}] {t_type} | {category}: ৳{amount} ({desc})")
    
    print("-" * 40)
    print(f"Total Income:  ৳{total_income}")
    print(f"Total Expense: ৳{total_expense}")
    print(f"Current Balance: ৳{total_income - total_expense}")
    print("-" * 40)

def main():
    initialize_file()
    while True:
        print("\n=== FinPulse (v1.0) ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Financial Report")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            cat = input("Enter Income Source (e.g., Salary, Business): ")
            amount = float(input("Enter Amount (৳): "))
            desc = input("Short Description: ")
            add_transaction("Income", cat, amount, desc)
        elif choice == '2':
            cat = input("Enter Expense Category (e.g., Food, Marketing): ")
            amount = float(input("Enter Amount (৳): "))
            desc = input("Short Description: ")
            add_transaction("Expense", cat, amount, desc)
        elif choice == '3':
            view_report()
        elif choice == '4':
            print("Thank you for using FinPulse. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1-4.")

if __name__ == "__main__":
    main()
