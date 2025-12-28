import json
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
  email = str(input("Enter your email: "))
  password = str(input("Enter your password: "))
  i=1
  with open(datafile, "r") as file:
    data = json.load(file)
    print((data))
    for i in range(3):
      if i>0:
        for user in data:
          if(user["email"] == email.lower() and user["password"] == password.lower()):
            print("Login Successful")
            relax()
            option = int(input("Enter what you want to do next:\n1. Manage Expenses\n2. Exit\n"))
            expenses_method(option)
            return
      else:
        print("Too many failed attempts. Try again later.")
        # exit()
    relax()
  


def logout():
  print("Logged out successfully")
  relax()
  exit()

def reset_password():
  print("Welcome to Reset Password")
  with open(datafile,"r") as file:
    data = json.load(file)

  email = input("Enter your registered email: ")
  animal = input("Enter your favourite animal: ")
  if(data["email"] == email.lower() and data["animal"] == animal.lower()):
    new_password = input("Enter your new password: ")
    data["password"] = new_password.lower()
    with open(datafile,"w") as file:
      json.dump(data,file,indent=3)
    print("Password reset successful")
  pass

def change_password():
  print("Welcome to Change Password")
  with open(datafile,"r") as file:
    data = json.load(file)
  email = input("Enter your registered email: ")
  animal = input("Enter your favourite animal: ")
  old_password = input("Enter your old password: ")
  if(data["email"] == email.lower() and data["animal"] == animal.lower() and data["password"] == old_password.lower()):
    new_password = input("Enter your new password: ")
    data["password"] = new_password.lower()
    with open(datafile,"w") as file:
      json.dump(data,file,indent=3)
    print("Password change successful")
 

def delete_account():
  print("Welcome to Delete Account")
  with open(datafile,"r") as file:
    data = json.load(file)
  email = input("Enter your registered email: ")
  animal = input("Enter your favourite animal: ")
  password = input("Enter your password: ")
  if(data["email"] == email.lower() and data["animal"] == animal.lower() and data["password"] == password.lower()):
    confirm = input("Are you sure you want to delete your account? (yes/no): ")
    if confirm.lower() == "yes":
      data = {}
      with open(datafile,"w") as file:
        json.dump(data,file,indent=3)
      print("Account deleted successfully")
    else:
      print("Account deletion cancelled")
  

def update_profile():
  print("Welcome to Update Profile")
  with open(datafile,"r") as file:
    data = json.load(file)
  email = input("Enter your registered email: ")
  animal = input("Enter your favourite animal: ")
  password = input("Enter your password: ")
  if(data["email"] == email.lower() and data["animal"] == animal.lower() and data["password"] == password.lower()):
    new_name = input("Enter your new name: ")
    new_email = input("Enter your new email: ")
    new_animal = input("Enter your new favourite animal: ")
    data["name"] = new_name
    data["email"] = new_email.lower()
    data["animal"] = new_animal.lower()
    with open(datafile,"w") as file:
      json.dump(data,file,indent=3)
    print("Profile updated successfully")
  pass

def view_profile():
  print("Welcome to View Profile")
  with open(datafile,"r") as file:
    data = json.load(file)
  email = input("Enter your registered email: ")
  password = input("Enter your password: ")
  if(data["email"] == email.lower() and data["password"] == password.lower()):
    print("Name:",data["name"])
    print("Email:",data["email"])
    print("Favourite Animal:",data["animal"])
  else:
    print("Invalid Credentials")
  pass

def match(num):
  match num:
    case 1:      
      signup()      
      login()      
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