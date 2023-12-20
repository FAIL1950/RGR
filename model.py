import psycopg2
import re
from datetime import datetime


class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='55krotvkaske',
            host='localhost',
            port=5432
        )

    def is_int(self, value):
        return value.isdigit()

    def is_date(self, input_string):
        try:
            datetime.strptime(input_string, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False
    def check_str(self, value, length):
        if len(value) <= length and len(value) >= 1:
            return True
        else:
            return False


    def is_email(self,email):
        pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
        if re.match(pattern, email) is not None:
            return True
        else:
            return False
    def is_correct_address_id(self, id):
        c = self.conn.cursor()
        if self.is_int(id):
            c.execute('SELECT COUNT(*) FROM "Address" WHERE "AddressID" = %s', (id,))
            r = c.fetchone()
            if r[0] == 0:
                return False
            elif r[0] == 1:
                return True
        else:
            return False

    def is_correct_organizer_id(self, id):
        c = self.conn.cursor()
        if self.is_int(id):
            c.execute('SELECT COUNT(*) FROM "Оrganizers" WHERE "ОrganizerID" = %s', (id,))
            r = c.fetchone()
            if r[0] == 0:
                return False
            elif r[0] == 1:
                return True
        else:
            return False

    def is_correct_event_id(self, id):
        c = self.conn.cursor()
        if self.is_int(id):
            c.execute('SELECT COUNT(*) FROM "Events" WHERE "EventID" = %s', (id,))
            r = c.fetchone()
            if r[0] == 0:
                return False
            elif r[0] == 1:
                return True
        else:
            return False
    def is_correct_tourist_id(self, id):
        c = self.conn.cursor()
        if self.is_int(id):
            c.execute('SELECT COUNT(*) FROM "Tourists" WHERE "TouristID" = %s', (id,))
            r = c.fetchone()
            if r[0] == 0:
                return False
            elif r[0] == 1:
                return True
        else:
            return False
    def is_correct_phone_id(self, id):
        c = self.conn.cursor()
        if self.is_int(id):
            c.execute('SELECT COUNT(*) FROM "Phone_nums" WHERE "PhoneID" = %s', (id,))
            r = c.fetchone()
            if r[0] == 0:
                return False
            elif r[0] == 1:
                return True
        else:
            return False

    def org_tour_check(self,f_name, l_name, email):
        if self.check_str(f_name,30):
            if self.check_str(l_name,30):
                if self.check_str(email,30):
                    if self.is_email(email):
                        return True, 'Ok'
                    else:
                        return False, 'ERROR: wrong email style'
                else:
                    return False, 'ERROR: wrong email length'
            else:
                return False, 'ERROR: wrong l_name length'
        else:
            return False, 'ERROR: wrong f_name length'
    def add_organizer(self, f_name, l_name, email):
        c = self.conn.cursor()
        b, strr = self.org_tour_check(f_name, l_name, email)
        if b:
            c.execute('INSERT INTO "Оrganizers" ("F_name", "L_name", email) VALUES (%s, %s, %s)',(f_name, l_name, email))
            self.conn.commit()
        return b,strr


    def add_tourist(self, f_name, l_name, email):
        c = self.conn.cursor()
        b, strr = self.org_tour_check(f_name, l_name, email)
        if b:
            c.execute('INSERT INTO "Tourists" ("F_name", "L_name", email) VALUES (%s, %s, %s)', (f_name, l_name, email))
            self.conn.commit()
        return b, strr

    def event_check(self,title, type_, date, address_id):
        if self.is_correct_address_id(address_id):
            if self.check_str(title,100):
                if self.check_str(type_,30):
                    if self.is_date(date):
                        return True, 'Ok'
                    else:
                        return False, 'ERROR: wrong date style'
                else:
                    return False, 'ERROR: wrong type length'
            else:
                return False, 'ERROR: wrong title length'
        else:
            return False, 'ERROR: wrong Address_ID'

    def add_event(self, title, type_, date, address_id):
        c = self.conn.cursor()
        b, strr = self.event_check(title, type_, date, address_id)
        if b:
            c.execute('INSERT INTO "Events" ("Title", "Type", "Date", "Address_ID") VALUES (%s, %s, %s, %s)', (title, type_, date, address_id))
            self.conn.commit()
        return b,strr

    def phone_check(self, tourist_id, number):
        if self.is_correct_tourist_id(tourist_id):
            if self.check_str(number,16):
                return True, 'Ok'
            else:
                return False, 'ERROR: wrong number length'
        else:
            return False, 'ERROR: wrong Tourist_ID'
    def add_phone_num(self, tourist_id, number):
        c = self.conn.cursor()
        b, strr = self.phone_check(tourist_id, number)
        if b:
            c.execute('INSERT INTO "Phone_nums" ("Tourist_ID", "Number") VALUES (%s, %s)',(tourist_id, number))
            self.conn.commit()
        return b,strr


    def get_all(self, strr, strr1):
        c = self.conn.cursor()
        c.execute('SELECT * FROM %s ORDER BY %s ASC' %(strr, strr1))
        return c.fetchall()

    def update_tour(self, id, f_name, l_name, email):
        c = self.conn.cursor()
        if self.is_correct_tourist_id(id):
            b,strr = self.org_tour_check(f_name, l_name, email)
            if b:
                c.execute('UPDATE "Tourists" SET "F_name"=%s, "L_name"=%s, email=%s WHERE "TouristID"=%s', (f_name, l_name, email, id))
                self.conn.commit()
            return b,strr
        else:
            return False, 'ERROR: wrong TouristID'

    def update_org(self, id, f_name, l_name, email):
        c = self.conn.cursor()
        if self.is_correct_organizer_id(id):
            b, strr = self.org_tour_check(f_name, l_name, email)
            if b:
                c.execute('UPDATE "Оrganizers" SET "F_name"=%s, "L_name"=%s, email=%s WHERE "ОrganizerID"=%s', (f_name, l_name, email, id))
                self.conn.commit()
            return b,strr
        else:
            return False, 'ERROR: wrong ОrganizerID'

    def update_event(self, id, title, type_, date, address_id):
        c = self.conn.cursor()
        if self.is_correct_event_id(id):
            b, strr = self.event_check(title, type_, date, address_id)
            if b:
                c.execute('UPDATE "Events" SET "Title"=%s, "Type"=%s,"Date"=%s, "Address_ID"=%s WHERE "EventID"=%s', (title, type_, date, address_id, id))
                self.conn.commit()
            return b,strr
        else:
            return False, 'ERROR: wrong EventID'

    def update_phone(self, id, tourist_id, number):
        c = self.conn.cursor()
        if self.is_correct_phone_id(id):
            b, strr = self.phone_check(tourist_id, number)
            if b:
                c.execute('UPDATE "Phone_nums" SET "Tourist_ID"=%s, "Number"=%s WHERE "PhoneID"=%s', (tourist_id, number, id))
                self.conn.commit()
            return b, strr
        else:
            return False, 'ERROR: wrong PhoneID'

    def delete_p(self, id):
        c = self.conn.cursor()
        if self.is_correct_phone_id(id):
            c.execute('DELETE FROM "Phone_nums" WHERE "PhoneID"=%s', (id,))
            self.conn.commit()
            return True
        else:
            return False
    def cnt_t_fk(self,id):
        c = self.conn.cursor()
        c.execute('SELECT COUNT(*) FROM "Tourists/Events" WHERE "Tourist" = %s', (id,))
        t_e = c.fetchone()
        c.execute('SELECT COUNT(*) FROM "Phone_nums" WHERE "Tourist_ID" = %s', (id,))
        p = c.fetchone()
        if t_e[0] > 0 or p[0] > 0:
            return True, t_e[0], p[0]
        else:
            return False,t_e[0],p[0]
    def get_t_e(self, id):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Tourists/Events" WHERE "Tourist" = %s',  (id,))
        return c.fetchall()

    def get_p(self, id):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Phone_nums" WHERE "Tourist_ID" = %s',  (id,))
        return c.fetchall()
    def delete_t(self, id):
        c = self.conn.cursor()
        if self.is_correct_tourist_id(id):
            c.execute('DELETE FROM "Tourists" WHERE "TouristID"=%s', (id,))
            self.conn.commit()
            return True
        else:
            return False



    def cnt_o_fk(self,id):
        c = self.conn.cursor()
        c.execute('SELECT COUNT(*) FROM "Оrganizers/Events" WHERE "Оrganizer" = %s', (id,))
        o_e = c.fetchone()

        if o_e[0] > 0:
            return True, o_e[0]
        else:
            return False,o_e[0]
    def get_o_e(self, id):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Оrganizers/Events" WHERE "Оrganizer" = %s',  (id,))
        return c.fetchall()
    def delete_o(self,id):
        c = self.conn.cursor()
        if self.is_correct_organizer_id(id):
            c.execute('DELETE FROM "Оrganizers" WHERE "ОrganizerID"=%s', (id,))
            self.conn.commit()
            return True
        else:
            return False

    def cnt_e_fk(self,id):
        c = self.conn.cursor()
        c.execute('SELECT COUNT(*) FROM "Оrganizers/Events" WHERE "Event_o" = %s', (id,))
        e1 = c.fetchone()
        c.execute('SELECT COUNT(*) FROM "Tourists/Events" WHERE "Event_t" = %s', (id,))
        e2 = c.fetchone()
        if e1[0] > 0 or e2[0] > 0:
            return True, e1[0],e2[0]
        else:
            return False,e1[0],e2[0]

    def get_e1(self, id):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Оrganizers/Events" WHERE "Event_o" = %s',  (id,))
        return c.fetchall()

    def get_e2(self, id):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Tourists/Events" WHERE "Event_t" = %s',  (id,))
        return c.fetchall()

    def delete_e(self,id):
        c = self.conn.cursor()
        if self.is_correct_event_id(id):
            c.execute('DELETE FROM "Events" WHERE "EventID"=%s', (id,))
            self.conn.commit()
            return True
        else:
            return False

    def rand_event(self,n):
        c = self.conn.cursor()
        for i in range(n):
            c.execute('INSERT INTO "Events" ("Title", "Type", "Date", "Address_ID") VALUES ((select chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int)), (select chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int)), (select timestamp \'2023-01-10 20:00:00\' + random() * (timestamp \'2023-12-20 20:00:00\' - timestamp \'2023-01-10 10:00:00\')), (select "AddressID" from "Address" order by random() limit 1))')
            self.conn.commit()
    def cnt_events(self):
        c = self.conn.cursor()
        c.execute('SELECT COUNT(*) FROM "Events"')
        r = c.fetchone()
        return r[0]

    def call(self):
        c = self.conn.cursor()
        c.execute('select * from (select "Address_ID" as "AddressID", count (*) as cnt from "Events" where "Date" > Now() group by "Address_ID") as address_id inner join "Address"  on "Address"."AddressID" = address_id."AddressID"')
        return c.fetchall()
