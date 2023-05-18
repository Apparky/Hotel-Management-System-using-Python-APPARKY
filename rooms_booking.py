from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
import random
import datetime
from babel.numbers import *
from babel.dates import *


class RoomBooking:
    def __init__(self, root):
        self.rooms = root
        self.rooms.title("Room Details")
        self.rooms.geometry("1313x573+232+222")
        self.rooms.maxsize(1313, 573)
        self.rooms.minsize(1313, 573)

        ##################=================================================== Dababase Creation and connection ============================================

        ##### Customer Table #####

        mydb = sqlite3.connect("hotel_management_system.db")
        my_cursor = mydb.cursor()

        my_cursor.execute("""CREATE TABLE if not exists customer (
                            Customer_ID	INTEGER UNIQUE,
                            Customer_Name TEXT,
                            Sex	TEXT,
                            Address	TEXT,
                            Pin_Code	INTEGER,
                            Contact_No	INTEGER,
                            eMail	TEXT,
                            Nationality	TEXT,
                            ID_Type	TEXT,
                            ID_No INTEGER,
                            PRIMARY KEY('Customer_ID'))""")

        mydb.commit()
        mydb.close()

        mydb = sqlite3.connect("hotel_management_system.db")
        my_cursor = mydb.cursor()

        #### Room Table ####

        my_cursor.execute("""CREATE TABLE if not exists room_booking (
                                Booking_ID integer unique,
                                Customer_ID integer,
                                Name text,
                                Contact_No integer, 
                                Check_In text, 
                                Check_Out text, 
                                Room_Type text, 
                                Allotted_Room integer, 
                                Meal text, 
                                No_of_Days integer,
                                PRIMARY KEY ('Booking_ID'))""")

        mydb.commit()
        mydb.close()

        #### Room Type Table ####

        mydb = sqlite3.connect("hotel_management_system.db")
        my_cursor = mydb.cursor()

        my_cursor.execute("""CREATE TABLE if not exists room_types (
                                    Room_No integer unique, 
                                    Floor text, 
                                    Room_Type text, 
                                    Availability text, 
                                    Room_Cost integer, 
                                    Room_Status text, 
                                    PRIMARY KEY ('Room_No'))""")

        mydb.commit()
        mydb.close()

        #### Bill Table ####

        mydb = sqlite3.connect("hotel_management_system.db")
        my_cursor = mydb.cursor()

        my_cursor.execute("""CREATE TABLE if not exists bills (
                                        Bill_No integer unique,
                                        Name text, 
                                        Customer_ID integer, 
                                        Check_In text, 
                                        Check_Out text, 
                                        Room_Type text, 
                                        Allotted_Room integer, 
                                        Meal_Type text, 
                                        No_of_Days integer, 
                                        Sub_amount integer, 
                                        Tax_amount integer, 
                                        Total_cost integer,
                                        PRIMARY KEY ('Bill_No'))""")

        mydb.commit()
        mydb.close()

        #### Planer Table ####

        mydb = sqlite3.connect("hotel_management_system.db")
        my_cursor = mydb.cursor()

        my_cursor.execute("""CREATE TABLE if not exists planner (
                                Planner_ID text unique, 
                                Planer_type text, 
                                Single_cost integer, 
                                Double_cost integer, 
                                Luxury_cost integer, 
                                Delux_cost integer, 
                                Super_Delux_cost integer, 
                                Latest_Updated_as_date text, 
                                Latest_update_as_time text, 
                                PRIMARY KEY ('Planner_ID'))""")

        mydb.commit()
        mydb.close()

        accommodation = {
            "Break Fast": 800,
            "Lunch": 1200,
            "Dinner": 1500,
            "Tiffine": 500

        }

        room_type = {
            "Single": 1500,
            "Double": 2500,
            "Luxury": 4000,
            "Deluxe": 4500,
            "Super Deluxe": 6000
        }

        ##################=================================================== All Functions ============================================================

        def room_availability(event):
            room_type_list = list(room_type.keys())

            if self.Room_type_var.get() == room_type_list[0]:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    my_cursor.execute(f"""SELECT Room_No FROM room_types WHERE Room_Type = '{self.Room_type_var.get()}' AND Availability = 'Yes' AND Room_Status = 'OK'""")

                    data = my_cursor.fetchall()
                    mydb.commit()
                    mydb.close()

                    if len(data) > 0:
                        Allotted_room_label_combobox["values"] = ("")
                        Allotted_room_label_combobox.set("")
                        Allotted_room_label_combobox["values"] = data

                    else:
                        Allotted_room_label_combobox["values"] = ("")
                        Allotted_room_label_combobox.set("Not Available")

                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.rooms)

            elif self.Room_type_var.get() == room_type_list[1]:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    my_cursor.execute(f"""SELECT Room_No FROM room_types WHERE Room_Type = '{self.Room_type_var.get()}' AND Availability = 'Yes' AND Room_Status = 'OK'""")

                    data = my_cursor.fetchall()
                    mydb.commit()
                    mydb.close()

                    if len(data) > 0:
                        Allotted_room_label_combobox["values"] = ("")
                        Allotted_room_label_combobox.set("")
                        Allotted_room_label_combobox["values"] = data

                    else:
                        Allotted_room_label_combobox["values"] = ("")
                        Allotted_room_label_combobox.set("Not Available")

                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.rooms)

            elif self.Room_type_var.get() == room_type_list[2]:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    my_cursor.execute(f"""SELECT Room_No FROM room_types WHERE Room_Type = '{self.Room_type_var.get()}' AND Availability = 'Yes' AND Room_Status = 'OK'""")

                    data = my_cursor.fetchall()
                    mydb.commit()
                    mydb.close()

                    if len(data) > 0:
                        Allotted_room_label_combobox["values"] = ("")
                        Allotted_room_label_combobox.set("")
                        Allotted_room_label_combobox["values"] = data

                    else:
                        Allotted_room_label_combobox["values"] = ("")
                        Allotted_room_label_combobox.set("Not Available")

                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.rooms)

            elif self.Room_type_var.get() == room_type_list[3]:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    my_cursor.execute(f"""SELECT Room_No FROM room_types WHERE Room_Type = '{self.Room_type_var.get()}' AND Availability = 'Yes' AND Room_Status = 'OK'""")

                    data = my_cursor.fetchall()
                    mydb.commit()
                    mydb.close()

                    if len(data) > 0:
                        Allotted_room_label_combobox["values"] = ("")
                        Allotted_room_label_combobox.set("")
                        Allotted_room_label_combobox["values"] = data

                    else:
                        Allotted_room_label_combobox["values"] = ("")
                        Allotted_room_label_combobox.set("Not Available")

                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.rooms)

            elif self.Room_type_var.get() == room_type_list[4]:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    my_cursor.execute(f"""SELECT Room_No FROM room_types WHERE Room_Type = '{self.Room_type_var.get()}' AND Availability = 'Yes' AND Room_Status = 'OK'""")

                    data = my_cursor.fetchall()
                    mydb.commit()
                    mydb.close()

                    if len(data) > 0:
                        Allotted_room_label_combobox["values"] = ("")
                        Allotted_room_label_combobox.set("")
                        Allotted_room_label_combobox["values"] = data

                    else:
                        Allotted_room_label_combobox["values"] = ("")
                        Allotted_room_label_combobox.set("Not Available")

                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.rooms)

        def fetch_contact():
            if self.Customer_Contact_No_var.get() == "" or self.Customer_Contact_No_var.get() == 0:
                messagebox.showerror("Error", "Contact entry is Empty! Please fill the Contact Details", parent=self.rooms)
                Customer_Contact_No_label_entry.delete(0, END)

            else:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    my_cursor.execute(f"SELECT Customer_ID, * FROM customer WHERE Contact_No = {self.Customer_Contact_No_var.get()}")

                    data = my_cursor.fetchall()

                    mydb.commit()
                    mydb.close()

                    if data==None:
                        messagebox.showinfo("Empty", "No data found", parent=self.rooms)

                    else:
                        try:
                            mydb = sqlite3.connect("hotel_management_system.db")
                            my_cursor = mydb.cursor()

                            my_cursor.execute(f"SELECT Customer_Name FROM customer WHERE Contact_No = {self.Customer_Contact_No_var.get()}")
                            val = my_cursor.fetchone()
                            self.customer_name_var.set(val[0])

                            my_cursor.execute(f"SELECT Customer_ID FROM customer WHERE Contact_No = {self.Customer_Contact_No_var.get()}")
                            val = my_cursor.fetchone()
                            self.customer_id_no_var.set(val[0])

                            my_cursor.execute(f"SELECT Sex FROM customer WHERE Contact_No = {self.Customer_Contact_No_var.get()}")
                            val = my_cursor.fetchone()
                            self.sex_type_var.set(val[0])

                            my_cursor.execute(f"SELECT eMail FROM customer WHERE Contact_No = {self.Customer_Contact_No_var.get()}")
                            val = my_cursor.fetchone()
                            self.email_id_var.set(val[0])

                            my_cursor.execute(f"SELECT Nationality FROM customer WHERE Contact_No = {self.Customer_Contact_No_var.get()}")
                            val = my_cursor.fetchone()
                            self.nationality_type_var.set(val[0])

                            my_cursor.execute(f"SELECT ID_Type FROM customer WHERE Contact_No = {self.Customer_Contact_No_var.get()}")
                            val = my_cursor.fetchone()
                            self.id_type_var.set(val[0])

                            my_cursor.execute(f"SELECT Pin_Code FROM customer WHERE Contact_No = {self.Customer_Contact_No_var.get()}")
                            val = my_cursor.fetchone()
                            self.pin_code_var.set(val[0])

                        except Exception as e:
                            messagebox.showerror("Error", f"Something went Wrong!!! {str(e)}")

                    mydb.commit()
                    mydb.close()
                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong!!! {str(e)}", parent=self.rooms)

        def clear_function():
            self.customer_name_var.set("")
            self.customer_id_no_var.set("")
            self.sex_type_var.set("")
            self.email_id_var.set("")
            self.nationality_type_var.set("")
            self.id_type_var.set("")
            self.pin_code_var.set("")

        def add_data():
            mydb = sqlite3.connect("hotel_management_system.db")
            my_cursor = mydb.cursor()
            if self.Customer_Contact_No_var.get() == "" or self.Customer_Contact_No_var.get() == 0:
                messagebox.showerror("Error", "Contact entry is Empty! Please fill the Contact Details", parent=self.rooms)
                Customer_Contact_No_label_entry.delete(0, END)

            else:
                try:
                    my_cursor.execute(f"SELECT Customer_Name FROM customer WHERE Contact_No = {self.Customer_Contact_No_var.get()}")
                    val = my_cursor.fetchone()
                    self.customer_name_var.set(val[0])
                    mydb.commit()
                    mydb.close()

                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    """
                    self.Customer_Contact_No_var = IntVar()
                    self.Customer_Check_In_var = StringVar()
                    self.Customer_Check_Out_var = StringVar()
                    self.Room_type_var = StringVar()
                    self.Available_room_var = IntVar()
                    self.Meal_type_var = StringVar()
                    self.No_of_day_var = IntVar()
                    self.Tax_var = IntVar()
                    self.Sub_total_var = IntVar()
                    self.Total_var = IntVar()
                    """

                    my_cursor.execute(
                        "INSERT INTO room_booking VALUES (:booking_id, :cust_id, :name, :contact_no, :check_in, :check_out, :room_type, :allotted_room, :meal, :no_of_days)",
                        {
                            'booking_id': self.Customer_Booking_ID_var.get(),
                            'cust_id': self.customer_id_no_var.get(),
                            'name': self.customer_name_var.get(),
                            'contact_no': self.Customer_Contact_No_var.get(),
                            'check_in': self.Customer_Check_In_var.get(),
                            'check_out': self.Customer_Check_Out_var.get(),
                            'room_type': self.Room_type_var.get(),
                            'allotted_room': self.Allotted_room_var.get(),
                            'meal': self.Plan_type_var.get(),
                            'no_of_days': self.No_of_day_var.get(),
                        })
                    mydb.commit()
                    mydb.close()
                    messagebox.showinfo("Successful", "Data has been added Successfully!", parent=self.rooms)
                    booked_room_no()
                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong!! {str(e)}", parent=self.rooms)
                fetch_tree()

        def update_data():
            if self.Customer_Contact_No_var.get() == "" or self.Customer_Contact_No_var.get() == 0:
                messagebox.showerror("Error", "Please enter Valid Contact No.", parent=self.rooms)

            elif self.Customer_Check_In_var.get() == "" or self.Customer_Check_In_var.get() == 0:
                messagebox.showerror("Error", "Please enter Valid Check In Date", parent=self.rooms)

            elif self.Customer_Check_Out_var.get() == "" or self.Customer_Check_Out_var.get() == 0:
                messagebox.showerror("Error", "Please enter Valid Check Out Date", parent=self.rooms)

            elif self.Room_type_var.get() == "" or self.Room_type_var.get() == 0:
                messagebox.showerror("Error", "Please enter Valid Room Type", parent=self.rooms)

            elif self.Allotted_room_var.get() == "" or self.Allotted_room_var.get() == 0:
                messagebox.showerror("Error", "Please enter Valid Allotted Rooms", parent=self.rooms)

            elif self.Plan_type_var.get() == "" or self.Plan_type_var.get() == 0:
                messagebox.showerror("Error", "Please enter Valid Meal Types", parent=self.rooms)

            elif self.No_of_day_var.get() == "" or self.No_of_day_var.get() == 0:
                messagebox.showerror("Error", "Please enter Valid Number of Days", parent=self.rooms)

            elif self.customer_name_var.get() == "" or self.customer_id_no_var.get() == "":
                messagebox.showerror("Error", "Name & Ref No. is not fetched! Please Fetch Name and Ref No.", parent=self.rooms)

            else:
                querry = messagebox.askyesno("Are You Sure?", "Are You sure! You want to update this data?", parent=self.rooms)
                if querry == 1:
                    try:
                        mydb = sqlite3.connect("hotel_management_system.db")
                        my_cursor = mydb.cursor()

                        my_cursor.execute("""UPDATE room_booking SET
                                            Customer_ID = :cust_id,
                                            Name = :name,
                                            Contact_No = :contact,
                                            Check_In = :check_in,
                                            Check_Out = :check_out,
                                            Room_Type = :room_type,
                                            Allotted_Room = :allotted,
                                            Meal = :meal,
                                            No_of_Days = :no_of_d
                                            
                                            WHERE Booking_ID = :oid""",
                                          {
                                              'cust_id': self.customer_id_no_var.get(),
                                              'name': self.customer_name_var.get(),
                                              'contact': self.Customer_Contact_No_var.get(),
                                              'check_in': self.Customer_Check_In_var.get(),
                                              'check_out': self.Customer_Check_Out_var.get(),
                                              'room_type': self.Room_type_var.get(),
                                              'allotted': self.Allotted_room_var.get(),
                                              'meal': self.Plan_type_var.get(),
                                              'no_of_d': self.No_of_day_var.get(),
                                              'oid': self.Customer_Booking_ID_var.get()
                                          })
                        mydb.commit()
                        mydb.close()
                        fetch_tree()
                        messagebox.showinfo("Successful", "Data has been updated Successfully!!", parent=self.rooms)
                        booked_room_no()

                    except Exception as e:
                        messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.rooms)

                else:
                    pass

            fetch_tree()

        def delete_data():
            query = messagebox.askyesno("Are you sure", "Are You Sure!! You want to Delete this Data?", parent=self.rooms)
            if query == 1:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    my_cursor.execute(f"DELETE FROM room_booking WHERE Booking_ID = {self.Customer_Booking_ID_var.get()}")

                    mydb.commit()
                    mydb.close()
                    fetch_tree()

                    messagebox.showinfo("Deleted", "Your data has been Deleted!!", parent=self.rooms)

                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.rooms)

            else:
                pass

        def reset_button():
            x = random.randint(10000, 90000)
            self.Customer_Booking_ID_var.set(x)
            self.Customer_Contact_No_var.set(0)
            self.Customer_Check_In_var.set("")
            self.Customer_Check_Out_var.set("")
            self.Room_type_var.set("")
            self.Allotted_room_var.set(0)
            self.Plan_type_var.set("")
            self.No_of_day_var.set(0)
            self.Tax_var.set(0)
            self.Sub_total_var.set(0)
            self.Total_var.set(0)

            self.customer_name_var.set("")
            self.customer_id_no_var.set("")
            self.sex_type_var.set("")
            self.email_id_var.set("")
            self.nationality_type_var.set("")
            self.id_type_var.set("")
            self.pin_code_var.set("")

            fetch_tree()

        def create_bill():
            try:
                check_in = self.Customer_Check_In_var.get()
                check_out = self.Customer_Check_Out_var.get()
                check_in = datetime.datetime.strptime(check_in, "%d/%m/%Y")
                check_out = datetime.datetime.strptime(check_out, "%d/%m/%Y")
                self.No_of_day_var.set(abs(check_out - check_in).days)

                accommodation_list = list(accommodation.keys())
                room_type_list = list(room_type.keys())

                for i in accommodation_list:
                    for j in room_type_list:
                        if self.Room_type_var.get() == j and self.Plan_type_var.get() == i:
                            single_day_fare = float(accommodation[self.Plan_type_var.get()] + room_type[self.Room_type_var.get()])
                            total_fare = float(single_day_fare * float(self.No_of_day_var.get()))

                            tax_fare = total_fare * 0.1
                            sub_total = total_fare
                            total_payment = float(tax_fare + sub_total)

                            self.Sub_total_var.set(int(sub_total))
                            self.Tax_var.set(int(tax_fare))
                            self.Total_var.set(int(total_payment))

                bill = messagebox.askyesno("Bill", "Bill has been Generated. Do you ant to save the bill?", parent=self.rooms)
                if bill == 1:
                    generate_bill_data()

                else:
                    pass

            except Exception as e:
                messagebox.showerror("Error", "Something Went Wrong...! Please Check Your Entries...!", parent=self.rooms)

        def generate_bill_data():
            try:
                start = 19
                stop = 29
                data = ""
                for i in range(3):
                    val = random.randint(start, stop)
                    data = data + str(val)

                bill_id = int(data)
                mydb = sqlite3.connect("hotel_management_system.db")
                my_cursor = mydb.cursor()

                my_cursor.execute("INSERT INTO bills VALUES (:bill_no, :name, :cust_id, :check_in, :check_out, :room_type, :allotted_room, :meal_type, :no_of_days, :sub_amount, :tax_amount, :total_amount)",
                                  {
                                      'bill_no': bill_id,
                                      'name': self.customer_name_var.get(),
                                      'cust_id': self.customer_id_no_var.get(),
                                      'check_in': self.Customer_Check_In_var.get(),
                                      'check_out': self.Customer_Check_Out_var.get(),
                                      'room_type': self.Room_type_var.get(),
                                      'allotted_room': self.Allotted_room_var.get(),
                                      'meal_type': self.Plan_type_var.get(),
                                      'no_of_days': self.No_of_day_var.get(),
                                      'sub_amount': self.Sub_total_var.get(),
                                      'tax_amount': self.Tax_var.get(),
                                      'total_amount': self.Total_var.get()
                                  })

                mydb.commit()
                mydb.close()
                messagebox.showinfo("Bill", "Bill has been Generated. Data has been saved to your DateBase.", parent=self.rooms)

            except Exception as e:
                messagebox.showerror("Error", f"Something went Wrong{str(e)}", parent=self.rooms)

        def fetch_tree():
            mydb = sqlite3.connect("hotel_management_system.db")
            my_cursor = mydb.cursor()

            my_cursor.execute("SELECT * FROM room_booking")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.Room_details_table.delete(*self.Room_details_table.get_children())
                for i in data:
                    self.Room_details_table.insert("", END, value=i)
                mydb.commit()
            mydb.close()

        def get_tree_data(event):
            try:
                cursor_row = self.Room_details_table.focus()
                content = self.Room_details_table.item(cursor_row)
                content_value = content["values"]

                self.Customer_Booking_ID_var.set(int(content_value[0])),
                self.customer_id_no_var.set(content_value[1]),
                self.customer_name_var.set(content_value[2]),
                self.Customer_Contact_No_var.set(int(content_value[3])),
                self.Customer_Check_In_var.set(content_value[4]),
                self.Customer_Check_Out_var.set(content_value[5]),
                self.Room_type_var.set(content_value[6]),
                self.Allotted_room_var.set(int(content_value[7])),
                self.Plan_type_var.set(content_value[8]),
                self.No_of_day_var.set(int(content_value[9]))

                fetch_contact()

                self.Sub_total_var.set(0)
                self.Tax_var.set(0)
                self.Total_var.set(0)

            except:
                pass

        def search_attribute(event):
            if self.search_by_table_var.get() == "Name":
                Search_by_attribute_combobox["values"] = ("")
                Search_by_attribute_combobox.set("")
                Search_by_attribute_combobox.config(state=NORMAL)

            elif self.search_by_table_var.get() == "Check In":
                Search_by_attribute_combobox["values"] = ("")
                Search_by_attribute_combobox.set("")
                Search_by_attribute_combobox.config(state=NORMAL)

            elif self.search_by_table_var.get() == "Check Out":
                Search_by_attribute_combobox["values"] = ("")
                Search_by_attribute_combobox.set("")
                Search_by_attribute_combobox.config(state=NORMAL)

            elif self.search_by_table_var.get() == "Room Type":
                Search_by_attribute_combobox["values"] = list(room_type.keys())
                Search_by_attribute_combobox.set("")
                Search_by_attribute_combobox.config(state="readonly")

            elif self.search_by_table_var.get() == "Allotted Room":
                Search_by_attribute_combobox["values"] = ("")
                Search_by_attribute_combobox.set("")
                Search_by_attribute_combobox.config(state=NORMAL)

            elif self.search_by_table_var.get() == "Meal":
                Search_by_attribute_combobox["values"] = list(accommodation.keys())
                Search_by_attribute_combobox.set("")
                Search_by_attribute_combobox.config(state="readonly")

            else:
                pass

        def search():
            mydb = sqlite3.connect("hotel_management_system.db")
            my_cursor = mydb.cursor()

            if Search_by_table_name_combobox.get() == "" or Search_by_attribute_combobox.get() == "":
                messagebox.showerror("Error", "Invalid Entry!! Please check your Values", parent=self.rooms)

            else:
                try:
                    if self.search_by_table_var.get() == "Name":
                        my_cursor.execute(
                            f"SELECT * FROM room_booking WHERE {self.search_by_table_var.get()} = '{self.search_by_attribute_var.get()}'")
                        data = my_cursor.fetchall()
                        if len(data) >= 1:
                            self.Room_details_table.delete(*self.Room_details_table.get_children())
                            for i in data:
                                self.Room_details_table.insert("", END, values=i)

                        else:
                            self.Room_details_table.delete(*self.Room_details_table.get_children())
                            mydb.commit()
                        mydb.close()

                    elif self.search_by_table_var.get() == "Check In":
                        my_cursor.execute(
                            f"SELECT * FROM room_booking WHERE Check_In = '{self.search_by_attribute_var.get()}'")
                        data = my_cursor.fetchall()
                        if len(data) >= 1:
                            self.Room_details_table.delete(*self.Room_details_table.get_children())
                            for i in data:
                                self.Room_details_table.insert("", END, values=i)

                        else:
                            self.Room_details_table.delete(*self.Room_details_table.get_children())
                            mydb.commit()
                        mydb.close()

                    elif self.search_by_table_var.get() == "Check Out":
                        my_cursor.execute(
                            f"SELECT * FROM room_booking WHERE Check_Out = '{self.search_by_attribute_var.get()}'")
                        data = my_cursor.fetchall()
                        if len(data) >= 1:
                            self.Room_details_table.delete(*self.Room_details_table.get_children())
                            for i in data:
                                self.Room_details_table.insert("", END, values=i)

                        else:
                            self.Room_details_table.delete(*self.Room_details_table.get_children())
                            mydb.commit()
                        mydb.close()

                    elif self.search_by_table_var.get() == "Room Type":
                        my_cursor.execute(
                            f"SELECT * FROM room_booking WHERE Room_Type = '{self.search_by_attribute_var.get()}'")
                        data = my_cursor.fetchall()
                        if len(data) >= 1:
                            self.Room_details_table.delete(*self.Room_details_table.get_children())
                            for i in data:
                                self.Room_details_table.insert("", END, values=i)

                        else:
                            self.Room_details_table.delete(*self.Room_details_table.get_children())
                            mydb.commit()
                        mydb.close()

                    elif self.search_by_table_var.get() == "Allotted Room":
                        my_cursor.execute(
                            f"SELECT * FROM room_booking WHERE Allotted_Room = {self.search_by_attribute_var.get()}")
                        data = my_cursor.fetchall()
                        if len(data) >= 1:
                            self.Room_details_table.delete(*self.Room_details_table.get_children())
                            for i in data:
                                self.Room_details_table.insert("", END, values=i)

                        else:
                            self.Room_details_table.delete(*self.Room_details_table.get_children())
                            mydb.commit()
                        mydb.close()

                    elif self.search_by_table_var.get() == "Meal":
                        my_cursor.execute(
                            f"SELECT * FROM room_booking WHERE {self.search_by_table_var.get()} = '{self.search_by_attribute_var.get()}'")
                        data = my_cursor.fetchall()
                        if len(data) >= 1:
                            self.Room_details_table.delete(*self.Room_details_table.get_children())
                            for i in data:
                                self.Room_details_table.insert("", END, values=i)

                        else:
                            self.Room_details_table.delete(*self.Room_details_table.get_children())
                            mydb.commit()
                        mydb.close()

                    else:
                        pass

                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.rooms)

        def show_all():
            fetch_tree()
            self.search_by_table_var.set("")
            self.search_by_attribute_var.set("")
            Search_by_attribute_combobox["values"] = ("")
            Search_by_attribute_combobox.config(state=NORMAL)

        def booked_room_no():
            day_counter = check_day(self.Customer_Check_Out_var.get())
            if day_counter == 1:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    my_cursor.execute(f"""UPDATE room_types SET Availability = 'No' WHERE Room_No = {self.Allotted_room_var.get()}""")

                    mydb.commit()
                    mydb.close()
                except Exception as e:
                    messagebox.showerror("Error", f"Something Went Wrong {str(e)}", parent=self.rooms)
            else:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()
                    my_cursor.execute(f"""UPDATE room_types SET Availability = 'Yes' WHERE Room_No = {self.Allotted_room_var.get()}""")
                    mydb.commit()
                    mydb.close()
                except Exception as e:
                    messagebox.showerror("Error", f"Something Went Wrong {str(e)}", parent=self.rooms)

        def check_day(data):
            _today = datetime.datetime.now()
            _today = str(_today.date())
            _today = datetime.datetime.strptime(_today, "%Y-%m-%d")

            data = datetime.datetime.strptime(data, "%d/%m/%Y")

            if data > _today:
                return 1
            else:
                return 0

        ##################=================================================== Title Section ============================================================

        title_label = Label(self.rooms, text="Room Booking Details", font=("Calibre", 20, "bold"), background="black", foreground="gold", border=1, relief=RIDGE)
        title_label.place(x=0, y=0, width=1313, height=50)

        image_logo = Image.open(r"Images\logohotel.png")
        image_logo = image_logo.resize((100, 45), Image.ANTIALIAS)
        self.image_logo = ImageTk.PhotoImage(image_logo)

        image_logo_label = Label(self.rooms, image=self.image_logo, border=0, relief=RIDGE)
        image_logo_label.place(x=2, y=2, width=100, height=45)

        exit_button = Button(self.rooms, text="Exit", font=("Calibre", 20, "bold"), background="black", foreground="red", border=0, relief=RIDGE, cursor="hand2", command=self.rooms.destroy)
        exit_button.place(x=1240, y=5, width=70, height=40)

        ###################=============================================== All Variables ===========================================================

        self.Customer_Booking_ID_var = IntVar()
        x = random.randint(10000, 90000)
        self.Customer_Booking_ID_var.set(x)
        self.Customer_Contact_No_var = IntVar()
        self.Customer_Check_In_var = StringVar()
        self.Customer_Check_Out_var = StringVar()
        self.Room_type_var = StringVar()
        self.Allotted_room_var = IntVar()
        self.Plan_type_var = StringVar()
        self.No_of_day_var = IntVar()
        self.Tax_var = IntVar()
        self.Sub_total_var = IntVar()
        self.Total_var = IntVar()


        ###################=============================================== Label Frame =============================================================

        Room_Details_label_frame = LabelFrame(self.rooms, text="Room Booking Details", border=2, relief=RIDGE, padx=2, font=("Calibre", 10))
        Room_Details_label_frame.place(x=5, y=50, width=425, height=510)

        mydb = sqlite3.connect("hotel_management_system.db")
        my_cursor = mydb.cursor()
        my_cursor.execute("""SELECT Planer_type FROM planner""")
        data = my_cursor.fetchall()
        mydb.commit()
        mydb.close()

        Customer_booking_id_label = Label(Room_Details_label_frame, text="Booking ID", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Customer_booking_id_label.grid(row=0, column=0, sticky=W)
        Customer_booking_id_label_entry = ttk.Entry(Room_Details_label_frame, width=30, font=("arial", 12), textvariable=self.Customer_Booking_ID_var, state="readonly")
        Customer_booking_id_label_entry.grid(row=0, column=1, sticky=W, padx=4)

        Customer_Contact_No_label = Label(Room_Details_label_frame, text="Contact No.", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Customer_Contact_No_label.grid(row=1, column=0, sticky=W)
        Customer_Contact_No_label_entry = ttk.Entry(Room_Details_label_frame, width=20, font=("arial", 12), textvariable=self.Customer_Contact_No_var)
        Customer_Contact_No_label_entry.grid(row=1, column=1, sticky=W, padx=4)
        Fetch_data_button = Button(Room_Details_label_frame, text="Fetch Data", font=("Calibre", 12, "bold"), foreground="gold", command=fetch_contact, background="black", width=8, cursor="hand2", border=0)
        Fetch_data_button.place(x=325, y=47, height=25)

        Customer_Check_in_date_label = Label(Room_Details_label_frame, text="Check In", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Customer_Check_in_date_label.grid(row=2, column=0, sticky=W)
        Customer_Check_in_date_label_entry = ttk.Entry(Room_Details_label_frame, width=30, font=("arial", 12), textvariable=self.Customer_Check_In_var)
        Customer_Check_in_date_label_entry.grid(row=2, column=1, sticky=E, padx=4)

        Customer_Check_out_date_label = Label(Room_Details_label_frame, text="Check Out", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Customer_Check_out_date_label.grid(row=3, column=0, sticky=W)
        Customer_Check_out_date_label_entry = ttk.Entry(Room_Details_label_frame, width=30, font=("arial", 12), textvariable=self.Customer_Check_Out_var)
        Customer_Check_out_date_label_entry.grid(row=3, column=1, sticky=E, padx=4)

        Room_type_label = Label(Room_Details_label_frame, text="Room Type", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Room_type_label.grid(row=4, column=0, sticky=W)
        Room_type_label_combobox = ttk.Combobox(Room_Details_label_frame, width=28, font=("arial", 12), textvariable=self.Room_type_var, state="readonly")
        Room_type_label_combobox["values"] = list(room_type.keys())
        Room_type_label_combobox.bind("<<ComboboxSelected>>", room_availability)
        Room_type_label_combobox.set("")
        Room_type_label_combobox.grid(row=4, column=1, sticky=E, padx=4)

        Allotted_room_label = Label(Room_Details_label_frame, text="Allotted Room", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Allotted_room_label.grid(row=5, column=0, sticky=W)
        Allotted_room_label_combobox = ttk.Combobox(Room_Details_label_frame, width=28, font=("arial", 12), textvariable=self.Allotted_room_var, state="readonly")
        Allotted_room_label_combobox["values"] = ("")
        Allotted_room_label_combobox.set("")
        Allotted_room_label_combobox.grid(row=5, column=1, sticky=E, padx=4)

        Plan_type_label = Label(Room_Details_label_frame, text="Plan", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Plan_type_label.grid(row=6, column=0, sticky=W)
        Plan_type_label_combobox = ttk.Combobox(Room_Details_label_frame, width=28, font=("arial", 12), textvariable=self.Plan_type_var, state="readonly")
        Plan_type_label_combobox["values"] = data
        Plan_type_label_combobox.grid(row=6, column=1, sticky=E, padx=4)

        No_of_days_label = Label(Room_Details_label_frame, text="No of Days", font=("Calibre", 12, "bold"), padx=4, pady=8)
        No_of_days_label.grid(row=7, column=0, sticky=W)
        No_of_days_label_entry = ttk.Entry(Room_Details_label_frame, width=30, font=("arial", 12), textvariable=self.No_of_day_var)
        No_of_days_label_entry.grid(row=7, column=1, sticky=E, padx=4)

        Payment_sub_total_label = Label(Room_Details_label_frame, text="Sub Total", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Payment_sub_total_label.grid(row=8, column=0, sticky=W)
        Payment_sub_total_label_entry = ttk.Entry(Room_Details_label_frame, width=30, font=("arial", 12), textvariable=self.Sub_total_var)
        Payment_sub_total_label_entry.grid(row=8, column=1, sticky=E, padx=4)

        Payed_tax_label = Label(Room_Details_label_frame, text="Payed Tax", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Payed_tax_label.grid(row=9, column=0, sticky=W)
        Payed_tax_label_entry = ttk.Entry(Room_Details_label_frame, width=30, font=("arial", 12), textvariable=self.Tax_var)
        Payed_tax_label_entry.grid(row=9, column=1, sticky=E, padx=4)

        Payment_total_label = Label(Room_Details_label_frame, text="Total Cost", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Payment_total_label.grid(row=10, column=0, sticky=W)
        Payment_total_label_entry = ttk.Entry(Room_Details_label_frame, width=30, font=("arial", 12), textvariable=self.Total_var)
        Payment_total_label_entry.grid(row=10, column=1, sticky=E, padx=4)

        ############======================================================= Buttons =========================================================================

        Button_Frame = Frame(Room_Details_label_frame, border=2, relief=RIDGE)
        Button_Frame.place(x=1, y=445, width=414, height=40)

        Add_Button = Button(Button_Frame, text="Add", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=7, cursor="hand2", command=add_data)
        Add_Button.grid(row=0, column=0, padx=1, pady=2)

        Update_Button = Button(Button_Frame, text="Update", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=9, cursor="hand2", command=update_data)
        Update_Button.grid(row=0, column=1, padx=1, pady=2)

        Delete_Button = Button(Button_Frame, text="Delete", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=8, cursor="hand2", command=delete_data)
        Delete_Button.grid(row=0, column=2, padx=1, pady=2)

        Reset_button = Button(Button_Frame, text="Reset", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=8, cursor="hand2", command=reset_button)
        Reset_button.grid(row=0, column=3, padx=1, pady=2)

        bill_button = Button(Button_Frame, text="Bill", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=7, cursor="hand2", command=create_bill)
        bill_button.grid(row=0, column=4, padx=1, pady=2)


        ########================================================================ Data Frame to Show Selected Data =================================================================

        show_data_label_frame = LabelFrame(self.rooms, text="Customer Data", font=("Calibre", 10))
        show_data_label_frame.place(x=442, y=50, width=310, height=220)

        self.customer_name_var = StringVar()
        self.customer_id_no_var = StringVar()
        self.sex_type_var = StringVar()
        self.email_id_var = StringVar()
        self.nationality_type_var = StringVar()
        self.id_type_var = StringVar()
        self.pin_code_var = StringVar()

        name_label = Label(show_data_label_frame, text="Name: ", font=("Calibre", 12))
        name_label.place(x=1, y=1)
        name_from_db = Label(show_data_label_frame, textvariable=self.customer_name_var, font=("Calibre", 9))
        name_from_db.place(x=100, y=1)

        customer_id_label = Label(show_data_label_frame, text="Customer ID:", font=("Calibre", 12))
        customer_id_label.place(x=1, y=26)
        customer_id_from_db = Label(show_data_label_frame, textvariable=self.customer_id_no_var, font=("Calibre", 9))
        customer_id_from_db.place(x=100, y=26)

        sex_label = Label(show_data_label_frame, text="Sex: ", font=("Calibre", 12))
        sex_label.place(x=1, y=51)
        sex_from_db = Label(show_data_label_frame, textvariable=self.sex_type_var, font=("Calibre", 9))
        sex_from_db.place(x=100, y=51)

        email_label = Label(show_data_label_frame, text="Email: ", font=("Calibre", 12))
        email_label.place(x=1, y=76)
        email_from_db = Label(show_data_label_frame, textvariable=self.email_id_var, font=("Calibre", 9))
        email_from_db.place(x=100, y=76)

        nationality_label = Label(show_data_label_frame, text="Nationality: ", font=("Calibre", 12))
        nationality_label.place(x=1, y=101)
        nationality_from_db = Label(show_data_label_frame, textvariable=self.nationality_type_var, font=("Calibre", 9))
        nationality_from_db.place(x=100, y=101)

        id_proof_label = Label(show_data_label_frame, text="ID Proof: ", font=("Calibre", 12))
        id_proof_label.place(x=1, y=126)
        id_proof_from_db = Label(show_data_label_frame, textvariable=self.id_type_var, font=("Calibre", 9))
        id_proof_from_db.place(x=100, y=126)

        pin_label = Label(show_data_label_frame, text="Pin: ", font=("Caliber", 12))
        pin_label.place(x=1, y=151)
        pin_from_db = Label(show_data_label_frame, textvariable=self.pin_code_var, font=("Calibre", 9))
        pin_from_db.place(x=100, y=151)

        clear_button = Button(show_data_label_frame, text="Clear", border=0, foreground="red", cursor="hand2", command=clear_function)
        clear_button.pack(side=BOTTOM, anchor=SE)


        ########================================================================ Right Side Image =============================================================

        bed_image = Image.open(r"Images\bed.png")
        bed_image = bed_image.resize((545, 235), Image.ANTIALIAS)
        self.bed_photo_image = ImageTk.PhotoImage(bed_image)

        bed_image_Label = Label(self.rooms, image=self.bed_photo_image, borderwidth=0, relief=RIDGE)
        bed_image_Label.place(x=760, y=55, width=545, height=235)


        ############============================================================ Right Frame ===================================================================

        self.search_by_table_var = StringVar()
        self.search_by_attribute_var = StringVar()

        Details_and_search_system_frame = LabelFrame(self.rooms, border=2, relief=RIDGE, text="Details and Search System", font=("Calibre", 10))
        Details_and_search_system_frame.place(x=440, y=270, width=865, height=290)

        Search_by_label = Label(Details_and_search_system_frame, font=("Calibre", 12, "bold"), text="Search By", background="red", foreground="white")
        Search_by_label.grid(row=0, column=0, sticky=W, padx=5)

        Search_by_table_name_combobox = ttk.Combobox(Details_and_search_system_frame, font=("Calibre", 12), width=20, state="readonly", textvariable=self.search_by_table_var)
        Search_by_table_name_combobox["values"] = ("Name", "Check In", "Check Out", "Room Type", "Allotted Room", "Meal")
        Search_by_table_name_combobox.set("")
        Search_by_table_name_combobox.bind("<<ComboboxSelected>>", search_attribute)
        Search_by_table_name_combobox.grid(row=0, column=1, padx=2)

        Search_by_attribute_combobox = ttk.Combobox(Details_and_search_system_frame, font=("Calibre", 12), width=20, textvariable=self.search_by_attribute_var)
        Search_by_attribute_combobox["values"] = ("")
        Search_by_attribute_combobox.set("")
        Search_by_attribute_combobox.grid(row=0, column=2, padx=2)

        Search_button = Button(Details_and_search_system_frame, text="Search", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, cursor="hand2", command=search)
        Search_button.grid(row=0, column=3, padx=10)

        ShowAll_button = Button(Details_and_search_system_frame, text="Show All", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, cursor="hand2", command=show_all)
        ShowAll_button.grid(row=0, column=4)

        refresh_button = Button(Details_and_search_system_frame, text="Refresh", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, cursor="hand2")
        refresh_button.grid(row=0, column=5, padx=10)

        ######========================================================== Show Data Table ========================================================================

        Date_table_frame = Frame(Details_and_search_system_frame, border=2, relief=RIDGE)
        Date_table_frame.place(x=0, y=40, width=860, height=230)

        scroll_bar_x = ttk.Scrollbar(Date_table_frame, orient=HORIZONTAL)
        scroll_bar_y = ttk.Scrollbar(Date_table_frame, orient=VERTICAL)

        self.Room_details_table = ttk.Treeview(Date_table_frame, columns=("booking_id", "customer_id", "name", "contact", "checkin", "checkout", "room type", "allotted room", "meal", "no of days"), xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

        scroll_bar_x.config(command=self.Room_details_table.xview)
        scroll_bar_y.config(command=self.Room_details_table.yview)

        self.Room_details_table.heading("booking_id", text="Booking ID", anchor=CENTER)
        self.Room_details_table.heading("customer_id", text="Customer ID", anchor=CENTER)
        self.Room_details_table.heading("name", text="Name", anchor=CENTER)
        self.Room_details_table.heading("contact", text="Contact No.", anchor=CENTER)
        self.Room_details_table.heading("checkin", text="Check In", anchor=CENTER)
        self.Room_details_table.heading("checkout", text="Check Out", anchor=CENTER)
        self.Room_details_table.heading("room type", text="Room Type", anchor=CENTER)
        self.Room_details_table.heading("allotted room", text="Allotted Room", anchor=CENTER)
        self.Room_details_table.heading("meal", text="Meal", anchor=CENTER)
        self.Room_details_table.heading("no of days", text="No of Days", anchor=CENTER)

        self.Room_details_table["show"] = "headings"

        self.Room_details_table.column("booking_id", width=100, anchor=CENTER)
        self.Room_details_table.column("customer_id", width=100, anchor=CENTER)
        self.Room_details_table.column("name", width=120, anchor=CENTER)
        self.Room_details_table.column("contact", width=80, anchor=CENTER)
        self.Room_details_table.column("checkin", width=80, anchor=CENTER)
        self.Room_details_table.column("checkout", width=80, anchor=CENTER)
        self.Room_details_table.column("room type", width=80, anchor=CENTER)
        self.Room_details_table.column("allotted room", width=100, anchor=CENTER)
        self.Room_details_table.column("meal", width=150, anchor=CENTER)
        self.Room_details_table.column("no of days", width=80, anchor=CENTER)

        self.Room_details_table.pack(fill=BOTH, expand=1)
        self.Room_details_table.bind("<ButtonRelease-1>", get_tree_data)
        fetch_tree()


if __name__ == '__main__':
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()
