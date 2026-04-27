while True:
    print("\nMenu:")
    print("1. Check even/odd")
    print("2. Check positive/negative")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

    elif choice == 2:
        num = int(input("Enter a number: "))
        if num > 0:
            print("Positive number")
        elif num < 0:
            print("Negative number")
        else:
            print("Zero")

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
