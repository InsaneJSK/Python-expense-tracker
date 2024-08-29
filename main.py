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
    global user
    print("Welcome to personal expense tracker")
    val = input("Username: ")
    user = val
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
        print("5 quit")
        while True:
            try:
                var = int(input("Enter the value: "))
            except ValueError:
                continue
            if var == 1:
                add_exp()
                input("Press enter to continue")
                break
            elif var == 2:
                view_exp()
                input("Press enter to continue")
                break
            elif var == 3:
                stats()
                input("Press enter to continue")
                break
            elif var == 4:
                del_user()
                input("Press enter to continue")
                break
            elif var == 5:
                os.system('cls')
                print("Quitting the application")
                quit()
            else:
                print("Try again!")

def add_exp():
    os.system("cls")
    paid = int(input("Amount paid: "))
    paidto = input("Amount paid to: ")
    time = datetime.datetime.now()
    try:
        with open(f"program-files/expenses/{user}.csv", 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([paid, paidto, time])
    except FileNotFoundError:
        with open(f"program-files/expenses/{user}.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([paid, paidto, time])

def view_exp():
    os.system("cls")
    print("Enter the number corresponding to the task")
    print("1 All transactions")
    print("2 Transactions by date")
    print("3 Transactions by amount")
    print("4 Transactions by the person paid to")
    print("5 Go back")
    print("6 quit")
    while True:
        var = int(input("Enter the value: "))
        if var == 1:
            view_all()
            break
        elif var == 2:
            view_date()
            break
        elif var == 3:
            view_amount()
            break
        elif var == 4:
            view_person()
            break
        elif var == 5:
            menu()
        elif var == 6:
            os.system('cls')
            print("Quitting the application")
            quit()
        else:
            print("Try again!")

def stats():
    print(f"Stats page for {user}")
    now = datetime.datetime.now()
    month = now.month
    exp = 0
    dicti = {}
    try:
        with open(f"program-files\\expenses\\{user}.csv", "r", newline='') as f:
            reader = csv.reader(f)
            for i in reader:
                if int(i[2][5:7]) == month:
                    exp += int(i[0])
                    if i[1] not in dicti.keys():
                        dicti[i[1]] = int(i[0])
                    else:
                        dicti[i[1]] += int(i[0])
    except FileNotFoundError:
        pass
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print(f"Total Expenditure in the month of {months[month-1]} is {exp}")
    max_key = max(dicti, key=dicti.get)
    print(f"The most expenditure was done on {max_key} which was {dicti[max_key]}")
    avg = exp/30
    print(f"Average Daily expenditure = {avg}")

def del_user():
    print("Are you sure?")
    yn = input("Enter y to proceed, anything else to cancel")
    if yn != "y":
        menu()
    with open("program-files\\Users.csv", "r", newline='') as f:
        reader = csv.reader(f)
        listi = []
        for i in reader:
            listi.append(i)
    print(listi)
    index = listi.index([user])
    listi.pop(index)
    with open("program-files\\Users.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(listi)
    with open("program-files\\Passwords.csv", "r", newline="") as f:
        reader = csv.reader(f)
        listii = []
        for i in reader:
            listii.append(i)
    listii.pop(index)
    with open("program-files\\Passwords.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(listi)
    print(f"{user} deleted successfully")

def view_all():
    try:
        with open(f"program-files\\expenses\\{user}.csv", "r", newline='') as f:
            reader = csv.reader(f)
            for i in reader:
                print(i)
    except FileNotFoundError:
        print("No expenses tracked for the current user!")

def view_date():
    while True:
        date = input("Enter the date like YYYY-MM-DD: ")
        if len(date) != 10:
            print("invalid")
            continue
        elif (date[4], date[7]) != ("-", "-"):
            print("invalid")
            continue
        elif int(date[5:7]) not in list(range(1, 13)):
            print("invalid")
            continue
        elif int(date[8:]) not in list(range(1, 32)):
            print("invalid")
            continue
        else:
            break
    try:
        with open(f"program-files\\expenses\\{user}.csv", "r", newline="") as f:
            reader = csv.reader(f)
            boo = False
            for i in reader:
                if date == i[2][:10]:
                    print(i)
                    boo = True
            if not boo:
                print("No records found")
    except FileNotFoundError:
        print("No expenses tracked for the current user!")
        
def view_amount():
    while True:
        try:
            amount = int(input("Enter the amount: "))
            break
        except ValueError:
            print("Try again!")
    try:
        with open(f"program-files\\expenses\\{user}.csv", "r", newline="") as f:
            reader = csv.reader(f)
            boo = False
            for i in reader:
                if amount == int(i[0]):
                    print(i)
                    boo = True
            if not boo:
                print("No records found")
    except FileNotFoundError:
        print("No expenses tracked for the current user!")

def view_person():
    person = input("Enter the name of the person the amount was paid to: ")
    try:
        with open(f"program-files\\expenses\\{user}.csv", "r", newline="") as f:
            reader = csv.reader(f)
            boo = False
            for i in reader:
                if person == int(i[1]):
                    print(i)
                    boo = True
            if not boo:
                print("No records found")
    except FileNotFoundError:
        print("No expenses tracked for the current user!")

#Main loop
main_flow()
