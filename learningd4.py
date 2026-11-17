a = "100"
b = int(a)

print(b)
print(type(b))\
                
                
# Ask the users name and age.
# Ask their monthly income.
# Ask their monthly expenses.
# Calculate monthly savings.
# Ask their dream car and house prices.
# Calculate how many months are needed to reach a savings target.
# Display a formatted financial report.
# Show a motivational message using the users name.

print("------Personal Life and Financail Trainer------")
name = input("Enter your name :")
age = int(input("Enter your age :"))

monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your monthly expense :"))

# calculating your monthly savings
savings = monthly_income - monthly_expenses

dream_car = input("Enter your dream car name :")
dream_house_price = int(input("Enter you dream house price:"))

print(f"Your Total Saving Is : {savings}")

# calculating number of month to reaching the target
target = dream_house_price / savings
print(f"So Total number of months to reach the target is{target}")

print(f"\nYour name is {name}")
print(f"Your age is {age}")
print(f"Your monthly income is {monthly_income}")
print(f"Your monthly saving expense is {monthly_expenses}")
print(f"Your monthly saving is {savings}")
print(f"Your dream car name is {dream_car}")
print(f"Your dream house price is {dream_house_price}")
print(f"Total number of months you gonna take is around{target}")


