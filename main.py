"""This is a personal expense tracker
made solely in python
Made by Jaspreet Singh"""

import csv, os, datetime

with open("program-files/Users.csv", 'r', newline='') as f:
    reader = csv.reader(f)
    Users = [i for i in reader]

with open("program-files/Passwords.csv", 'r', newline='') as f:
    reader = csv.reader(f)
    Passwords = [i for i in reader]

def main_flow():
    print("Welcome to personal expense tracker")
    val = input("Username: ")
    if Users == []:
        with open("program-files/Users.csv", "a", newline='') as f:
                writer = csv.writer(f)
                writer.writerow([val])
                new_user(val)
    else:
        for i in Users:
            if val in i:
                old_user(val)
                break
        else:
            with open("program-files/Users.csv", "a", newline='') as f:
                writer = csv.writer(f)
                writer.writerow([val])
                new_user(val)

def new_user(val):
    print("New user detected, please set your password!")
    var = input("Enter the value: ")
    with open("program-files/Passwords.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([val, var])
    menu()

def old_user(val):
    print(f"Welcome back, {val}")
    var = input("Please enter your password: ")
    check_password(val, var)
    menu()

def check_password(val, var):
    for i in Passwords:
        if i[0] == val:
            passwd = i[1]
    ctr = 2
    for i in range(2):
        if var == passwd:
            print("Signing in!")
            break
        else:
            print(f"You have {ctr} more attempts, try again")
            var = input("Please enter your password: ")
            ctr -= 1
    else:
        print("You couldn't give the correct password... exiting the application")
        quit()

def menu():
    while True:    
        os.system("cls")
        print("Enter the number corresponding to the task")
        print("1 Add Expense")
        print("2 View Expenses")
        print("3 Statistics")
        print("4 Delete user data")
        while True:
            var = input("Enter the value: ")
            if var == 1:
                add_exp()
                break
            elif var == 2:
                view_exp()
                break
            elif var == 3:
                stats()
                break
            elif var == 4:
                del_user()
                break
            elif var == 5:
                quit()
            else:
                print("Try again!")

def add_exp():
    pass

def view_exp():
    pass

def stats():
    pass

def del_user():
    pass

#Main loop
main_flow()
