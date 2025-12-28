import os
import json

expense_path = "model/expense.json"

# code for folder creation
def folder_creation(foldername):
  os.makedirs(foldername,exist_ok=True)
  return foldername


def get_file_path(foldername,filename):
  folder_creation(foldername)
  return os.path.join(foldername,filename) 



def load_expense():
  print("Loading expenses from expense.json")
  with open("model/expense.json","r") as file:
    data = json.load(file)
    print(data)
  print("Expenses loaded successfully")
  

def save_expense(path, expenses):
    with open(path, "w") as file:
        json.dump(expenses, file, indent=2)


def add_expense(path):
    expenses = load_expense(path)
    amount = float(input("Amount: "))
    category = input("Category: ")
    note = input("Note: ")

    expense = {
      "amount": amount,
      "category": category,
      "note": note
    }
    expenses.append(expense)
    save_expense(path, expenses)

    print("Expense added successfully")

def view_expense(path):
    expenses = load_expense(path)

    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Your Expenses ---")
    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. Amount: {exp['amount']} | Category: {exp['category']} | Note: {exp['note']}")


def expenses_method(choice):
    match choice:
        case 1: 
            load_expense()
        case 2:
            save_expense(expense_path, [])
        case 3:
            add_expense(expense_path)
        case 4:
            view_expense(expense_path)        
        case 9:
            print("Exiting...")
            exit()
        case _:
            print("Invalid option")