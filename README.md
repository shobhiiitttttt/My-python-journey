
expenses = []

def add_expense(name, amount):
    expenses.append({
        "name": name,
        "amount": amount
    })
    print(f"Added: {name} - Rs.{amount}")

def show_expenses():
    print("\n--- Expense Report ---")
    total = 0

    for expense in expenses:
        print(f"{expense['name']}: Rs.{expense['amount']}")
        total += expense["amount"]

    print("----------------------")
    print(f"Total Spending: Rs.{total}")

add_expense("Food", 150)
add_expense("Travel", 100)
add_expense("Coffee", 50)

show_expenses()
