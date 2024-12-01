expenses = []

def addExpense():
    print("\nAdd Expense: ")
    item = input("What kind of item is it?: ")
    price = input("Enter the total amount: ")

    expense = {
        "Item" : item,
        "Price" : price
    }
    expenses.append(expense)

    print("\nExpense added successfully!")
def viewExpenses():
    if len(expenses) == 0:
        print("No expenses yet!")
    else:
        print("\nAll of your expenses are:")
        for expense in expenses:
            print(expense)
def deleteExpenses():


def mainMenu():
    print("\nWelcome to your expense tracker: ")
    print("Choose what action to perform: ")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Delete Expense")

while True:
    mainMenu()
    action = input("\nChoose a action to perform else press any other key to exit: ")

    if action == "1":
        addExpense()
    elif action == "2":
        viewExpenses()
    elif action == "3":
        deleteExpenses()
    else:
        print("\nThank You!")
        break