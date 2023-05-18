from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
from babel.numbers import *
from babel.dates import *


class RoomDetailsWindow:
    def __init__(self, root):
        self.room_detail_window = root
        self.room_detail_window.title("Details")
        self.room_detail_window.geometry("1313x573+232+222")
        self.room_detail_window.maxsize(1313, 573)
        self.room_detail_window.minsize(1313, 573)

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

        def add_for_room():
            try:
                if self.floor_for_room_var.get() == 0 or self.floor_for_room_var.get() == "":
                    messagebox.showerror("Error", "Floor Can not be Empty! Please fill the Floor Entry", parent=self.room_detail_window)

                elif self.room_no_var.get() == 0 or self.room_no_var.get() == "":
                    messagebox.showerror("Error", "Room No. Can not be Empty! Please fill the Room No. Entry", parent=self.room_detail_window)

                elif self.room_type_for_room_var.get() == 0 or self.room_no_var.get() == "":
                    messagebox.showerror("Error", "Room Type Can not be Empty! Please fill the Room Type Entry", parent=self.room_detail_window)

                elif self.availability_var.get() == 0 or self.availability_var.get() == "":
                    messagebox.showerror("Error", "Availability Can not be Empty! Please fill the Availability Entry", parent=self.room_detail_window)

                elif self.room_cost_var.get() == 0 or self.room_cost_var.get() == "":
                    messagebox.showerror("Error", "Room Cost Can not be Empty! Please fill the Room Cost Entry", parent=self.room_detail_window)

                elif self.room_status_var.get() == 0 or self.room_status_var.get() == "":
                    messagebox.showerror("Error", "Room Status Can not be Empty! Please fill the Room Status Entry", parent=self.room_detail_window)

                else:
                    try:
                        mydb = sqlite3.connect("hotel_management_system.db")
                        my_cursor = mydb.cursor()

                        my_cursor.execute("""INSERT INTO room_types VALUES (:room_no, :floor, :room_type, :availability, :room_cost, :room_status)""",
                                          {
                                              'room_no': self.room_no_var.get(),
                                              'floor': self.floor_for_room_var.get(),
                                              'room_type': self.room_type_for_room_var.get(),
                                              'availability': self.availability_var.get(),
                                              'room_cost': self.room_cost_var.get(),
                                              'room_status': self.room_status_var.get()
                                          })

                        mydb.commit()
                        mydb.close()
                        fetch_room_data()
                        messagebox.showinfo("Successful", "Your data has been added Successfully.", parent=self.room_detail_window)
                        reset_for_room()

                    except Exception as e:
                        messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.room_detail_window)

            except Exception as e:
                messagebox.showerror("Error", "Something went Wrong!! Entries might me Empty!! Please check Entries before the Operation", parent=self.room_detail_window)

        def update_for_room():
            if self.floor_for_room_var.get() == 0 or self.floor_for_room_var.get() == "":
                messagebox.showerror("Error", "Floor Can not be Empty! Please fill the Floor Entry", parent=self.room_detail_window)

            elif self.room_no_var.get() == 0 or self.room_no_var.get() == "":
                messagebox.showerror("Error", "Room No. Can not be Empty! Please fill the Room No. Entry", parent=self.room_detail_window)

            elif self.room_type_for_room_var.get() == 0 or self.room_no_var.get() == "":
                messagebox.showerror("Error", "Room Type Can not be Empty! Please fill the Room Type Entry", parent=self.room_detail_window)

            elif self.availability_var.get() == 0 or self.availability_var.get() == "":
                messagebox.showerror("Error", "Availability Can not be Empty! Please fill the Availability Entry", parent=self.room_detail_window)

            elif self.room_cost_var.get() == 0 or self.room_cost_var.get() == "":
                messagebox.showerror("Error", "Room Cost Can not be Empty! Please fill the Room Cost Entry", parent=self.room_detail_window)

            elif self.room_status_var.get() == 0 or self.room_status_var.get() == "":
                messagebox.showerror("Error", "Room Status Can not be Empty! Please fill the Room Status Entry", parent=self.room_detail_window)

            else:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    my_cursor.execute("""UPDATE room_types SET
                                            Floor = :floor,  
                                            Room_Type = :room_type, 
                                            Availability = :availability, 
                                            Room_Cost = :cost, 
                                            Room_Status = :status
                                            
                                            WHERE Room_No = :room_no""",
                                      {
                                          'floor': self.floor_for_room_var.get(),
                                          'room_type': self.room_type_for_room_var.get(),
                                          'availability': self.availability_var.get(),
                                          'cost': self.room_cost_var.get(),
                                          'status': self.room_status_var.get(),
                                          'room_no': self.room_no_var.get()
                                      })

                    mydb.commit()
                    mydb.close()
                    fetch_room_data()
                    messagebox.showinfo("Successful", "Data has been updated Successfully", parent=self.room_detail_window)

                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.room_detail_window)

        def delete_for_room():
            delete = messagebox.askyesno("Delete", f"Are You Sure! You want to Delete this Data?", parent=self.room_detail_window)
            if delete == 1:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    my_cursor.execute(f"DELETE FROM room_types WHERE Room_No = {self.room_no_var.get()}")

                    mydb.commit()
                    mydb.close()

                    fetch_room_data()
                    messagebox.showinfo("Delete", "Data has been Deleted Successfully", parent=self.room_detail_window)
                    reset_for_room()

                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.room_detail_window)

            else:
                pass

        def reset_for_room():
            self.floor_for_room_var.set("")
            self.room_no_var.set(self.room_no_var.get() + 1)
            self.room_type_for_room_var.set("")
            self.availability_var.set("")
            self.room_cost_var.set("")
            self.room_status_var.set("")

            fetch_room_data()

        def fetch_room_data():
            mydb = sqlite3.connect("hotel_management_system.db")
            my_cursor = mydb.cursor()

            my_cursor.execute("""SELECT * FROM room_types""")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.Room_details_table.delete(* self.Room_details_table.get_children())
                for i in data:
                    self.Room_details_table.insert("", END, value=i)
                    mydb.commit()
                mydb.close()

        def get_room_data_from_tree(event):
            try:
                cursor_row = self.Room_details_table.focus()
                content = self.Room_details_table.item(cursor_row)
                content_value = content["values"]

                self.room_no_var.set(int(content_value[0]))
                self.floor_for_room_var.set(content_value[1])
                self.room_type_for_room_var.set(content_value[2])
                self.availability_var.set(content_value[3])
                self.room_cost_var.set(int(content_value[4]))
                self.room_status_var.set(content_value[5])

            except Exception as e:
                pass

        def search_by_for_room():
            mydb = sqlite3.connect("hotel_management_system.db")
            my_cursor = mydb.cursor()

            if self.search_by_table_for_room_var.get() == "" or self.search_by_attribute_for_room_var.get() == "":
                messagebox.showerror("Error", "Invalid Entry!! Please check your Values", parent=self.room_detail_window)

            else:
                try:
                    if self.search_by_table_for_room_var.get() == search_by_types_list[0]:
                        my_cursor.execute(f"SELECT * FROM room_types WHERE {self.search_by_table_for_room_var.get()} = '{self.search_by_attribute_for_room_var.get()}'")
                        data = my_cursor.fetchall()
                        if len(data) >= 1:
                            self.Room_details_table.delete(*self.Room_details_table.get_children())
                            for i in data:
                                self.Room_details_table.insert("", END, values=i)

                        else:
                            self.Room_details_table.delete(*self.Room_details_table.get_children())
                            mydb.commit()
                        mydb.close()

                    elif self.search_by_table_for_room_var.get() == search_by_types_list[1]:
                        my_cursor.execute(f"""SELECT * FROM room_types WHERE Room_Type = '{self.search_by_attribute_for_room_var.get()}'""")
                        data = my_cursor.fetchall()
                        if len(data) >= 1:
                            self.Room_details_table.delete(* self.Room_details_table.get_children())
                            for i in data:
                                self.Room_details_table.insert("", END, values=i)

                        else:
                            self.Room_details_table.delete(* self.Room_details_table.get_children())
                            mydb.commit()
                        mydb.close()

                    elif self.search_by_table_for_room_var.get() == search_by_types_list[2]:
                        my_cursor.execute(f"""SELECT * FROM room_types WHERE {self.search_by_table_for_room_var.get()} = '{self.search_by_attribute_for_room_var.get()}'""")
                        data = my_cursor.fetchall()
                        if len(data) >= 1:
                            self.Room_details_table.delete(* self.Room_details_table.get_children())
                            for i in data:
                                self.Room_details_table.insert("", END, values=i)

                        else:
                            self.Room_details_table.delete(* self.Room_details_table.get_children())
                            mydb.commit()
                        mydb.close()

                    elif self.search_by_table_for_room_var.get() == search_by_types_list[3]:
                        my_cursor.execute(f"""SELECT * FROM room_types WHERE Room_Status = '{self.search_by_attribute_for_room_var.get()}'""")
                        data = my_cursor.fetchall()
                        if len(data) >= 1:
                            self.Room_details_table.delete(* self.Room_details_table.get_children())
                            for i in data:
                                self.Room_details_table.insert("", END, values=i)

                        else:
                            self.Room_details_table.delete(* self.Room_details_table.get_children())
                            mydb.commit()
                        mydb.close()

                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong!! {str(e)}", parent=self.room_detail_window)

        def search_by_attribute_for_room(event):
            floor_list = ("1st Floor", "2nd Floor", "3rd Floor")
            if self.search_by_table_for_room_var.get() == search_by_types_list[0]:
                Search_by_attribute_for_room_combobox["values"] = floor_list
                Search_by_attribute_for_room_combobox.set("")
                Search_by_attribute_for_room_combobox.configure(state="readonly")

            elif self.search_by_table_for_room_var.get() == search_by_types_list[1]:
                Search_by_attribute_for_room_combobox["values"] = list(room_type.keys())
                Search_by_attribute_for_room_combobox.set("")
                Search_by_attribute_for_room_combobox.configure(state="readonly")

            elif self.search_by_table_for_room_var.get() == search_by_types_list[2]:
                Search_by_attribute_for_room_combobox["values"] = ("Yes", "No")
                Search_by_attribute_for_room_combobox.set("")
                Search_by_attribute_for_room_combobox.configure(state="readonly")

            elif self.search_by_table_for_room_var.get() == search_by_types_list[3]:
                Search_by_attribute_for_room_combobox["values"] = ("OK", "On Servicing")
                Search_by_attribute_for_room_combobox.set("")
                Search_by_attribute_for_room_combobox.configure(state="readonly")

        def show_all_room_datas():
            fetch_room_data()
            self.search_by_table_for_room_var.set("")
            self.search_by_attribute_for_room_var.set("")

        def floor_settings(event):
            floor_list = ("1st Floor", "2nd Floor", "3rd Floor")
            if self.floor_for_room_var.get() == floor_list[0]:
                self.room_no_var.set("")
                self.room_no_var.set(100)

            elif self.floor_for_room_var.get() == floor_list[1]:
                self.room_no_var.set("")
                self.room_no_var.set(200)

        ##################=================================================== Title Section ============================================================

        search_by_types_list = ("Floor", "Room Type", "Availability", "Room Status")

        title_label_in_room_tab = Label(self.room_detail_window, text="Details", font=("Calibre", 20, "bold"), background="black", foreground="gold", border=1, relief=RIDGE)
        title_label_in_room_tab.place(x=0, y=0, width=1313, height=50)

        image_logo_in_room_tab = Image.open(r"Images\logohotel.png")
        image_logo_in_room_tab = image_logo_in_room_tab.resize((100, 45), Image.ANTIALIAS)
        self.image_logo_in_room_tab = ImageTk.PhotoImage(image_logo_in_room_tab)

        image_logo_label_in_room_tab = Label(self.room_detail_window, image=self.image_logo_in_room_tab, border=0, relief=RIDGE)
        image_logo_label_in_room_tab.place(x=2, y=2, width=100, height=45)

        exit_button_in_room_tab = Button(self.room_detail_window, text="Exit", font=("Calibre", 20, "bold"), background="black", foreground="red", border=0, relief=RIDGE, cursor="hand2", command=self.room_detail_window.destroy)
        exit_button_in_room_tab.place(x=1240, y=5, width=70, height=40)

        ###################=============================================== Label Frame =============================================================

        Room_Details_Information_label_frame = LabelFrame(self.room_detail_window, text="Details Information", border=2, relief=RIDGE, padx=2, font=("Calibre", 10))
        Room_Details_Information_label_frame.place(x=5, y=50, width=425, height=510)

        self.floor_for_room_var = StringVar()
        self.room_no_var = IntVar()
        self.room_type_for_room_var = StringVar()
        self.availability_var = StringVar()
        self.room_cost_var = IntVar()
        self.room_status_var = StringVar()

        Floor_label = Label(Room_Details_Information_label_frame, text="Floor", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Floor_label.grid(row=0, column=0, sticky=W)
        Floor_label_combobox = ttk.Combobox(Room_Details_Information_label_frame, width=28, font=("arial", 12), state="readonly", textvariable=self.floor_for_room_var)
        Floor_label_combobox["values"] = ("1st Floor", "2nd Floor", "3rd Floor")
        Floor_label_combobox.bind("<<ComboboxSelected>>", floor_settings)
        Floor_label_combobox.grid(row=0, column=1, sticky=W, padx=4)
        self.floor_for_room_var.set("")

        Room_No_label = Label(Room_Details_Information_label_frame, text="Room No.", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Room_No_label.grid(row=1, column=0, sticky=W)
        Room_no_label_entry = ttk.Entry(Room_Details_Information_label_frame, width=30, font=("arial", 12), textvariable=self.room_no_var)
        Room_no_label_entry.grid(row=1, column=1, sticky=E, padx=4)
        self.room_no_var.set("")

        Room_type_label = Label(Room_Details_Information_label_frame, text="Room Type", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Room_type_label.grid(row=2, column=0, sticky=W)
        Room_type_label_combobox = ttk.Combobox(Room_Details_Information_label_frame, width=28, font=("arial", 12), state="readonly", textvariable=self.room_type_for_room_var)
        Room_type_label_combobox["values"] = list(room_type.keys())
        Room_type_label_combobox.set("")
        Room_type_label_combobox.grid(row=2, column=1, sticky=E, padx=4)

        Availability_label = Label(Room_Details_Information_label_frame, text="Availability", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Availability_label.grid(row=3, column=0, sticky=W)
        Availability_label_combobox = ttk.Combobox(Room_Details_Information_label_frame, width=28, font=("arial", 12), state="readonly", textvariable=self.availability_var)
        Availability_label_combobox["values"] = ("Yes", "No")
        Availability_label_combobox.set("")
        Availability_label_combobox.grid(row=3, column=1, sticky=E, padx=4)

        Room_cost_label = Label(Room_Details_Information_label_frame, text="Room Cost", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Room_cost_label.grid(row=4, column=0, sticky=W)
        Room_cost_label_entry = ttk.Entry(Room_Details_Information_label_frame, width=30, font=("arial", 12), textvariable=self.room_cost_var)
        Room_cost_label_entry.grid(row=4, column=1, sticky=E, padx=4)
        self.room_cost_var.set("")

        Room_status_label = Label(Room_Details_Information_label_frame, text="Room Status", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Room_status_label.grid(row=5, column=0, sticky=W)
        Room_status_label_combobox = ttk.Combobox(Room_Details_Information_label_frame, width=28, font=("arial", 12), state="readonly", textvariable=self.room_status_var)
        Room_status_label_combobox["values"] = ("OK", "On Servicing")
        Room_status_label_combobox.set("")
        Room_status_label_combobox.grid(row=5, column=1, sticky=E, padx=4)

        ############========================================================= Buttons =========================================================================

        Button_Frame = Frame(Room_Details_Information_label_frame, border=2, relief=RIDGE)
        Button_Frame.place(x=1, y=445, width=414, height=40)

        Add_Button_for_room = Button(Button_Frame, text="Add", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=7, cursor="hand2", command=add_for_room)
        Add_Button_for_room.grid(row=0, column=0, padx=1, pady=2)

        Update_Button_for_room = Button(Button_Frame, text="Update", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=9, cursor="hand2", command=update_for_room)
        Update_Button_for_room.grid(row=0, column=1, padx=1, pady=2)

        Delete_Button_for_room = Button(Button_Frame, text="Delete", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=8, cursor="hand2", command=delete_for_room)
        Delete_Button_for_room.grid(row=0, column=2, padx=1, pady=2)

        Reset_button_for_room = Button(Button_Frame, text="Reset", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=8, cursor="hand2", command=reset_for_room)
        Reset_button_for_room.grid(row=0, column=3, padx=1, pady=2)

        bill_button_for_room = Button(Button_Frame, text="Bill", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=7, cursor="hand2")
        bill_button_for_room.grid(row=0, column=4, padx=1, pady=2)

        ############============================================================ Right Frame ===================================================================

        self.search_by_table_for_room_var = StringVar()
        self.search_by_attribute_for_room_var = StringVar()

        Room_details_and_search_system_frame = LabelFrame(self.room_detail_window, border=2, relief=RIDGE, text="Room Details and Search System", font=("Calibre", 10))
        Room_details_and_search_system_frame.place(x=440, y=50, width=865, height=510)

        Search_by_label_for_room = Label(Room_details_and_search_system_frame, font=("Calibre", 12, "bold"), text="Search By", background="red", foreground="white")
        Search_by_label_for_room.grid(row=0, column=0, sticky=W, padx=5)

        Search_by_table_for_room_name_combobox = ttk.Combobox(Room_details_and_search_system_frame, font=("Calibre", 12), width=20, state="readonly", textvariable=self.search_by_table_for_room_var)
        Search_by_table_for_room_name_combobox["values"] = ("Floor", "Room Type", "Availability", "Room Status")
        Search_by_table_for_room_name_combobox.set("")
        Search_by_table_for_room_name_combobox.bind("<<ComboboxSelected>>", search_by_attribute_for_room)
        Search_by_table_for_room_name_combobox.grid(row=0, column=1, padx=2)

        Search_by_attribute_for_room_combobox = ttk.Combobox(Room_details_and_search_system_frame, font=("Calibre", 12), width=20, state="readonly", textvariable=self.search_by_attribute_for_room_var)
        Search_by_attribute_for_room_combobox["values"] = ("")
        Search_by_attribute_for_room_combobox.set("")
        Search_by_attribute_for_room_combobox.grid(row=0, column=2, padx=2)

        Search_for_room_button = Button(Room_details_and_search_system_frame, text="Search", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, cursor="hand2", command=search_by_for_room)
        Search_for_room_button.grid(row=0, column=3, padx=10)

        ShowAll_for_room_button = Button(Room_details_and_search_system_frame, text="Show All", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, cursor="hand2", command=show_all_room_datas)
        ShowAll_for_room_button.grid(row=0, column=4)

        refresh_for_room_button = Button(Room_details_and_search_system_frame, text="Refresh", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, cursor="hand2")
        refresh_for_room_button.grid(row=0, column=5, padx=10)

        ######========================================================== Show Room Data Table ========================================================================

        Room_Date_table_frame = Frame(Room_details_and_search_system_frame, border=2, relief=RIDGE)
        Room_Date_table_frame.place(x=0, y=40, width=860, height=450)

        scroll_bar_for_room_x = ttk.Scrollbar(Room_Date_table_frame, orient=HORIZONTAL)
        scroll_bar_for_room_y = ttk.Scrollbar(Room_Date_table_frame, orient=VERTICAL)

        self.Room_details_table = ttk.Treeview(Room_Date_table_frame, columns=("room no", "floor", "room type", "availability", "room cost", "room status"), xscrollcommand=scroll_bar_for_room_x.set, yscrollcommand=scroll_bar_for_room_y.set)
        scroll_bar_for_room_x.pack(side=BOTTOM, fill=X)
        scroll_bar_for_room_y.pack(side=RIGHT, fill=Y)

        scroll_bar_for_room_x.config(command=self.Room_details_table.xview)
        scroll_bar_for_room_y.config(command=self.Room_details_table.yview)

        self.Room_details_table.heading("room no", text="Room No.", anchor=CENTER)
        self.Room_details_table.heading("floor", text="Floor", anchor=CENTER)
        self.Room_details_table.heading("room type", text="Room Type", anchor=CENTER)
        self.Room_details_table.heading("availability", text="Availability", anchor=CENTER)
        self.Room_details_table.heading("room cost", text="Room Cost", anchor=CENTER)
        self.Room_details_table.heading("room status", text="Room Status", anchor=CENTER)

        self.Room_details_table["show"] = "headings"

        self.Room_details_table.column("room no", width=40, anchor=CENTER)
        self.Room_details_table.column("floor", width=40, anchor=CENTER)
        self.Room_details_table.column("room type", width=100, anchor=CENTER)
        self.Room_details_table.column("availability", width=100, anchor=CENTER)
        self.Room_details_table.column("room cost", width=100, anchor=CENTER)
        self.Room_details_table.column("room status", width=120, anchor=CENTER)

        self.Room_details_table.pack(fill=BOTH, expand=1)
        self.Room_details_table.bind("<ButtonRelease-1>", get_room_data_from_tree)
        fetch_room_data()



if __name__ == '__main__':
    root = Tk()
    obj = RoomDetailsWindow(root)
    root.mainloop()
