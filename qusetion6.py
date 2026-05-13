# Mini Shopping Cart System

cart = []
prices = []

while True:

    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Search Item")
    print("4. Calculate Total Bill")
    print("5. Display Duplicate Items")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add item
    if choice == 1:
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))

        cart.append(item)
        prices.append(price)

        print("Item added successfully.")

    # Remove item
    elif choice == 2:
        item = input("Enter item name to remove: ")

        if item in cart:
            index = cart.index(item)

            cart.pop(index)
            prices.pop(index)

            print("Item removed successfully.")

        else:
            print("Item not found.")

    # Search item
    elif choice == 3:
        item = input("Enter item name to search: ")

        if item in cart:
            print("Item found in cart.")
        else:
            print("Item not found.")

    # Calculate total bill
    elif choice == 4:
        total = sum(prices)
        print("Total Bill =", total)

    # Display duplicate items
    elif choice == 5:
        duplicates = []

        for item in cart:
            if cart.count(item) > 1 and item not in duplicates:
                duplicates.append(item)

        print("Duplicate Items:", duplicates)

    # Exit
    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")    