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

def check_if_user_pass_in(f, username, password):
    if username or password not in f:
        auth = False
    else:
        auth = True

    return auth

def login_system(f):
    attempts = 3
    print("Hello!")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    is_customer = input("Are you a customer or a business owner? If you are a customer, press c, if a business owner, press b. ")
    if is_customer.lower() == "c":
        is_customer = False
    else:
        is_customer = False
    auth = check_if_user_pass_in(f, username, password)
    while auth == False or attempts < 1:
        print("Incorrect username/password!")
        print(f"{attempts} attempts remaining.")
        attempts -= 1
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        auth = check_if_user_pass_in(f, username, password)
        if attempts == 0:
            sys.exit("Ran out of attempts. Goodbye!")
    print(f"Welcome back, {username}")

    return is_customer

def Add_Business(username, password, is_customer):
    ""

def menu_page():
    print("S: Signup")
    print("L: Login")
    print("A: Add Business")
    