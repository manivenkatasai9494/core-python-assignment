class TicketBooking:
    def __init__(self, total_seats, booked_seats):
        self.total_seats = total_seats
        self.booked_seats = booked_seats
        self.available_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

    def book_seat(self, seat_no):
        if seat_no in self.available_seats:
            self.available_seats.remove(seat_no)
            self.booked_seats.append(seat_no)
            print(f"Seat {seat_no} is booked successfully!")
        else:
            print(f"Seat {seat_no} is already booked or invalid.")

    def cancel_seat(self, seat_no):
        if seat_no in self.booked_seats:
            self.booked_seats.remove(seat_no)
            self.available_seats.append(seat_no)
            print(f"Seat {seat_no} is cancelled successfully!")
            self.available_seats.sort()
        else:
            print(f"Seat {seat_no} is not booked or invalid.")

    def get_availability(self):
        return self.available_seats

    def view_seat_options(self):
        while True:
            try:
                print("\n=================================")
                print("1. Book a Seat.")
                print("2. Cancel a Seat.")
                print("3. View Available Seats.")
                print("4. Exit.")
                print("=================================")
                option = int(input("Enter your choice: "))

                if option == 1:
                    seat_to_book = int(input("Enter seat number to book: "))
                    self.book_seat(seat_to_book)
                elif option == 2:
                    seat_to_cancel = int(input("Enter seat number to cancel: "))
                    self.cancel_seat(seat_to_cancel)
                elif option == 3:
                    print("Available Seats: ", self.get_availability())
                elif option == 4:
                    print("Thank you! Have a great experience!")
                    break
                else:
                    print("Invalid option. Please select a valid option.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")


total_seats = int(input("Total number of seats: "))
input_str = input("Enter booked seats (separate by commas): ").strip()
if input_str:
    booked_seats = list(map(int, input_str.split(',')))
    print("Booked seats:", booked_seats)
else:
    booked_seats = []

ticket_booking = TicketBooking(total_seats, booked_seats)
ticket_booking.view_seat_options()
