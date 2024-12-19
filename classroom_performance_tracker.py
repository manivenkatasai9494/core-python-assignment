

print("==========Classroom Performance Tracker==========")

class ClassroomPerformanceTracker:
    students = {}

    def AddStudent(self):
        name = input("Enter the Student Name = ")
        grades = []
        for i in range(1, 4):
            grade = input(f"Enter Marks Obtained in Subject {i}: ")
            if grade:
                grades.append(int(grade))
            else:
                break
        self.students[name] = grades
        print(f"Student => {name} added with Marks => {grades}")

    def AverageMarksOfStudents(self):
        print("==========Average Marks of Students==========")
        if not self.students:
            print("No students added.")
        else:
            for name, grades in self.students.items():
                average = sum(grades) / len(grades) if grades else 0
                print(f"Student: {name}, Average Marks = {average:.2f}")

    def ViewStudents(self):
        print("==========Student List==========")
        if not self.students:
            print("No students added.")
        else:
            for index, (name, grades) in enumerate(self.students.items(), start=1):
                print(f"{index}. {name} = {grades}")

    def TopPerformer(self):
        if not self.students:
            print("No students added.")
        else:
            top_student = None
            top_avg = -1
            for name, grades in self.students.items():
                average = sum(grades) / len(grades) if grades else 0
                if average > top_avg:
                    top_avg = average
                    top_student = name
            if top_student:
                print(f"Top Performer: {top_student} ===>>> {top_avg:.2f}")
            else:
                print("No students to determine the top performer.")

    def ViewOptions(self):
        while True:
            try:
                self.clear_screen()  # Clear the screen at the beginning of each option
                print("================================")
                print("1. Add Student")
                print("2. View Students")
                print("3. View Average Marks of Students")
                print("4. View Top Performer")
                print("5. Exit")
                print("================================")
                operation = int(input("Enter Option = "))
                match operation:
                    case 1:
                        self.AddStudent()
                    case 2:
                        self.ViewStudents()
                    case 3:
                        self.AverageMarksOfStudents()
                    case 4:
                        self.TopPerformer()
                    case 5:
                        print("Exiting the program.")
                        exit()
                    case _:
                        print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 5.")

object = ClassroomPerformanceTracker()
object.ViewOptions()
