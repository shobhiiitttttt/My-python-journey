# if : executes if the condition is True
# if-else : executes if True, another if False
# if-elif-else : checks multiples conditions in sequence

# FOR PRACTISING 
# Q1. Accept two numbers and print the greatest between them.
# Q2. Accept the gender from the user as char and print the
# respective greeting message
# Ex - Good Morning Sir (on the basis of gender)
# Q3. Accept an integer and check whether it is an even number
# or odd.
# Q4. Accept name and age from the user. Check if the user is a
# valid voter or not.
# Ex- “hello shery you are a valid voter”
# Q5. Accept a year and check if it a leap year or not (google to
# find out what is a leap year)\

# answer 1
# num_1 = int(input("Enter the number 1 : " ))
# num_2 = int(input("Enter the number 2 : "))
# 
# if num_1 > num_2:
#     print(f"{num_1} is greater than {num_2}")
# elif num_1 == num_2:
#     print("Both of the values are equal")
# else:
#     print(f"{num_2} is greater than {num_1}")
    
# answer2
# options = f"""
# Select your gender
# 1 . Male
# 2 . Female
# 3 . Others"""
# print(options)
# gen = int(input("Select you gender (1-3) :"))
# if gen == 1:
#     print("Good Morning Sir")
# elif gen == 2:
#     print("Good Morning Maam")
# else:
#     print("Good morning broski")

# # answer 3
# num = int(input("Enter the number :"))
# if num%2 == 0:
#     print("EVEN Numbers")
# else:
#     print("ODD Numbers")

# answer4

# age = int(input("Enter your age :"))
# name = input("Enter your name :")
# age_vote = 18
# diff = age_vote - age
# if age >= 18:
#     print(f"{name} is a valid voter")
# else:
#     print(f"{name} is unable to vote and can vote after {diff} years")

# answer 5
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")