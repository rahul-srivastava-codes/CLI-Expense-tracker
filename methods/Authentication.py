import json
import sys 
import time 
from utils.file_utils import expenses_method
datafile = "data/data.json"

def relax():
  time.sleep(2)
  

def signup():
      print("Welcome to Signup")
      name = str(input("Enter your name: "))
      email = str(input("Enter your email: "))
      password = str(input("Enter your password: "))
      animal = str(input("Enter your favourite animal: "))
      data = {
      "name": name,
      "email": email.lower(),
      "password": password.lower(),
      "animal": animal.lower()
      }    
      with open(datafile, "r") as file:
        content = json.load(file)
        print((content))

      if not isinstance(content, list):
        content = [content]

      content.append(data)

      with open(datafile, "w") as file:
        json.dump(content, file, indent=3)

      print("Signup Successful")
      print("You can now login with your credentials")
      relax()
      login()
  

def login():
    print("Welcome to Login")

    with open(datafile, "r") as file:
        data = json.load(file)

    for attempt in range(3):
        email = input("Enter your email: ").lower()
        password = input("Enter your password: ").lower()

        for user in data:
            if user["email"] == email and user["password"] == password:
                print("Login Successful")
                relax()
                option = int(input(
                    "Enter what you want to do next:\n1. Manage Expenses\n2. Exit\n"
                ))
                expenses_method(option)
                return

        print(f"Invalid credentials. Attempts left: {2 - attempt}")

    print("Too many failed attempts. Try again later.")

  


def logout():
  print("Logged out successfully")
  relax()
  sys.exit()

def reset_password():
    print("Welcome to Reset Password")

    with open(datafile, "r") as file:
        data = json.load(file)

    email = input("Enter your registered email: ").lower()
    animal = input("Enter your favourite animal: ").lower()

    for user in data:
        if user["email"] == email and user["animal"] == animal:
            new_password = input("Enter your new password: ")
            user["password"] = new_password  # DO NOT lower password

            with open(datafile, "w") as file:
                json.dump(data, file, indent=3)

            print("Password reset successful")
            return

    print("Invalid email or security answer")


def change_password():
    print("Welcome to Change Password")

    with open(datafile, "r") as file:
        data = json.load(file)

    email = input("Enter your registered email: ").lower()
    animal = input("Enter your favourite animal: ").lower()
    old_password = input("Enter your old password: ")

    for user in data:
        if (
            user["email"] == email and
            user["animal"] == animal and
            user["password"] == old_password
        ):
            new_password = input("Enter your new password: ")
            user["password"] = new_password

            with open(datafile, "w") as file:
                json.dump(data, file, indent=3)

            print("Password changed successfully")
            return

    print("Invalid credentials. Password not changed.")


def delete_account():
    print("Welcome to Delete Account")

    with open(datafile, "r") as file:
        data = json.load(file)

    email = input("Enter your registered email: ").lower()
    animal = input("Enter your favourite animal: ").lower()
    password = input("Enter your password: ")

    for i, user in enumerate(data):
        if (
            user["email"] == email and
            user["animal"] == animal and
            user["password"] == password
        ):
            confirm = input(
                "Are you sure you want to delete your account? (yes/no): "
            ).lower()

            if confirm == "yes":
                data.pop(i)

                with open(datafile, "w") as file:
                    json.dump(data, file, indent=3)

                print("Account deleted successfully")
            else:
                print("Account deletion cancelled")
            return

    print("Invalid credentials. Account not deleted.")


def update_profile():
    print("Welcome to Update Profile")

    with open(datafile, "r") as file:
        data = json.load(file)

    email = input("Enter your registered email: ").lower()
    animal = input("Enter your favourite animal: ").lower()
    password = input("Enter your password: ")

    for user in data:
        if (
            user["email"] == email and
            user["animal"] == animal and
            user["password"] == password
        ):
            new_name = input("Enter your new name: ")
            new_email = input("Enter your new email: ").lower()
            new_animal = input("Enter your new favourite animal: ").lower()

            user["name"] = new_name
            user["email"] = new_email
            user["animal"] = new_animal

            with open(datafile, "w") as file:
                json.dump(data, file, indent=3)

            print("Profile updated successfully")
            return

    print("Invalid credentials. Profile not updated.")


def view_profile():
    print("Welcome to View Profile")

    with open(datafile, "r") as file:
        data = json.load(file)

    email = input("Enter your registered email: ").lower()
    password = input("Enter your password: ")

    for user in data:
        if user["email"] == email and user["password"] == password:
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("Favourite Animal:", user["animal"])
            return

    print("Invalid credentials")


def match(num):
  match num:
    case 1:      
      signup()      
    case 2:      
      login()
    case 3:
      logout()
    case 4:
      reset_password()
    case 5:
      change_password()
    case 6:
      delete_account()
    case 7:
      update_profile()
    case 8:
      view_profile()
    case 9:
      exit()  
    case _:
      print("Invalid option")