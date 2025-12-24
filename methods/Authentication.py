import json
import time 

datafile = "data/data.json"

def relax():
  time.sleep(2)

def signup():
      name = input("Enter your name: ")
      email = input("Enter your email: ")
      password = input("Enter your password: ")
      animal = input("Enter your favourite animal: ")
      data = {
      "name": name,
      "email": email.lower(),
      "password": password.lower(),
      "animal": animal.lower()
      }    
      with open(datafile, "r") as file:
        content = json.load(file)

      if not isinstance(content, list):
        content = [content]

      content.append(data)

      with open(datafile, "w") as file:
        json.dump(content, file, indent=3)

      print("Signup Successful")
      print("You can now login with your credentials")
      relax()
  

def login():
  email = input("Enter your email: ")
  password = input("Enter your password: ")
  with open(datafile, "r") as file:
    data = json.load(file)
    if data["email"] == email.lower() and data["password"] == password.lower():
      print("Login Successful")
    else:
      print("Invalid Credentials")
    relax()
  


def logout():
  print("Logged out successfully")
  relax()
  exit()

def reset_password():
  pass

def change_password():
  pass

def delete_account():
  pass

def update_profile():
  pass

def view_profile():
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
    case _:
      print("Invalid option")