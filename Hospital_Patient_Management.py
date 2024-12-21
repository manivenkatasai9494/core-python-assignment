class HospitalManagement:
    def __init__(self):
        self.patients = []

    def add_patient(self):
        name = input("Enter Patient's Name: ")
        age = int(input("Enter Patient's Age: "))
        disease = input("Enter Patient's Disease: ")
        self.patients.append({"Name": name, "Age": age, "Disease": disease})
        print(f"Patient {name} has been added successfully!")

    def delete_patient(self):
        print("\nCurrent Patient Records:")
        self.view_all_patients()
        name = input("Enter the Patient's Name you want to delete: ")
        patient_to_delete = next((p for p in self.patients if p["Name"] == name), None)
        if patient_to_delete:
            self.patients.remove(patient_to_delete)
            print(f"Patient {name} has been removed successfully!")
        else:
            print(f"No patient found with the name '{name}'.")

    def view_all_patients(self):
        if not self.patients:
            print("No patient records available.")
        else:
            print("Patient Records:")
            for patient in self.patients:
                print(f"Name: {patient['Name']}, Age: {patient['Age']}, Disease: {patient['Disease']}")

    def search_by_disease(self):
        disease = input("Enter the disease to search for patients: ")
        matching_patients = [p["Name"] for p in self.patients if p["Disease"].lower() == disease.lower()]
        if matching_patients:
            print(f"Patients with {disease}: {matching_patients}")
        else:
            print(f"No patients found with the disease '{disease}'.")

    def end(self):
        print("========== Thank you! Visit Again ==========")
        exit()

    def view_options(self):
        while True:
            try:
                print("\n===================================")
                print("1. Add a Patient.")
                print("2. Delete a Patient.")
                print("3. View All Patients.")
                print("4. Search Patients by Disease.")
                print("5. Exit.")
                print("===================================")
                operation = int(input("Enter your choice: "))
                match operation:
                    case 1:
                        self.add_patient()
                    case 2:
                        self.delete_patient()
                    case 3:
                        self.view_all_patients()
                    case 4:
                        self.search_by_disease()
                    case 5:
                        self.end()
                    case _:
                        print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 5.")

hospital = HospitalManagement()
hospital.view_options()
