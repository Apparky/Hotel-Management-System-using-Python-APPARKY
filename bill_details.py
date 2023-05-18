from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import datetime
from PIL import Image, ImageTk
from babel.numbers import *
from babel.dates import *


class BillWindow:
    def __init__(self, root):
        self.bill_window = root
        self.bill_window.title("Bill Details")
        self.bill_window.geometry("1313x573+232+222")
        self.bill_window.maxsize(1313, 573)
        self.bill_window.minsize(1313, 573)

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

        def fetch_bill_data():
            mydb = sqlite3.connect("hotel_management_system.db")
            my_cursor = mydb.cursor()

            my_cursor.execute("SELECT * FROM bills")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.Bill_details_table.delete(*self.Bill_details_table.get_children())
                for i in data:
                    self.Bill_details_table.insert("", END, value=i)
                    mydb.commit()
                mydb.close()

        def get_bill_tree_data(event):
            try:
                cursor_row = self.Bill_details_table.focus()
                content = self.Bill_details_table.item(cursor_row)
                content_value = content["values"]

                self.sl_no_for_bill_var.set(int(content_value[0]))
                self.name_var_for_bill_var.set(content_value[1])
                self.ref_no_for_bill_var.set(int(content_value[2]))
                self.check_in_for_bill_var.set(content_value[3])
                self.check_out_for_bill_var.set(content_value[4])
                self.room_type_for_bill_var.set(content_value[5])
                self.allotted_room_for_bill_var.set(content_value[6])
                self.meal_type_for_bill_var.set(content_value[7])
                self.no_of_days_for_bill_var.set(int(content_value[8]))
                self.sub_amount_for_bill_var.set(int(content_value[9]))
                self.tax_amount_for_bill_var.set(int(content_value[10]))
                self.total_amount_for_bill_var.set(int(content_value[11]))

                fetch_bill_data()
            except Exception as e:
                pass

        def reset_bill_data():
            self.sl_no_for_bill_var.set(0)
            self.name_var_for_bill_var.set("")
            self.ref_no_for_bill_var.set(0)
            self.check_in_for_bill_var.set("")
            self.check_out_for_bill_var.set("")
            self.room_type_for_bill_var.set("")
            self.allotted_room_for_bill_var.set("")
            self.meal_type_for_bill_var.set("")
            self.no_of_days_for_bill_var.set(0)
            self.sub_amount_for_bill_var.set(0)
            self.tax_amount_for_bill_var.set(0)
            self.total_amount_for_bill_var.set(0)

            Name_label_entry.configure(state="readonly")
            Ref_no_label_entry.configure(state="readonly")
            Check_in_label_entry.configure(state="readonly")
            Check_out_label_entry.configure(state="readonly")
            Room_type_label_combobox.configure(state="readonly")
            Allotted_room_label_entry.configure(state="readonly")
            Meal_type_label_entry.configure(state="readonly")
            No_of_day_label_entry.configure(state="readonly")
            Sub_total_label_entry.configure(state="readonly")
            Tax_amount_label_entry.configure(state="readonly")
            Total_amount_label_entry.configure(state="readonly")

        def delete_bill_data():
            query = messagebox.askyesno("Are You Sure", "Are you Sure? You want to delete this data?", parent=self.bill_window)
            if query == 1:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    my_cursor.execute(f"DELETE FROM bills WHERE oid = {self.sl_no_for_bill_var.get()}")

                    mydb.commit()
                    mydb.close()

                    fetch_bill_data()

                    messagebox.showinfo("Successful", "Data has been deleted Successfully", parent=self.bill_window)

                except Exception as e:
                    fetch_bill_data()
                    messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.bill_window)

            else:
                fetch_bill_data()
                messagebox.showinfo("Info", "You have made a greate Decision!", parent=self.bill_window)

        def update_bill_data():
            update = messagebox.askyesno("Update", "Are you sure, You want to Update this Data?", parent=self.bill_window)
            if update == 1:
                Name_label_entry.configure(state=NORMAL)
                Ref_no_label_entry.configure(state=NORMAL)
                Check_in_label_entry.configure(state=NORMAL)
                Check_out_label_entry.configure(state=NORMAL)
                Allotted_room_label_entry.configure(state=NORMAL)
                Meal_type_label_entry.configure(state=NORMAL)
                No_of_day_label_entry.configure(state=NORMAL)
                Sub_total_label_entry.configure(state=NORMAL)
                Tax_amount_label_entry.configure(state=NORMAL)
                Total_amount_label_entry.configure(state=NORMAL)

            else:
                pass

            Update_Button_for_bill.configure(text="Update Now", command=update_now_bill_data)

        def update_now_bill_data():
            if self.name_var_for_bill_var.get() == "" or self.name_var_for_bill_var.get() == 0:
                messagebox.showerror("Error", "Name can not be Empty. Please fill the Entry.", parent=self.bill_window)

            elif self.ref_no_for_bill_var.get() == "" or self.ref_no_for_bill_var.get() == 0:
                messagebox.showerror("Error", "Ref No. can not be Empty. Please fill the Entry.", parent=self.bill_window)

            elif self.check_in_for_bill_var.get() == "" or self.check_in_for_bill_var.get() == 0:
                messagebox.showerror("Error", "Check In can not be Empty. Please fill the Entry.", parent=self.bill_window)

            elif self.check_out_for_bill_var.get() == "" or self.check_out_for_bill_var.get() == 0:
                messagebox.showerror("Error", "Check Out can not be Empty. Please fill the Entry.", parent=self.bill_window)

            elif self.allotted_room_for_bill_var.get() == "" or self.allotted_room_for_bill_var == 0:
                messagebox.showerror("Error", "Allotted Room can not be Empty. Please fill the Entry.", parent=self.bill_window)

            elif self.meal_type_for_bill_var.get() == "" or self.meal_type_for_bill_var.get() == 0:
                messagebox.showerror("Error", "Meal Type can not be Empty. Please fill the Entry.", parent=self.bill_window)

            elif self.no_of_days_for_bill_var.get() == "" or self.no_of_days_for_bill_var.get() == 0:
                messagebox.showerror("Error", "No Of Days can not be Empty. Please fill the Entry.", parent=self.bill_window)

            elif self.sub_amount_for_bill_var.get() == "" or self.sub_amount_for_bill_var.get() == 0:
                messagebox.showerror("Error", "Sub Total can not be Empty. Please fill the Entry.", parent=self.bill_window)

            elif self.tax_amount_for_bill_var.get() == "" or self.tax_amount_for_bill_var.get() == 0:
                messagebox.showerror("Error", "Tax can not be Empty. Please fill the Entry.", parent=self.bill_window)

            elif self.total_amount_for_bill_var.get() == "" or self.total_amount_for_bill_var.get() == 0:
                messagebox.showerror("Error", "Total Cost can not be Empty. Please fill the Entry.", parent=self.bill_window)

            else:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    my_cursor.execute("""UPDATE bills SET 
                                        Name = :name,
                                        Ref_No = :ref, 
                                        Check_In = :check_in, 
                                        Check_Out = :check_out, 
                                        Room_Type = :room,
                                        Allotted_Room = :allotted_room, 
                                        Meal_Type = :meal, 
                                        No_of_Days = :no_of_day, 
                                        Sub_amount = :sub_total, 
                                        Tax_amount = :tax, 
                                        Total_cost = :total

                                        WHERE oid = :oid""",
                                      {
                                          'name': self.name_var_for_bill_var.get(),
                                          'ref': self.ref_no_for_bill_var.get(),
                                          'check_in': self.check_in_for_bill_var.get(),
                                          'check_out': self.check_out_for_bill_var.get(),
                                          'room': self.room_type_for_bill_var.get(),
                                          'allotted_room': self.allotted_room_for_bill_var.get(),
                                          'meal': self.meal_type_for_bill_var.get(),
                                          'no_of_day': self.no_of_days_for_bill_var.get(),
                                          'sub_total': self.sub_amount_for_bill_var.get(),
                                          'tax': self.tax_amount_for_bill_var.get(),
                                          'total': self.total_amount_for_bill_var.get(),
                                          'oid': self.sl_no_for_bill_var.get()
                                      })

                    mydb.commit()
                    mydb.close()

                    Name_label_entry.configure(state="readonly")
                    Ref_no_label_entry.configure(state="readonly")
                    Check_in_label_entry.configure(state="readonly")
                    Check_out_label_entry.configure(state="readonly")
                    Allotted_room_label_entry.configure(state="readonly")
                    Meal_type_label_entry.configure(state="readonly")
                    No_of_day_label_entry.configure(state="readonly")
                    Sub_total_label_entry.configure(state="readonly")
                    Tax_amount_label_entry.configure(state="readonly")
                    Total_amount_label_entry.configure(state="readonly")

                    Update_Button_for_bill.configure(text="Update", command=update_bill_data)
                    messagebox.showinfo("Successful", "Data has been Updated Successfully", parent=self.bill_window)

                    fetch_bill_data()

                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong!!! {str(e)}", parent=self.bill_window)

        def refresh_bill_data():
            fetch_bill_data()

        def bill_from_bill_data():
            check_in = self.check_in_for_bill_var.get()
            check_out = self.check_out_for_bill_var.get()
            check_in = datetime.datetime.strptime(check_in, "%d/%m/%Y")
            check_out = datetime.datetime.strptime(check_out, "%d/%m/%Y")
            self.no_of_days_for_bill_var.set(abs(check_out - check_in).days)

            accommodation_list = list(accommodation.keys())
            room_type_list = list(room_type.keys())

            for i in accommodation_list:
                for j in room_type_list:
                    if self.room_type_for_bill_var.get() == j and self.meal_type_for_bill_var.get() == i:
                        single_day_fare = float(accommodation[self.meal_type_for_bill_var.get()] + room_type[
                            self.room_type_for_bill_var.get()])
                        total_fare = float(single_day_fare * float(self.no_of_days_for_bill_var.get()))

                        tax_fare = total_fare * 0.1
                        sub_total = total_fare
                        total_payment = float(tax_fare + sub_total)

                        self.sub_amount_for_bill_var.set(int(sub_total))
                        self.tax_amount_for_bill_var.set(int(tax_fare))
                        self.total_amount_for_bill_var.set(int(total_payment))

            messagebox.showinfo("Successful", "Bill has been Generated", parent=self.bill_window)

        ##################=================================================== Title Section ============================================================

        title_label_in_bill_tab = Label(self.bill_window, text="Details", font=("Calibre", 20, "bold"), background="black", foreground="gold", border=1, relief=RIDGE)
        title_label_in_bill_tab.place(x=0, y=0, width=1312, height=50)

        image_logo_in_bill_tab = Image.open(r"Images\logohotel.png")
        image_logo_in_bill_tab = image_logo_in_bill_tab.resize((100, 45), Image.ANTIALIAS)
        self.image_logo_in_bill_tab = ImageTk.PhotoImage(image_logo_in_bill_tab)

        image_logo_label_for_bill_tab = Label(self.bill_window, image=self.image_logo_in_bill_tab, border=0, relief=RIDGE)
        image_logo_label_for_bill_tab.place(x=2, y=2, width=100, height=45)

        exit_button_for_bill_tab = Button(self.bill_window, text="Exit", font=("Calibre", 20, "bold"), background="black", foreground="red", border=0, relief=RIDGE, cursor="hand2", command=self.bill_window.destroy)
        exit_button_for_bill_tab.place(x=1238, y=5, width=70, height=40)

        ###################=============================================== Label Frame =============================================================

        Bill_Details_Information_label_frame = LabelFrame(self.bill_window, text="Details Information", border=2, relief=RIDGE, padx=2, font=("Calibre", 10))
        Bill_Details_Information_label_frame.place(x=5, y=50, width=425, height=510)

        self.sl_no_for_bill_var = IntVar()
        self.name_var_for_bill_var = StringVar()
        self.ref_no_for_bill_var = IntVar()
        self.check_in_for_bill_var = StringVar()
        self.check_out_for_bill_var = StringVar()
        self.room_type_for_bill_var = StringVar()
        self.allotted_room_for_bill_var = StringVar()
        self.meal_type_for_bill_var = StringVar()
        self.no_of_days_for_bill_var = IntVar()
        self.sub_amount_for_bill_var = IntVar()
        self.tax_amount_for_bill_var = IntVar()
        self.total_amount_for_bill_var = IntVar()

        Name_label = Label(Bill_Details_Information_label_frame, text="Name", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Name_label.grid(row=0, column=0, sticky=W)
        Name_label_entry = ttk.Entry(Bill_Details_Information_label_frame, width=30, font=("arial", 12), textvariable=self.name_var_for_bill_var, state="readonly")
        Name_label_entry.grid(row=0, column=1, sticky=W, padx=4)

        Ref_No_label = Label(Bill_Details_Information_label_frame, text="Ref No.", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Ref_No_label.grid(row=1, column=0, sticky=W)
        Ref_no_label_entry = ttk.Entry(Bill_Details_Information_label_frame, width=30, font=("arial", 12), textvariable=self.ref_no_for_bill_var, state="readonly")
        Ref_no_label_entry.grid(row=1, column=1, sticky=E, padx=4)

        Check_in_label = Label(Bill_Details_Information_label_frame, text="Check In", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Check_in_label.grid(row=2, column=0, sticky=W)
        Check_in_label_entry = ttk.Entry(Bill_Details_Information_label_frame, width=30, font=("arial", 12), textvariable=self.check_in_for_bill_var, state="readonly")
        Check_in_label_entry.grid(row=2, column=1, sticky=E, padx=4)

        Check_out_label = Label(Bill_Details_Information_label_frame, text="Check Out", font=("Calibre", 12, "bold"),padx=4, pady=8)
        Check_out_label.grid(row=3, column=0, sticky=W)
        Check_out_label_entry = ttk.Entry(Bill_Details_Information_label_frame, width=30, font=("arial", 12), textvariable=self.check_out_for_bill_var, state="readonly")
        Check_out_label_entry.grid(row=3, column=1, sticky=E, padx=4)

        Room_type_label = Label(Bill_Details_Information_label_frame, text="Room Type", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Room_type_label.grid(row=4, column=0, sticky=W)
        Room_type_label_combobox = ttk.Combobox(Bill_Details_Information_label_frame, width=28, font=("arial", 12), state="readonly", textvariable=self.room_type_for_bill_var)
        Room_type_label_combobox["values"] = ("Single", "Double", "Luxury", "Deluxe", "Super Deluxe")
        Room_type_label_combobox.set("")
        Room_type_label_combobox.grid(row=4, column=1, sticky=E, padx=4)

        Allotted_room_label = Label(Bill_Details_Information_label_frame, text="Allotted Room", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Allotted_room_label.grid(row=5, column=0, sticky=W)
        Allotted_room_label_entry = ttk.Entry(Bill_Details_Information_label_frame, width=30, font=("arial", 12), textvariable=self.allotted_room_for_bill_var, state="readonly")
        Allotted_room_label_entry.grid(row=5, column=1, sticky=E, padx=4)

        Meal_type_label = Label(Bill_Details_Information_label_frame, text="Meal", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Meal_type_label.grid(row=6, column=0, sticky=W)
        Meal_type_label_entry = ttk.Entry(Bill_Details_Information_label_frame, width=30, font=("arial", 12), textvariable=self.meal_type_for_bill_var, state="readonly")
        Meal_type_label_entry.grid(row=6, column=1, sticky=E, padx=4)

        No_of_day_label = Label(Bill_Details_Information_label_frame, text="No of Days", font=("Calibre", 12, "bold"), padx=4, pady=8)
        No_of_day_label.grid(row=7, column=0, sticky=W)
        No_of_day_label_entry = ttk.Entry(Bill_Details_Information_label_frame, width=30, font=("arial", 12), textvariable=self.no_of_days_for_bill_var, state="readonly")
        No_of_day_label_entry.grid(row=7, column=1, sticky=E, padx=4)

        Sub_total_label = Label(Bill_Details_Information_label_frame, text="Sub Total", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Sub_total_label.grid(row=8, column=0, sticky=W)
        Sub_total_label_entry = ttk.Entry(Bill_Details_Information_label_frame, width=30, font=("arial", 12), textvariable=self.sub_amount_for_bill_var, state="readonly")
        Sub_total_label_entry.grid(row=8, column=1, sticky=E, padx=4)

        Tax_amount_label = Label(Bill_Details_Information_label_frame, text="Tax", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Tax_amount_label.grid(row=9, column=0, sticky=W)
        Tax_amount_label_entry = ttk.Entry(Bill_Details_Information_label_frame, width=30, font=("arial", 12), textvariable=self.tax_amount_for_bill_var, state="readonly")
        Tax_amount_label_entry.grid(row=9, column=1, sticky=E, padx=4)

        Total_amount_label = Label(Bill_Details_Information_label_frame, text="Total Cost", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Total_amount_label.grid(row=10, column=0, sticky=W)
        Total_amount_label_entry = ttk.Entry(Bill_Details_Information_label_frame, width=30, font=("arial", 12), textvariable=self.total_amount_for_bill_var, state="readonly")
        Total_amount_label_entry.grid(row=10, column=1, sticky=E, padx=4)

        ############======================================================= Buttons =========================================================================

        Button_Frame = Frame(Bill_Details_Information_label_frame, border=2, relief=RIDGE)
        Button_Frame.place(x=3, y=445, width=412, height=40)

        Update_Button_for_bill = Button(Button_Frame, text="Update", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=11, cursor="hand2", command=update_bill_data)
        Update_Button_for_bill.grid(row=0, column=0, padx=1, pady=2)

        Delete_Button_for_bill = Button(Button_Frame, text="Delete", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, cursor="hand2", command=delete_bill_data)
        Delete_Button_for_bill.grid(row=0, column=1, padx=1, pady=2)

        Reset_button_for_bill = Button(Button_Frame, text="Reset", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=11, cursor="hand2", command=reset_bill_data)
        Reset_button_for_bill.grid(row=0, column=2, padx=1, pady=2)

        Bill_button_for_bill_details = Button(Button_Frame, text="Bill", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=8, cursor="hand2", command=bill_from_bill_data)
        Bill_button_for_bill_details.grid(row=0, column=3, padx=1, pady=2)

        ############============================================================ Right Frame ===================================================================

        self.search_by_table_for_bill_var = StringVar()
        self.search_by_attribute_for_bill_var = StringVar()

        Bill_Details_and_search_system_frame_for_bill_tab = LabelFrame(self.bill_window, border=2, relief=RIDGE, text="Bill Details and Search System", font=("Calibre", 10))
        Bill_Details_and_search_system_frame_for_bill_tab.place(x=440, y=50, width=865, height=510)

        Search_by_label_for_bill = Label(Bill_Details_and_search_system_frame_for_bill_tab, font=("Calibre", 12, "bold"), text="Search By", background="red", foreground="white")
        Search_by_label_for_bill.grid(row=0, column=0, sticky=W, padx=5)

        Search_by_table_for_bill_name_combobox = ttk.Combobox(Bill_Details_and_search_system_frame_for_bill_tab, font=("Calibre", 12), width=20, state="readonly", textvariable=self.search_by_table_for_bill_var)
        Search_by_table_for_bill_name_combobox["values"] = ("Name", "Check In", "Check Out", "Room Type", "Allotted Room", "Meal")
        Search_by_table_for_bill_name_combobox.set("")
        Search_by_table_for_bill_name_combobox.grid(row=0, column=1, padx=2)

        Search_by_attribute_for_bill_combobox = ttk.Combobox(Bill_Details_and_search_system_frame_for_bill_tab, font=("Calibre", 12), width=20, textvariable=self.search_by_attribute_for_bill_var)
        Search_by_attribute_for_bill_combobox["values"] = ("")
        Search_by_attribute_for_bill_combobox.set("")
        Search_by_attribute_for_bill_combobox.grid(row=0, column=2, padx=2)

        Search_for_bill_button = Button(Bill_Details_and_search_system_frame_for_bill_tab, text="Search", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, cursor="hand2")
        Search_for_bill_button.grid(row=0, column=3, padx=10)

        ShowAll_for_bill_button = Button(Bill_Details_and_search_system_frame_for_bill_tab, text="Show All", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, cursor="hand2")
        ShowAll_for_bill_button.grid(row=0, column=4)

        refresh_for_bill_button = Button(Bill_Details_and_search_system_frame_for_bill_tab, text="Refresh", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, cursor="hand2", command=refresh_bill_data)
        refresh_for_bill_button.grid(row=0, column=5, padx=10)

        ######========================================================== Show Bill Data Table ========================================================================

        Bill_Date_table_frame = Frame(Bill_Details_and_search_system_frame_for_bill_tab, border=2, relief=RIDGE)
        Bill_Date_table_frame.place(x=0, y=40, width=860, height=450)

        scroll_bar_for_bill_x = ttk.Scrollbar(Bill_Date_table_frame, orient=HORIZONTAL)
        scroll_bar_for_bill_y = ttk.Scrollbar(Bill_Date_table_frame, orient=VERTICAL)

        self.Bill_details_table = ttk.Treeview(Bill_Date_table_frame, columns=("bill_no", "name", "cust_id", "checkin", "checkout", "room type", "allotted room", "meal", "no of days", "sub total", "tax amount", "total cost"), xscrollcommand=scroll_bar_for_bill_x.set, yscrollcommand=scroll_bar_for_bill_y.set)
        scroll_bar_for_bill_x.pack(side=BOTTOM, fill=X)
        scroll_bar_for_bill_y.pack(side=RIGHT, fill=Y)

        self.Bill_details_table.heading("bill_no", text="Bill No.", anchor=CENTER)
        self.Bill_details_table.heading("name", text="Name", anchor=CENTER)
        self.Bill_details_table.heading("cust_id", text="Customer ID", anchor=CENTER)
        self.Bill_details_table.heading("checkin", text="Check In", anchor=CENTER)
        self.Bill_details_table.heading("checkout", text="Check Out", anchor=CENTER)
        self.Bill_details_table.heading("room type", text="Room Type", anchor=CENTER)
        self.Bill_details_table.heading("allotted room", text="Allotted Room", anchor=CENTER)
        self.Bill_details_table.heading("meal", text="Meal", anchor=CENTER)
        self.Bill_details_table.heading("no of days", text="No of Days", anchor=CENTER)
        self.Bill_details_table.heading("sub total", text="Sub Total", anchor=CENTER)
        self.Bill_details_table.heading("tax amount", text="Tax Amount", anchor=CENTER)
        self.Bill_details_table.heading("total cost", text="Total Amount", anchor=CENTER)

        self.Bill_details_table["show"] = "headings"

        self.Bill_details_table.column("bill_no", width=60, anchor=CENTER)
        self.Bill_details_table.column("name", width=120, anchor=CENTER)
        self.Bill_details_table.column("cust_id", width=60, anchor=CENTER)
        self.Bill_details_table.column("checkin", width=80, anchor=CENTER)
        self.Bill_details_table.column("checkout", width=80, anchor=CENTER)
        self.Bill_details_table.column("room type", width=80, anchor=CENTER)
        self.Bill_details_table.column("allotted room", width=100, anchor=CENTER)
        self.Bill_details_table.column("meal", width=100, anchor=CENTER)
        self.Bill_details_table.column("no of days", width=80, anchor=CENTER)
        self.Bill_details_table.column("sub total", width=80, anchor=CENTER)
        self.Bill_details_table.column("tax amount", width=80, anchor=CENTER)
        self.Bill_details_table.column("total cost", width=80, anchor=CENTER)

        self.Bill_details_table.pack(fill=BOTH, expand=1)
        self.Bill_details_table.bind("<ButtonRelease-1>", get_bill_tree_data)
        fetch_bill_data()


if __name__ == '__main__':
    root = Tk()
    obj = BillWindow(root)
    root.mainloop()
