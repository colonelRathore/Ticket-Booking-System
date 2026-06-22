import sys

def create_account():
    username = input("Please create a username: ")
    password = input("Please create a password: ")
    is_customer = input("Are you a customer or a business owner? If you are a customer, press c, if a business owner, press b. ")
    if is_customer.lower() == "c":
        is_customer = True
    else:
        is_customer = False
    return username, password, is_customer

def add_to_file(username, password, is_customer):
    try:
        f = open("user_info.txt", "x")
    except:
        FileExistsError
        f = open("user_info.txt", "a")
        f.write(username, password, is_customer)
    
    return f

def login_system(f):
    attempts = 3
    print("Welcome Back!")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

def menu_page():
    print("S: Signup")
    print("L: Login")
    