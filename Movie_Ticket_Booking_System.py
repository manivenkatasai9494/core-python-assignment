class TicketBooking:
    def __init__(self,total_seats,booked_seats):
        self.total_seats=total_seats
        self.booked_seats=booked_seats
        self.available_seats=[seat for seat in range(1,total_seats+1) if seat not in booked_seats]

    def book_seat(self,seat_no):
        if seat_no in self.available_seats:
            self.available_seats.remove(seat_no)
            self.booked_seats.append(seat_no)
            print(f"Seat {seat_no} is booked successfuly!")
        else:
            print(f"Seat {seat_no} is already booked or invalid")

    def cancel_seat(self,seat_no):
        if seat_no in self.booked_seats:
            self.booked_seats.remove(seat_no)
            self.available_seats.append(seat_no)
            print(f"Seat {seat_no} is cancelled successfuly!")
            self.available_seats.sort()
        else:
            print(f"Seat {seat_no} is not booked or invalid")

    def get_availability(self):
        return self.available_seats


total_seats=int(input("Total no. of seats: "))
input_str = input("Enter booked seats (separate by comma): ").strip()
if input_str:
    booked_seats = list(map(int, input_str.split(',')))
    print("Booked seats:", booked_seats)
else:
    print("No seats entered!")

ticket=TicketBooking(total_seats,booked_seats)
while True:
    print("\nAvailable seats: ",ticket.get_availability())
    action = input("Do you want Book or Cancel a seat?(Enter 'E' to stop): ").lower()
    if action=='b':
        seat_to_book=int(input("Enter  seat no. to book: "))
        ticket.book_seat(seat_to_book)
    elif action=='c':
        seat_to_cancel=int(input("Enter seat no. to cancel: "))
        ticket.cancel_seat(seat_to_cancel)
    elif action=='e':
        print("Have a great experience!!")
        break
    else:
        print("Invalid action. Please enter 'B' to book or 'C' to cancel.")

