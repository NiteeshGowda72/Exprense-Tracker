expenses_list = []

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

n = 1
for expense in expenses_list:
    print(f"Expense number {n}")
    print(f"Expense amount : {expense['amount']}")
    print(f"Expense category: {expense['category']}")
    print(f"Expense description : {expense['description']}")
    print(f"Expense date : {expense['date']}")
    print("__________________________\n")
    n += 1
