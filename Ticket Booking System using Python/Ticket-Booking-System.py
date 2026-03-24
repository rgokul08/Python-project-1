seats = 50
while True:
 	print("\n--- Ticket Booking System ---")
 	print("1. Check Available Seats")
 	print("2. Book Ticket")
 	print("3. Exit")
 	choice = int(input("Enter your choice: "))
 	if choice == 1:
 		print("Available Seats:", seats)
 	elif choice == 2:
 		tickets = int(input("Enter number of tickets: "))
 		if tickets <= seats:
 			seats = seats - tickets
 			print("Booking Successful!")
 			print("Remaining Seats:", seats)
 		else:
 			print("Sorry! Not enough seats available.")
 	elif choice == 3:
 		print("Thank you for booking!")
 		break
	 else:
 		print("Invalid Choice")