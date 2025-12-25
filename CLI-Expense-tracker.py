
from utils.file_utils import  get_file_path
from methods.Authentication import match

datafile = get_file_path("data","data.json")
expensefile = get_file_path("model","expense.json")

print("Welcome to Expense Tracker CLI")
print("Press 1 for Signup")
print("Press 2 for Login")
print("Press 3 for Logout")
print("Press 4 for Reset Password")
print("Press 5 for Change Password")
print("Press 6 for Delete Account")
print("Press 7 for Update Profile")
print("Press 8 for View Profile")
print("Press 9 for exit")

choice = int(input("Enter your choice: "))

match(choice)



# print("1. Add Expense")
# print("2. View Expenses")
# print("3. Exit")
# choice = int(input("Enter your choice: "))
# match choice:
#     case 1:
#         add_expense(expensefile)
#     case 2:
#         view_expense(expensefile)
#     case 3:
#         print("Exiting...")
#         exit()
#     case _:
#         print("Invalid option")

