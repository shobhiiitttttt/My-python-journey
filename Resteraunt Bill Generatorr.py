# CodeBite Restaurant

print("=========================================")
print("          CODEBITE RESTAURANT")
print("=========================================")

print("\nWelcome Sir/Ma'am, Happy Ordering")
print("\n1. View Food Menu")
print("2. Place Order")
print("3. Exit")

choice = input("Enter Your Choice :")

if choice == "1":
    print("=====CODEBITE RESTAURANT=====")
    print("1. Burger - Rs. 120/-")
    print("2. Pizza - Rs. 250/-")
    print("3. Sandwich - Rs. 100/-")
    print("4. Pasta - Rs. 180/-")
    print("5. French Fries - Rs. 90/-")
    print("6. Cold Coffee - Rs. 110/-")
    print("7. Noodles - Rs. 150/-")
    print("8. Momos - Rs. 100/-")
    print("9. Paneer Roll - Rs. 130/-")
    print("10. Ice Cream - Rs. 80/-")
    item = input("Enter the food item number : ")
    quantity = int(input("Enter Quantity :"))
    print(f"Your selected item number {item}")
    print(f"Your selected item quantity is {quantity}")
    price =0
    if item == "1":
        price = 120
    elif item == "2":
        price = 250
    elif item == "3":
        price = 100
    elif item == "4":
        price = 180
    elif item == "5":
        price = 90
    elif item == "6":
        price = 110
    elif item == "7":
        price = 150
    elif item == "8":
        price = 100
    elif item == "9":
        price = 130
    elif item == "10":
        price = 80
    else:
        print("Invalid Food Item")
    if price > 0:
        total_price = price * quantity
        print(f"Your Total Price is Rs.{total_price}")
        confirm = input("\nDo you want to confirm this order? (yes/no) : ")
        if confirm == "yes":
            print("Your order has been confirmed")
            print("\nThankyou for ordering with CodeBite Resteraunt")
            payment = input("\nSelect a payment method (1.Cash/2.UPI) : ")
            if payment == "1":
                print("You selected Cash Payment")
            elif payment == "2":
                print("You selected UPI Payment")
            else:
                print("Invalid Payment Method")
            if payment == "1" or payment == "2":
                print("\n======ORDER RECIPT======")
                print("Thankypu for choosing CODEBITE")
                print(f"Food Item Number : {item}")
                print(f"Quantity : {quantity}")
                print(f"Total Price : {total_price}")
                print(f"Payment method : {payment}")
                print("==========VISIT AGAIN==========")
        else:
            print("Your order has been cancelled")
elif choice == "2":
    print("Lets Place Your Order")
elif choice == "3":
    print("Thankyou for visiting!")
else:
    print("Invalid Choice!")