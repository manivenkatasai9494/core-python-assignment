class CustomerFeedback:
    def __init__(self, ratings):
        self.ratings = ratings
    def calculate_positive_feedback(self):
        if not self.ratings:
            print("No ratings available to calculate positive feedback.")
            return

        total_ratings = len(self.ratings)
        positive_ratings = len([rating for rating in self.ratings if rating >= 4])
        positive_percentage = (positive_ratings / total_ratings) * 100

        print(f"Positive Feedback: {positive_percentage:.2f}%")

    def add_rating(self):
        try:
            rating = int(input("Enter a new rating (1-5): "))
            if 1 <= rating <= 5:
                self.ratings.append(rating)
                print("Rating added")
            else:
                print("Invalid rating")
        except ValueError:
            print("Invalid input")

    def view_options(self):
        while True:
            print("\n========================")
            print("1. View all ratings.")
            print("2. Add a new rating.")
            print("3. Calculate positive feedback.")
            print("4. Exit.")
            print("========================")
            choice = input("Enter your choice: ")
            if choice == '1':
                print(f"Current ratings: {self.ratings}")
            elif choice == '2':
                self.add_rating()
            elif choice == '3':
                self.calculate_positive_feedback()
            elif choice == '4':
                print("Thank you for using the feedback analysis system!")
                break
            else:
                print("Invalid option. Please try again.")

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
feedback_system = CustomerFeedback(ratings)
feedback_system.view_options()
