

#railway form
#---------------------

class RailwayForm:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
        self.destination = ""
        self.ticket_type = ""

    def get_details(self):
        print("Welcome to Railway Ticket Booking Form")
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.gender = input("Enter your gender: ")
        self.destination = input("Enter your destination: ")
        self.ticket_type = input("Enter ticket type (e.g., First Class, Second Class): ")

    def display_details(self):
        print("\n------ Ticket Details ------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Destination: {self.destination}")
        print(f"Ticket Type: {self.ticket_type}")

    def save_form(self):
        try:
            with open("railway_form.txt", "a") as file:
                file.write(f"Name: {self.name}\n")
                file.write(f"Age: {self.age}\n")
                file.write(f"Gender: {self.gender}\n")
                file.write(f"Destination: {self.destination}\n")
                file.write(f"Ticket Type: {self.ticket_type}\n\n")
            print("Form saved successfully!")
        except Exception as e:
            print("Error occurred while saving the form:", e)

    def modify_form(self):
        try:
            with open("railway_form.txt", "r") as file:
                forms = file.readlines()
                if forms:
                    print("\n------ Modify Form ------")
                    for i, form in enumerate(forms):
                        print(f"{i}. {form.strip()}")
                    index = int(input("\nEnter the index of the form you want to modify: "))
                    if 0 <= index < len(forms):
                        form_to_modify = forms[index]
                        print("\n------ Modify Details ------")
                        self.get_details()  # Get new details
                        forms[index] = f"Name: {self.name}\n" \
                                       f"Age: {self.age}\n" \
                                       f"Gender: {self.gender}\n" \
                                       f"Destination: {self.destination}\n" \
                                       f"Ticket Type: {self.ticket_type}\n\n"
                        with open("railway_form.txt", "w") as file:
                            file.writelines(forms)
                        print("Form modified successfully!")
                    else:
                        print("Invalid index.")
                else:
                    print("No forms found.")
        except FileNotFoundError:
            print("No forms found.")

    def submit_form(self):
        self.get_details()
        self.display_details()
        self.save_form()

        # Allow modification after submitting form
        self.modify_form()

    @staticmethod
    def read_saved_forms():
        try:
            with open("railway_form.txt", "r") as file:
                forms = file.readlines()
                if forms:
                    print("\n------ Saved Forms ------")
                    for form in forms:
                        print(form.strip())
                else:
                    print("No forms found.")
        except FileNotFoundError:
            print("No forms found.")


if __name__ == "__main__":
    form = RailwayForm()
    form.submit_form()

    # // Read and display updated saved forms
    RailwayForm.read_saved_forms()
    #--------------------------------------------------
