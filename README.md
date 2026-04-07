# Expense Tracker (CLI Application)

## Description

This is a command-line based Expense Tracker application built using Python.
The application allows users to manage their daily expenses efficiently by providing features such as adding, viewing, editing, deleting, and filtering expenses.

All data is stored persistently using a JSON file, ensuring that expenses are saved even after the program is closed.

---

## Features

* Add new expenses
* View all recorded expenses
* Calculate total spending
* Filter expenses by category
* Edit existing expenses
* Delete expenses
* Persistent storage using JSON

---

## Technologies Used

* Python
* JSON (for data storage)

---

## Project Structure

```
expense-tracker/
│── main.py
│── expenses.json
│── README.md
```

---

## How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/expense-tracker.git
```

2. Navigate to the project directory:

```
cd expense-tracker
```

3. Run the application:

```
python main.py
```

---

## How It Works

* The application displays a menu with multiple options.
* Users can select an option to perform operations such as adding or viewing expenses.
* Data is stored in a JSON file (`expenses.json`).
* The file is automatically loaded when the program starts and updated after every modification.

---

## Example Menu

```
---Menu Bar---
1 Add Expenses
2 View Expenses
3 Check Total Spending
4 Filter Expenses
5 Delete Expense
6 Edit Expense
7 Exit
```

---

## Future Improvements

* Add input validation for better error handling
* Convert CLI application into a graphical user interface
* Integrate database storage (SQLite/MySQL)
* Add category-wise summary and analytics

---

## Author

Your Name

---

## License

This project is open-source and available under the MIT License.
