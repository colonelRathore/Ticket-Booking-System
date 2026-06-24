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

def check_if_customer(is_customer: bool):
    if is_customer == True:
        can_bus = False
    else:
        can_bus = True
    
    return can_bus

def input_business_name_type():
    name = input("What is the name of your business? ")
    bus_type = input("What industry does your business work in?")

    return name, bus_type

def Add_Business(username, is_customer: bool):
    if check_if_customer(is_customer) == False:
        print("This mode is not for you! If you do want to create a business, create another account.")
        return
    else:
        pass
    try:
        b = open("business_list.txt", "x")
        name, bus_type = input_business_name_type()
        b.write(f"{name} owned by {username} in the {bus_type} industry.\n")
    except:
        FileExistsError
        b = open("business_list.txt", "a")
        b.write(f"{name} owned by {username} in the {bus_type} industry.\n")

    return b, name

def Get_Event_Name(username, is_customer, b, name):
    if check_if_customer(is_customer) == False:
        print("This mode is not for you! If you do want to create a business, create another account.")
        return
    else:
        pass
    if username not in b:
        print("There are no businesses listed under your username.")
        return
    else:
        pass
    for line in b:
        if name in line:
            event = input("What event/item would you like to add? ")
    
    return event

def Get_Event_TimeORPrice():
    ev_type = input("Please enter p if the event is an item, or t if it has a time? ")
    if ev_type.lower() == "t":
        print("Please enter your time as in the 24 hour clock. Example: 17:15, or 09:11")
        time_price = input()
    else:
        print("Please enter your price in USD, to two decimal places.")
        time_price = float(input())

    return time_price

def Add_to_Item_List(event, time_price, name):
    try:
        e = open("event_list.txt", "x")
        e.write(f"{event} set up by {name} at time/price {time_price}")
    except:
        FileExistsError
        e = open("event_list.txt", "a")
        e.write(f"{event} set up by {name} at time/price {time_price}")

    return e

#def Choose_E

def menu_page():
    opt = " "
    while opt.upper() != "Q":   
        print("S: Signup")
        print("L: Login")
        print("A: Add Business")
        print("E: Add Event/Item")
        print("B: Book Event")
        print("Q: Quit Program")
        if opt.upper() == "S":
            username, password, is_customer = create_account()
        opt = input()
    sys.exit("Thanks for using the program! See you soon!")
    #gonna keep on adding events!

menu_page()