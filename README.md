

# ==========================================
#       CODEBITE RESTAURANT
#       Restaurant Ordering System
# ==========================================

print("====================================")
print("       WELCOME TO CODEBITE")
print("====================================")

# FOOD MENU
menu = {
    "1": ("Burger", 120),
    "2": ("Pizza", 250),
    "3": ("Sandwich", 100),
    "4": ("French Fries", 80),
    "5": ("Cold Coffee", 90),
    "6": ("Pasta", 180),
    "7": ("Momos", 100),
    "8": ("Ice Cream", 70)
}

# EMPTY CART
cart = []

# DISPLAY MENU
print("\n========== FOOD MENU ==========")

for item_number, details in menu.items():
    print(f"{item_number}. {details[0]} - Rs.{details[1]}")

print("================================")

# MULTIPLE ITEM ORDERING SYSTEM

while True:

    item = input("\nEnter food item number (0 to finish): ")

    if item == "0":
        break

    if item not in menu:
        print("Invalid Food Item! Please try again.")
        continue

    quantity = input("Enter quantity: ")

    if not quantity.isdigit() or int(quantity) <= 0:
        print("Invalid quantity! Enter a positive number.")
        continue

    quantity = int(quantity)

    food_name = menu[item][0]
    food_price = menu[item][1]

    item_total = food_price * quantity

    # ADD ITEM TO CART
    cart.append({
        "name": food_name,
        "price": food_price,
        "quantity": quantity,
        "total": item_total
    })

    print(f"\n{food_name} added successfully!")
    print(f"Item Total: Rs.{item_total}")

# CHECK EMPTY CART

if len(cart) == 0:

    print("\nYour cart is empty.")
    print("Thank you for visiting CodeBite!")

else:

    # CALCULATE TOTAL PRICE

    total_price = sum(item["total"] for item in cart)

    # DISPLAY ORDER SUMMARY

    print("\n========== ORDER SUMMARY ==========")

    for item in cart:
        print(
            f"{item['name']} x {item['quantity']} "
            f"= Rs.{item['total']}"
        )

    print("-----------------------------------")
    print(f"Total Price: Rs.{total_price}")

    # ORDER CONFIRMATION

    choice = input(
        "\nDo you want to confirm this order? (yes/no): "
    ).lower().strip()

    if choice == "yes":

        print("\nYour order has been confirmed!")
        print("Thank you for ordering with CodeBite Restaurant.")

        # PAYMENT METHOD

        print("\n========== PAYMENT METHOD ==========")
        print("1. Cash Payment")
        print("2. UPI Payment")

        payment = input("Select payment method: ").strip()

        if payment == "1" or payment == "2":

            if payment == "1":
                payment_method = "Cash"

            else:
                payment_method = "UPI"

            # FINAL ORDER RECEIPT

            print("\n====================================")
            print("          CODEBITE RECEIPT")
            print("====================================")

            for item in cart:
                print(f"\nFood Item: {item['name']}")
                print(f"Price: Rs.{item['price']}")
                print(f"Quantity: {item['quantity']}")
                print(f"Item Total: Rs.{item['total']}")

            print("------------------------------------")
            print(f"Grand Total: Rs.{total_price}")
            print(f"Payment Method: {payment_method}")
            print("------------------------------------")
            print("       THANK YOU FOR VISITING")
            print("             CODEBITE")
            print("           VISIT AGAIN!")
            print("====================================")

        else:
            print("\nInvalid Payment Method!")
            print("Please try again.")

    elif choice == "no":

        print("\nYour order has been cancelled.")

    else:

        print("\nInvalid Choice!")

# EXIT MESSAGE

print("\nThank you for visiting CodeBite Restaurant!")
print("Have a wonderful day!")
