def main():
    print("Simple Expense Tracker")

    amount = float(input("Enter the amount: "))

    if validate_amount(amount) == False:
        print("Invalid amount")
        return

    category = input("Enter the category: ")

    exp = add_expense(amount, category)
    print("Expense added:", exp)

    expenses = []
    expenses.append(exp)

    total = calculate_total(expenses)
    print("Total expense:", total)


def add_expense(amount, category):
    expense = {}
    expense["amount"] = amount
    expense["category"] = category
    return expense


def calculate_total(expenses):
    total = 0
    for item in expenses:
        total = total + item["amount"]
    return total


def validate_amount(amount):
    if amount > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
