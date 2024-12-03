'''
Basic Python Project by Shahil Dhakal
Student, BE Software, NCIT
I will be Creating a simple Personal Expense Tracker that helps you manage daily expenses.
This project will incorporate all the Python basics I've learned.
'''

import pandas as pd #For reading, writing, and manipulating Excel files.
import os #To check and manage file operations, such as verifying if the file exists.

FILE_PATH = "expenses.xlsx" #Defines the path of the Excel file where expenses will be stored.


if not os.path.exists(FILE_PATH):
    df = pd.DataFrame(columns=["Name", "Category", "Amount"])
    df.to_excel(FILE_PATH, index=False)


def addExpenses():
    print("\nPlease Enter Your Expenses:")
    name = input("Enter the name of the product: ")
    category = input("Enter the category of the product (eg; food, bills, etc.): ")
    amount = input("Enter the total amount(In RS): ")

    df = pd.read_excel(FILE_PATH)
    new_expense = {"Name": name, "Category": category, "Amount": amount}
    df = df._append(new_expense, ignore_index=True)
    df.to_excel(FILE_PATH, index=False)
    print("Expense added successfully!")


def viewExpenses():
    df = pd.read_excel(FILE_PATH)

    if df.empty:
        print("\nNo expenses yet!")

    else:
        print(df)

def deleteExpenses():
    df = pd.read_excel(FILE_PATH)

    if df.empty:
        print("\nNo expenses yet!")
        return #Exit the deleteExpenses() function immediately

    print("\nCurrent Expenses:")
    for i,row in df.iterrows():
        print(f"{i+1}. Name: {row['Name']}, Category: {row['Category']}, Amount: {row['Amount']}")

    choice = input("\nEnter the expense number to delete: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(df):
            df = df.drop(df.index[choice - 1])
            df.to_excel(FILE_PATH, index=False)
            print("\nExpense deleted successfully!")
        else:
            print("\nInvalid choice. Try again!")
    else:
        print("\nPlease enter a valid number")


def mainMenu():
    print("\nWelcome to your personal expense tracker!")
    print("Here's your services:")
    print("1.Add Expenses")
    print("2.View Expenses")
    print("3.Delete Expenses")
    print("4.Press any other key to exit!")


while True:
    mainMenu()
    option = input("\nWhat action would you like to perform: ")

    if( option == "1"):
        addExpenses()
    elif(option == "2"):
        viewExpenses()
    elif(option == "3"):
        deleteExpenses()
    else:
        print("\nExiting the Program. Goodbye!")
        break