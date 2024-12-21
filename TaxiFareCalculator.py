class TaxiFareCalculator:
    def __init__(self, base_fare, distance_rate):
        self.base_fare = base_fare
        self.distance_rate = distance_rate
        self.trips = []

    def add_trip(self):
        try:
            distance = float(input("Enter the distance for the trip (in km): "))
            if distance > 0:
                self.trips.append(distance)
                print(f"Trip with distance {distance} km added successfully.")
            else:
                print("Distance must be greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    def calculate_fare(self, distance):
        return self.base_fare + (self.distance_rate * distance)

    def calculate_total_fare(self):
        if not self.trips:
            print("No trips available to calculate fare.")
            return

        total_fare = sum(self.calculate_fare(distance) for distance in self.trips)
        print("\nTrip Details and Fares:")
        for i, distance in enumerate(self.trips, start=1):
            fare = self.calculate_fare(distance)
            print(f"Trip {i}: Distance = {distance} km, Fare = ${fare:.2f}")
        print(f"\nTotal Fare for All Trips: ${total_fare:.2f}")

    def view_options(self):
        while True:
            print("\n========================")
            print("1. View all trips.")
            print("2. Add a new trip.")
            print("3. Calculate total fare.")
            print("4. Exit.")
            print("========================")
            choice = input("Enter your choice: ")
            if choice == '1':
                print(f"Current trips: {self.trips}")
            elif choice == '2':
                self.add_trip()
            elif choice == '3':
                self.calculate_total_fare()
            elif choice == '4':
                print("Thank you for using the Taxi Fare Calculator!")
                break
            else:
                print("Invalid option. Please try again.")

base_fare = 50
distance_rate = 10
trips = [5, 10, 3]

fare_calculator = TaxiFareCalculator(base_fare, distance_rate)
fare_calculator.trips = trips
fare_calculator.view_options()
