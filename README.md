# Simple-Expense-Tracker
#### Video Demo:

#### Description: The Simple Expense Tracker is a terminal-based Python application created as my final project for CS50’s Introduction to Programming with Python (CS50P). This project was designed to apply core Python programming concepts in a practical and beginner friendly way. The program allows users to record expenses by entering an amount and a category, store multiple expenses, and calculate the total amount spent.

The main objective of this project is to strengthen understanding of Python fundamentals such as functions, dictionaries, lists, loops, conditional statements, and user input handling. Rather than focusing on advanced features or graphical interfaces, the project emphasizes clean logic, simplicity, and correctness. This approach aligns closely with the goals of CS50P, which encourages learning through clear and well structured code.

The application runs entirely in the terminal and does not use any external libraries. This design choice keeps the focus on understanding Python’s built-in features and avoids unnecessary complexity. The project is intended for beginners who are learning how to structure programs, manage data, and solve real-world problems using basic programming techniques.

How the Program Works

When the program is executed, it begins by displaying a title message that identifies the application as the Simple Expense Tracker. This helps the user understand the purpose of the program before interacting with it. The program then prompts the user to enter an expense amount. This input represents how much money was spent and is a required part of recording an expense.

Once the user enters an amount, the program performs basic input validation to ensure that the value is valid. Specifically, it checks that the amount entered is greater than zero. If the user enters an invalid value, such as a negative number or zero, the program displays an error message and stops execution. This validation step helps prevent incorrect data from being stored and ensures that all calculations are accurate.

If the expense amount passes validation, the program continues by asking the user to enter a category for the expense. Categories allow expenses to be organized and provide context for how the money was spent. Common examples include food, travel, or shopping, but the program allows the user to enter any category they choose.

After both the amount and category are provided, the program stores the expense as a dictionary containing the expense details. This dictionary groups related data together in a clear and structured format. The expense dictionary is then added to a list, which allows the program to keep track of multiple expenses during a single run of the program.

Once all expense entries are stored, the program calculates the total amount spent. This is done by looping through the list of expense dictionaries and summing the expense amounts. After the calculation is complete, the final total is displayed to the user in the terminal, providing a clear summary of the recorded expenses.

Design Choices

This project was intentionally kept simple and terminal based to focus on Python fundamentals rather than user interface design. Dictionaries were chosen to store expenses because they naturally group related data, such as an amount and its category. A list is used to store multiple expense entries, making it easy to loop through them and perform calculations.

The program is divided into small, clearly defined functions, with each function responsible for a single task. This modular structure improves readability and makes the code easier to test and debug. Basic input validation is included to ensure accurate calculations and prevent invalid data from being processed.
