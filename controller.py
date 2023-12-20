from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == '1':
                c1 = self.view.show_extra_menu()
                if c1 == '1':
                    self.add_new_tourist()
                elif c1 == '2':
                    self.add_new_organizer()
                elif c1 == '3':
                    self.add_new_event()
                elif c1 == '4':
                    self.add_new_phone_num()


            elif choice == '2':
                c1 = self.view.show_extra_menu()
                if c1 == '1':
                    self.view_t()
                elif c1 == '2':
                    self.view_o()
                elif c1 == '3':
                    self.view_e()
                elif c1 == '4':
                    self.view_p()
            elif choice == '3':
                c1 = self.view.show_extra_menu()
                if c1 == '1':
                    self.update_t()
                elif c1 == '2':
                    self.update_o()
                elif c1 == '3':
                    self.update_e()
                elif c1 == '4':
                    self.update_p()
            elif choice == '4':
                c1 = self.view.show_extra_menu()
                if c1 == '1':
                    self.delete_t()
                elif c1 == '2':
                    self.delete_o()
                elif c1 == '3':
                    self.delete_e()
                elif c1 == '4':
                    self.delete_p()
            elif choice == '5':
                self.rand_event()
            elif choice == '6':
                self.event_cnt()
            elif choice == '7':
                self.view_call()
            elif choice == '8':
                break








    def add_new_tourist(self):
        f_name,l_name,email = self.view.get_tourist_organizer_input()
        b,msg = self.model.add_tourist(f_name,l_name,email)
        if b:
            self.view.show_message("Tourist added successfully!")
        else:
            self.view.show_message(msg)

    def add_new_organizer(self):
        f_name,l_name,email = self.view.get_tourist_organizer_input()
        b,msg = self.model.add_organizer(f_name,l_name,email)
        if b:
            self.view.show_message("Organizer added successfully!")
        else:
            self.view.show_message(msg)

    def add_new_event(self):
        title, type_, date, address_id = self.view.get_event_input()
        b,msg = self.model.add_event(title, type_, date, address_id)
        if b:
            self.view.show_message("Event added successfully!")
        else:
            self.view.show_message(msg)

    def add_new_phone_num(self):
        tourist_id, number = self.view.get_phone_input()
        b,msg = self.model.add_phone_num(tourist_id, number)
        if b:
            self.view.show_message("Event added successfully!")
        else:
            self.view.show_message(msg)

    def view_t(self):
        t = self.model.get_all('"Tourists"', '"TouristID"')
        self.view.show_tourists(t)

    def view_o(self):
        t = self.model.get_all('"Оrganizers"', '"ОrganizerID"')
        self.view.show_organizers(t)

    def view_e(self):
        t = self.model.get_all('"Events"', '"EventID"')
        self.view.show_events(t)

    def view_p(self):
        t = self.model.get_all('"Phone_nums"', '"PhoneID"')
        self.view.show_nums(t)

    def update_t(self):
        id = self.view.get_id()
        f_name, l_name, email = self.view.get_tourist_organizer_input()
        b, strr = self.model.update_tour(id, f_name, l_name, email)
        if b:
            self.view.show_message(f"Tourist id = {id} updated successfully!")
        else:
            self.view.show_message(strr)

    def update_o(self):
        id = self.view.get_id()
        f_name, l_name, email = self.view.get_tourist_organizer_input()
        b, strr = self.model.update_org(id, f_name, l_name, email)
        if b:
            self.view.show_message(f"Organizer id = {id} updated successfully!")
        else:
            self.view.show_message(strr)

    def update_e(self):
        id = self.view.get_id()
        title, type_, date, address_id = self.view.get_event_input()
        b, strr = self.model.update_event(id, title, type_, date, address_id)
        if b:
            self.view.show_message(f"Event id = {id} updated successfully!")
        else:
            self.view.show_message(strr)

    def update_p(self):
        id = self.view.get_id()
        tourist_id, number = self.view.get_phone_input()
        b, strr = self.model.update_phone(id, tourist_id, number)
        if b:
            self.view.show_message(f"Phone id = {id} updated successfully!")
        else:
            self.view.show_message(strr)

    def delete_p(self):
        id = self.view.get_id()
        b = self.model.delete_p(id)
        if b:
            self.view.show_message("Phone deleted successfully!")
        else:
            self.view.show_message("ERROR: wrong id")

    def delete_t(self):
        id = self.view.get_id()
        b, t_e, p = self.model.cnt_t_fk(id)
        if not b:
            bb = self.model.delete_t(id)
            if bb:
                self.view.show_message("Tourist deleted successfully!")
            else:
                self.view.show_message("ERROR: wrong id")
        else:
            self.view.show_message("\nWARNING:\n")
            self.view.show_message("You need to manually delete these rows in the tables, due to the fact that they contain references to the id of the row being deleted, and then try to delete again")
            if t_e > 0:
                j = self.model.get_t_e(id)
                self.view.show_t_e(j)
            if p > 0:
                j = self.model.get_p(id)
                self.view.show_nums(j)

    def delete_o(self):
        id = self.view.get_id()
        b, o_e = self.model.cnt_o_fk(id)
        if not b:
            bb = self.model.delete_o(id)
            if bb:
                self.view.show_message("Organizer deleted successfully!")
            else:
                self.view.show_message("ERROR: wrong id")
        else:
            self.view.show_message("\nWARNING:\n")
            self.view.show_message(
                "You need to manually delete these rows in the tables, due to the fact that they contain references to the id of the row being deleted, and then try to delete again")
            if o_e > 0:
                j = self.model.get_o_e(id)
                self.view.show_o_e(j)

    def delete_e(self):
        id = self.view.get_id()
        b, e1,e2 = self.model.cnt_e_fk(id)
        if not b:
            bb = self.model.delete_e(id)
            if bb:
                self.view.show_message("Event deleted successfully!")
            else:
                self.view.show_message("ERROR: wrong id")
        else:
            self.view.show_message("\nWARNING:\n")
            self.view.show_message(
                "You need to manually delete these rows in the tables, due to the fact that they contain references to the id of the row being deleted, and then try to delete again")
            if e1 > 0:
                j = self.model.get_o_e(id)
                self.view.show_o_e(j)
            if e2 > 0:
                j = self.model.get_t_e(id)
                self.view.show_t_e(j)

    def rand_event(self):
        n = int(self.view.get_cnt())
        self.model.rand_event(n)
        self.view.show_message("%s rows were created in the Events table" %n)

    def event_cnt(self):
        self.view.show_message("Number of Events: " + str(self.model.cnt_events()))

    def view_call(self):
        t = self.model.call()
        self.view.show_call(t)