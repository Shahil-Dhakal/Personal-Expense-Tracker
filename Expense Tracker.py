'''
Basic Python Project by Shahil Dhakal
Student, BE Software, NCIT
I will be Creating a simple Personal Expense Tracker that helps you manage daily expenses.
This project will incorporate all the Python basics I've learned.
'''

expenses = []
def addExpenses():
    print("\nPlease Enter Your Expenses:")
    name = input("Enter the name of the product: ")
    category = input("Enter the category of the product (eg; food, bills, etc.): ")
    amount = input("Enter the total amount(In RS): ")

    expense = {
        "Name" : name,
        "Category" : category,
        "Amount" : amount
    }
    expenses.append(expense)

    print("Expense added successfully!")


def viewExpenses():
    print("\nView all expenses:")
    if len(expenses) == 0:
        print("You haven't added any expenses yet!")
    else:
        for expense in expenses:
            print(expenses)
            # print(f"Name: {expense['name']}, Category: {expense['category']}, Amount: {expense['amount']}")


def deleteExpenses():
    if len(expenses) == 0:
        print("\nNo expenses yet!")
        return #Exit the deleteExpenses() function immediately

    for i in range(len(expenses)):
        print(f"{i+1}.", expenses)

    choice = input("\nEnter the expense number to delete: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(expenses):
            expenses.pop(choice - 1) #.pop(index) function delets the indexed element
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
    option = input("What action would you like to perform:")

    if( option == "1"):
        addExpenses()
    elif(option == "2"):
        viewExpenses()
    elif(option == "3"):
        deleteExpenses()
    else:
        print("Exiting the Program. Goodbye!")
        break