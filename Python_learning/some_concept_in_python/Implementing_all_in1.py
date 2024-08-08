import os
import sys
import datetime
import json
import re
import random

# Prompt the user for the file name
All_in_one_transaction = input("Enter the file name for storing transactions (e.g., transactions.json): ").strip()

# Check if the transactions file exists, create if not
if not os.path.exists(All_in_one_transaction):
    with open(All_in_one_transaction, "w") as file:
        json.dump([], file)  # Start with an empty list
    print(f"'{All_in_one_transaction}' created.")

def add_transaction(description, amount):
    transaction = {
        "description": description,
        "amount": amount,
        "date_added": datetime.datetime.now().isoformat(),
        "id": random.randint(1000, 9999)  # Random ID for the transaction
    }
    with open(All_in_one_transaction, "r+") as file:
        transactions = json.load(file)
        transactions.append(transaction)
        file.seek(0)
        json.dump(transactions, file, indent=4)
    print(f"Transaction added: {description} (${amount})")

def list_transactions():
    with open(All_in_one_transaction, "r") as file:
        transactions = json.load(file)
    if not transactions:
        print("No transactions found.")
    else:
        for transaction in transactions:
            print(f"ID: {transaction['id']}, Description: {transaction['description']}, Amount: ${transaction['amount']}, Date Added: {transaction['date_added']}")

def find_transactions(keyword):
    with open(All_in_one_transaction, "r") as file:
        transactions = json.load(file)
    
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    found_transactions = [t for t in transactions if pattern.search(t["description"])]
    
    if not found_transactions:
        print(f"No transactions found with keyword '{keyword}'.")
    else:
        for t in found_transactions:
            print(f"ID: {t['id']}, Description: {t['description']}, Amount: ${t['amount']}, Date Added: {t['date_added']}")

def delete_transaction(transaction_id):
    with open(All_in_one_transaction, "r+") as file:
        transactions = json.load(file)
        transactions = [t for t in transactions if t["id"] != transaction_id]
        file.seek(0)
        file.truncate()
        json.dump(transactions, file, indent=4)
    print(f"Transaction with ID {transaction_id} deleted.")

def generate_report():
    with open(All_in_one_transaction, "r") as file:
        transactions = json.load(file)
    
    total_income = sum(t["amount"] for t in transactions if t["amount"] > 0)
    total_expenses = sum(t["amount"] for t in transactions if t["amount"] < 0)
    balance = total_income + total_expenses
    
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Balance: ${balance}")

def main():
    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add Transaction")
        print("2. List Transactions")
        print("3. Find Transactions by Keyword")
        print("4. Delete Transaction")
        print("5. Generate Report")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            description = input("Enter transaction description: ").strip()
            amount = float(input("Enter transaction amount: ").strip())
            add_transaction(description, amount)
        elif choice == "2":
            list_transactions()
        elif choice == "3":
            keyword = input("Enter keyword to search for: ").strip()
            find_transactions(keyword)
        elif choice == "4":
            transaction_id = int(input("Enter transaction ID to delete: ").strip())
            delete_transaction(transaction_id)
        elif choice == "5":
            generate_report()
        elif choice == "6":
            print("Exiting the budget tracker.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
