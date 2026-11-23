
# ============================================================
#          PERSONAL FINANCE & GOAL TRACKER
#                     VERSION 1.0
# ============================================================

print("=" * 55)
print("          PERSONAL FINANCE & GOAL TRACKER")
print("=" * 55)


# ------------------------------------------------------------
# 1. INPUT VALIDATION FUNCTIONS
# ------------------------------------------------------------

def get_positive_number(message):
    while True:
        try:
            value = float(input(message))

            if value < 0:
                print("Please enter a non-negative value.")
            else:
                return value

        except ValueError:
            print("Invalid input! Please enter a number.")


def get_age(message):
    while True:
        try:
            age = int(input(message))

            if age <= 0:
                print("Age must be greater than zero.")
            else:
                return age

        except ValueError:
            print("Please enter a valid whole number.")


# ------------------------------------------------------------
# 2. USER PROFILE
# ------------------------------------------------------------

print("\n--- CREATE YOUR FINANCIAL PROFILE ---")

name = input("Enter your name: ").strip()

while not name:
    print("Name cannot be empty.")
    name = input("Enter your name: ").strip()

age = get_age("Enter your age: ")

monthly_income = get_positive_number(
    "Enter your monthly income (Rs.): "
)

current_savings = get_positive_number(
    "Enter your current savings (Rs.): "
)


# ------------------------------------------------------------
# 3. EXPENSE MANAGEMENT
# ------------------------------------------------------------

print("\n--- ENTER YOUR MONTHLY EXPENSES ---")

expense_categories = [
    "Rent",
    "Food",
    "Shopping",
    "Travel",
    "Other"
]

expenses = {}

for category in expense_categories:
    expenses[category] = get_positive_number(
        f"Enter monthly {category} expenses (Rs.): "
    )

total_expenses = sum(expenses.values())

monthly_savings = monthly_income - total_expenses

annual_savings = monthly_savings * 12

if monthly_income > 0:
    savings_percentage = (
        monthly_savings / monthly_income
    ) * 100
else:
    savings_percentage = 0


# ------------------------------------------------------------
# 4. FINANCIAL PROFILE DISPLAY
# ------------------------------------------------------------

def display_profile():

    print("\n" + "=" * 55)
    print("               FINANCIAL PROFILE")
    print("=" * 55)

    print(f"Name              : {name}")
    print(f"Age               : {age}")
    print(f"Monthly Income    : Rs. {monthly_income:,.2f}")
    print(f"Current Savings   : Rs. {current_savings:,.2f}")

    print("\n--- EXPENSE BREAKDOWN ---")

    for category, amount in expenses.items():
        print(f"{category:<18}: Rs. {amount:,.2f}")

    print("-" * 55)
    print(f"Total Expenses    : Rs. {total_expenses:,.2f}")
    print(f"Monthly Savings   : Rs. {monthly_savings:,.2f}")
    print(f"Annual Savings    : Rs. {annual_savings:,.2f}")

    print("=" * 55)


# ------------------------------------------------------------
# 5. MONTHLY SAVINGS CALCULATOR
# ------------------------------------------------------------

def calculate_savings():

    print("\n--- MONTHLY SAVINGS ANALYSIS ---")

    print(f"Monthly Income  : Rs. {monthly_income:,.2f}")
    print(f"Total Expenses  : Rs. {total_expenses:,.2f}")

    print("-" * 40)

    if monthly_savings > 0:
        print(f"You save Rs. {monthly_savings:,.2f} every month.")

    elif monthly_savings == 0:
        print("You are spending exactly what you earn.")

    else:
        print(
            f"You are spending Rs. "
            f"{abs(monthly_savings):,.2f} more than you earn."
        )

    print(f"Savings Rate    : {savings_percentage:.2f}%")

    print("-" * 40)


# ------------------------------------------------------------
# 6. FINANCIAL HEALTH CHECKER
# ------------------------------------------------------------

