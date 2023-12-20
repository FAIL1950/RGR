class View:

    def show_menu(self):
        self.show_message("\nMenu:")
        self.show_message("1. Add row")
        self.show_message("2. View rows")
        self.show_message("3. Update row")
        self.show_message("4. Delete row")
        self.show_message("5. Rand event")
        self.show_message("6. Number of Events")
        self.show_message("7. Call")
        self.show_message("8. Quit")
        return input("Enter your choice: ")


    def show_extra_menu(self):
        self.show_message("\nTables: ")
        self.show_message("1. Tourists")
        self.show_message("2. Organizers")
        self.show_message("3. Events")
        self.show_message("4. Phone_nums")
        self.show_message("5. Back")
        return input("Enter your choice: ")

    def show_tourists(self, j):
        print("Tourists: ")
        for i in j:
            print(f"TouristID: {i[0]}, F_name: {i[1]}, L_name: {i[2]}, email: {i[3]}")

    def show_organizers(self, j):
        print("Organizers: ")
        for i in j:
            print(f"OrganizerID: {i[0]}, F_name: {i[1]}, L_name: {i[2]}, email: {i[3]}")

    def show_events(self, j):
        print("Events: ")
        for i in j:
            print(f"EventID: {i[0]}, Title: {i[1]}, Type: {i[2]}, Date: {i[3]}, Address_ID: {i[4]}")

    def show_nums(self, j):
        print("Phone_nums: ")
        for i in j:
            print(f"PhoneID: {i[0]}, Tourist_ID: {i[1]}, Number: {i[2]}")

    def show_t_e(self, j):
        print("Tourists/Events: ")
        for i in j:
            print(f"Tourist: {i[0]}, Event_t: {i[1]}, booking_time: {i[2]}")

    def show_o_e(self, j):
        print("Оrganizers/Events: ")
        for i in j:
            print(f"Оrganizer: {i[0]}, Event_o: {i[1]}")

    def show_call(self, j):
        print("Number of events that will take place starting tomorrow: ")
        for i in j:
            print(f"AddressID: {i[0]}, cnt: {i[1]}, AddressID: {i[2]}, Country: {i[3]}, City: {i[4]}, Street: {i[5]}, House: {i[6]}")

    def get_tourist_organizer_input(self):
        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")
        email = input("Enter email: ")
        return f_name,l_name,email
    def get_event_input(self):
        title = input("Enter event title: ")
        type_ = input("Enter event type: ")
        date = input("Enter event date: ")
        address_id = input("Enter event address_id: ")
        return title, type_, date, address_id

    def get_phone_input(self):
        tourist_id = input("Enter tourist_id: ")
        number = input("Enter number: ")
        return tourist_id, number

    def get_id(self):
        return input("Enter ID: ")

    def get_cnt(self):
        return input("Enter enter number of lines to create: ")

    def show_message(self, message):
        print(message)
