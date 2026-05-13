# Train Seat Reservation System

# Create 20 seats initialized to 0
seats = [0] * 20

while True:
    print("\n1.Book Seat")
    print("2.Cancel Seat")
    print("3.Show Seats")
    print("4.Booking Percentage")
    print("5.Exit")

    choice = int(input("Enter your choice: "))

    # Book a seat
    if choice == 1:
        seat_no = int(input("Enter seat number (1-20): "))

        if seat_no < 1 or seat_no > 20:
            print("Invalid seat number!")

        elif seats[seat_no - 1] == 1:
            print("Seat already booked!")

        else:
            seats[seat_no - 1] = 1
            print("Seat booked successfully.")

    # Cancel a seat
    elif choice == 2:
        seat_no = int(input("Enter seat number to cancel (1-20): "))

        if seat_no < 1 or seat_no > 20:
            print("Invalid seat number!")

        elif seats[seat_no - 1] == 0:
            print("Seat is already available.")

        else:
            seats[seat_no - 1] = 0
            print("Seat cancelled successfully.")

    # Display seats
    elif choice == 3:
        print("\nSeat Status:")
        for i in range(20):
            status = "Booked" if seats[i] == 1 else "Available"
            print("Seat", i + 1, ":", status)

    # Booking percentage
    elif choice == 4:
        booked = seats.count(1)
        percentage = (booked / 20) * 100
        print("Booking Percentage =", percentage, "%")

    # Exit
    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")