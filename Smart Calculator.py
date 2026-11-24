#  Smart Calculator
print("--- Welcome to the Smart Calculator ---")

# now ask user their two numbers
num_1 = float(input("\nEnter your Number 1 : "))
num_2 = float(input("Enter your Number 2 : "))

#  now ask what kind of operations user want to calculate
operation = input("Choose an operation (+,-.*,/,%) : " )

#  now performing the operations from users demand

if operation == "+":
    print("Result :" , num_1 + num_2)
elif operation == "-":
    print("Result :", num_1 - num_2)
elif operation == "*":
    print("Result : ", num_1*num_2)
elif operation == "/":
    if num_2 == 0:
        print("Numbers cannot be divided by 0")
    else:
        print("Result :", num_1/num_2)
elif operation == "%":
    print("Reminder :" , num_1 % num_2)
else:
    print("Invalid Format Entered, Check your operations please.")