def financial_health():

    print("\n--- FINANCIAL HEALTH REPORT ---")

    if savings_percentage >= 40:
        print("Financial Health: EXCELLENT")
        print("You have an excellent savings rate!")

    elif savings_percentage >= 25:
        print("Financial Health: GOOD")
        print("You are managing your finances well.")

    elif savings_percentage >= 10:
        print("Financial Health: NEEDS IMPROVEMENT")
        print("Try reducing unnecessary expenses.")

    else:
        print("Financial Health: POOR")
        print("You should review your spending habits.")

    print(f"Your savings rate is {savings_percentage:.2f}%")

    if monthly_savings < 0:
        print("WARNING: Your expenses exceed your income!")

    print("-" * 40)


# ------------------------------------------------------------
# 7. DREAM GOAL CALCULATOR
# ------------------------------------------------------------

def dream_goal_calculator():

    print("\n--- DREAM GOAL CALCULATOR ---")

    print("1. Dream Car")
    print("2. Dream House")
    print("3. Custom Savings Goal")

    choice = input("\nChoose your goal (1-3): ").strip()

    if choice == "1":
        goal_name = "Dream Car"

    elif choice == "2":
        goal_name = "Dream House"

    elif choice == "3":
        goal_name = input("Enter your goal name: ").strip()

        if not goal_name:
            goal_name = "Custom Goal"

    else:
        print("Invalid choice!")
        return

    target_amount = get_positive_number(
        f"Enter the price of your {goal_name} (Rs.): "
    )

    remaining_amount = target_amount - current_savings

    print("\n--- YOUR GOAL REPORT ---")
    print(f"Goal              : {goal_name}")
    print(f"Target Amount     : Rs. {target_amount:,.2f}")
    print(f"Current Savings   : Rs. {current_savings:,.2f}")

    if remaining_amount <= 0:
        print("Congratulations! You have already achieved your goal.")

    elif monthly_savings <= 0:
        print("You currently have no positive monthly savings.")
        print("Reduce expenses or increase income to reach this goal.")

    else:
        months_needed = remaining_amount / monthly_savings

        # Round up because a partial month still requires another month.
        months_needed = int(months_needed) + (
            months_needed % 1 > 0
        )

        years = months_needed // 12
        months = months_needed % 12

        print(f"Amount Remaining  : Rs. {remaining_amount:,.2f}")
        print(f"Time Required     : {months_needed} months")

        if years > 0:
            print(f"Estimated Time    : {years} years and {months} months")
        else:
            print(f"Estimated Time    : {months} months")

    print("-" * 40)


# ------------------------------------------------------------
# 8. ANNUAL SAVINGS CALCULATOR
# ------------------------------------------------------------

def calculate_annual_savings():

    print("\n--- ANNUAL SAVINGS REPORT ---")

    print(f"Monthly Savings : Rs. {monthly_savings:,.2f}")
    print(f"Annual Savings  : Rs. {annual_savings:,.2f}")

    if annual_savings > 0:
        print("You are building your wealth!")
    elif annual_savings == 0:
        print("You are breaking even.")
    else:
        print("Your yearly expenses exceed your income.")

    print("-" * 40)


# ------------------------------------------------------------
# 9. MAIN INTERACTIVE MENU
# ------------------------------------------------------------

while True:

    print("\n" + "=" * 55)
    print("              MAIN MENU")
    print("=" * 55)

    print("1. View Financial Profile")
    print("2. Calculate Monthly Savings")
    print("3. Check Financial Health")
    print("4. Calculate Dream Goal Timeline")
    print("5. Display Annual Savings")
    print("6. Exit")

    print("=" * 55)

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        display_profile()

    elif choice == "2":
        calculate_savings()

    elif choice == "3":
        financial_health()

    elif choice == "4":
        dream_goal_calculator()

    elif choice == "5":
        calculate_annual_savings()

    elif choice == "6":
        print("\nThank you for using Personal Finance Tracker!")
        print(f"Goodbye, {name}! Keep working towards your goals.")
        print("=" * 55)
        break

    else:
        print("\nInvalid choice! Please select a number between 1 and 6.")


# ============================================================
#                     PROGRAM ENDED
# ============================================================
