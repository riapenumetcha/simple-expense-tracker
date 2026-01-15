from project import add_expense, calculate_total, validate_amount


def test_add_expense():
    expense = add_expense(100, "food")
    assert expense["amount"] == 100
    assert expense["category"] == "food"


def test_calculate_total():
    expenses = [
        {"amount": 50, "category": "travel"},
        {"amount": 30, "category": "food"}
    ]
    total = calculate_total(expenses)
    assert total == 80


def test_validate_amount():
    assert validate_amount(10) == True
    assert validate_amount(-5) == False
