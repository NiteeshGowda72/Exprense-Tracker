import json


def save_data():
    with open("expenses.json", "w") as file:
        json.dump(expenses_list, file, indent=4)


try:
    with open("expenses.json", "r") as file:
        expenses_list = json.load(file)
except:
    expenses_list = []


def display_expense():
    n = 1
    for expense in expenses_list:
        print(f"Expense number {n}")
        print(f"Expense amount : {expense['amount']}")
        print(f"Expense category : {expense['category']}")
        print(f"Expense description : {expense['description']}")
        print(f"Expense date : {expense['date']}")
        print("__________________________\n")
        n += 1


while True:
    select_menu = int(input(
        "---Menu Bar--- \n"
        "Enter 1 to add Expenses \n"
        "Enter 2 to view Expenses \n"
        "Enter 3 to check total spending \n"
        "Enter 4 to filter EXpenses \n"
        "Enter 5 to delete Expense \n"
        "Enter 6 to edit Expense \n"
        "Enter 7 to exit \n"))

    if select_menu == 1:

        while True:
            message = input(
                "Do you want to add expense? (yes/no): \n")
            if message.lower() == 'no':
                break

            expense_data = {
                'amount': int(input("Enter the amount: ")),
                'category': input("Enter the category: "),
                'description': input("Enter the Description: "),
                'date': input("Enter the date: ")
            }
            expenses_list.append(expense_data)
            save_data()

    elif select_menu == 2:
        display_expense()

    elif select_menu == 3:
        total = 0
        for expense in expenses_list:
            total += expense['amount']
        print(f"Total expense is: {total} \n")

    elif select_menu == 4:

        filter_category = input("Enter the category to filter : ")
        found = False
        for expense in expenses_list:
            if filter_category.lower() == expense['category'].lower():
                print(f"Expense amount : {expense['amount']}")
                print(f"Expense category : {expense['category']}")
                print(f"Expense description : {expense['description']}")
                print(f"Expense date : {expense['date']}")
                print("__________________________\n")
                found = True
        if not found:
            print("Entered category is not found")

    elif select_menu == 5:
        delete_expense = int(
            input("Enter the expense number you want to remove : "))

        index = delete_expense-1

        if 0 <= index < len(expenses_list):
            expenses_list.pop(index)
            print(f"Expense {delete_expense} is deleted")
            display_expense()
            save_data()

        else:
            print("Enter the valid expense number")

    elif select_menu == 6:
        edit_expense = int(input("Enter the expense number to edit : "))
        index = edit_expense-1

        if 0 <= index < len(expenses_list):
            selected_expense = expenses_list[index]
            select_key = int(input(

                "Enter 1 to edit amount \n"
                "Enter 2 to edit Category \n"
                "Enter 3 to edit Description \n"
                "Enter 4 to edit Date \n"))

            if select_key == 1:
                selected_expense['amount'] = int(input("Enter the amount: "))
            elif select_key == 2:
                selected_expense['category'] = input("Enter the category: ")
            elif select_key == 3:
                selected_expense['description'] = input(
                    "Enter the Description: ")
            elif select_key == 4:
                selected_expense['date'] = input("Enter the date: ")
            print(f"Expense {edit_expense} is edited")
            display_expense()
            save_data()

        else:
            print("Enter the valid expense number")
    elif select_menu == 7:
        break
