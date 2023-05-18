from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import datetime
import time
from babel.numbers import *
from babel.dates import *


class PlanDetailsWindow:
    def __init__(self, root):
        self.plan_details = root
        self.plan_details.title("Accommodation Plan Details")
        self.plan_details.geometry("1313x573+232+222")
        self.plan_details.maxsize(1313, 573)
        self.plan_details.minsize(1313, 573)

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

        #### Room Table ####

        mydb = sqlite3.connect("hotel_management_system.db")
        my_cursor = mydb.cursor()

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

        def add_planer():
            try:
                mydb = sqlite3.connect("hotel_management_system.db")
                my_cursor = mydb.cursor()

                my_cursor.execute("""INSERT INTO planner VALUES(:planer_id, :planer_type, :single_cost, :double_cost, :luxury_cost, :delux_cost, :super_delux_cost, :update_date, :update_time)""",
                                  {
                                      'planer_id': self.planer_id_var.get(),
                                      'planer_type': self.planer_type_var.get(),
                                      'single_cost': self.single_room_cost_var.get(),
                                      'double_cost': self.double_room_cost_var.get(),
                                      'luxury_cost': self.luxury_room_cost_var.get(),
                                      'delux_cost': self.delux_room_cost_var.get(),
                                      'super_delux_cost': self.super_delux_room_cost_var.get(),
                                      'update_date': self.updated_date_var.get(),
                                      'update_time': self.updated_time_var.get()
                                  })

                mydb.commit()
                mydb.close()
                fetch_date()
                messagebox.showinfo("Successful", "Data has been added Successfully", parent=self.plan_details)

            except Exception as e:
                messagebox.showerror("Error", f"Something Went Wrong {str(e)}", parent=self.plan_details)

        def update_planner():
            query = messagebox.askyesno("Update", "Are you sure you want to update this data?", parent=self.plan_details)
            if query == 1:
                if self.planer_id_var.get() == "" or self.planer_id_var.get() == 0:
                    messagebox.showerror("Error", "Planner ID can not be Empty", parent=self.plan_details)

                elif self.planer_type_var.get() == "" or self.planer_type_var.get() == 0:
                    messagebox.showerror("Error", "Planner Type can not be Empty", parent=self.plan_details)

                elif self.single_room_cost_var.get() == "" or self.single_room_cost_var.get() == 0:
                    messagebox.showerror("Error", "Single Room Cost can not be Empty", parent=self.plan_details)

                elif self.double_room_cost_var.get() == "" or self.double_room_cost_var.get() == 0:
                    messagebox.showerror("Error", "Double Room Cost can not be Empty", parent=self.plan_details)

                elif self.luxury_room_cost_var.get() == "" or self.luxury_room_cost_var.get() == 0:
                    messagebox.showerror("Error", "Luxury Room Cost can not be Empty", parent=self.plan_details)

                elif self.delux_room_cost_var.get() == "" or self.delux_room_cost_var.get() == 0:
                    messagebox.showerror("Error", "Delux Room Cost can not be Empty", parent=self.plan_details)

                elif self.super_delux_room_cost_var.get() == "" or self.super_delux_room_cost_var.get() == 0:
                    messagebox.showerror("Error", "Super Delux Room Cost can not be Empty", parent=self.plan_details)

                else:
                    try:
                        mydb = sqlite3.connect("hotel_management_system.db")
                        my_cursor = mydb.cursor()

                        my_cursor.execute("""UPDATE planner SET 
                                            Single_cost = :single, 
                                            Double_cost = :double, 
                                            Luxury_cost = :luxury, 
                                            Delux_cost = :delux, 
                                            Super_Delux_cost = :sup_delux, 
                                            Latest_Updated_as_date = :_date, 
                                            Latest_update_as_time = :_time
                                            
                                            Where Planner_ID = :id""",
                                          {
                                              'single': self.single_room_cost_var.get(),
                                              'double': self.double_room_cost_var.get(),
                                              'luxury': self.luxury_room_cost_var.get(),
                                              'delux': self.delux_room_cost_var.get(),
                                              'sup_delux': self.super_delux_room_cost_var.get(),
                                              '_date': self.updated_date_var.get(),
                                              '_time': self.updated_time_var.get(),
                                              'id': self.planer_id_var.get()
                                          })

                        mydb.commit()
                        mydb.close()
                        fetch_date()
                        messagebox.showinfo("Successful", "Data has been Updated Successfully", parent=self.plan_details)

                    except Exception as e:
                        messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.plan_details)

            else:
                pass

        def delete_planner():
            delete = messagebox.askyesno("Delete", "Are you sure You want to Delete this Data?", parent=self.plan_details)
            if delete == 1:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    my_cursor.execute(f"""DELETE FROM planner where Planner_ID = '{self.planer_id_var.get()}'""")

                    mydb.commit()
                    mydb.close()
                    fetch_date()
                    messagebox.showinfo("Delete", "Data has been Deleted", parent=self.plan_details)

                    self.planer_type_var.set("")
                    self.planer_id_var.set("")
                    self.single_room_cost_var.set(0)
                    self.double_room_cost_var.set(0)
                    self.luxury_room_cost_var.set(0)
                    self.delux_room_cost_var.set(0)
                    self.super_delux_room_cost_var.set(0)

                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.plan_details)

            else:
                pass

        def fetch_date():
            mydb = sqlite3.connect("hotel_management_system.db")
            my_cursor = mydb.cursor()

            my_cursor.execute("""SELECT rowid, * FROM planner""")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.Planner_details_table.delete(*self.Planner_details_table.get_children())
                for i in data:
                    self.Planner_details_table.insert("", END, value=i)
                    mydb.commit()
                mydb.close()

        def get_data(event):
            try:
                cursor_row = self.Planner_details_table.focus()
                content = self.Planner_details_table.item(cursor_row)
                content_value = content["values"]

                self.planer_id_var.set(content_value[1])
                self.planer_type_var.set(content_value[2])
                self.single_room_cost_var.set(int(content_value[3]))
                self.double_room_cost_var.set(int(content_value[4]))
                self.luxury_room_cost_var.set(int(content_value[5]))
                self.delux_room_cost_var.set(int(content_value[6]))
                self.super_delux_room_cost_var.set(int(content_value[7]))

            except Exception as e:
                pass

        ##################=================================================== Title Section ============================================================

        title_label = Label(self.plan_details, text="Accommodation Plan Details", font=("Calibre", 20, "bold"), background="black", foreground="gold", border=1, relief=RIDGE)
        title_label.place(x=0, y=0, width=1313, height=50)

        image_logo = Image.open(r"Images\logohotel.png")
        image_logo = image_logo.resize((100, 45), Image.ANTIALIAS)
        self.image_logo = ImageTk.PhotoImage(image_logo)

        image_logo_label = Label(self.plan_details, image=self.image_logo, border=0, relief=RIDGE)
        image_logo_label.place(x=2, y=2, width=100, height=45)

        exit_button = Button(self.plan_details, text="Exit", font=("Calibre", 20, "bold"), background="black", foreground="red", border=0, relief=RIDGE, cursor="hand2", command=self.plan_details.destroy)
        exit_button.place(x=1240, y=5, width=70, height=40)

        ###################=============================================== Label Frame =============================================================

        self.planer_id_var = StringVar()
        self.planer_type_var = StringVar()
        self.single_room_cost_var = IntVar()
        self.double_room_cost_var = IntVar()
        self.luxury_room_cost_var = IntVar()
        self.delux_room_cost_var = IntVar()
        self.super_delux_room_cost_var = IntVar()
        self.updated_date_var = StringVar()
        self.updated_time_var = StringVar()

        _date = datetime.date.today()
        _time = time.strftime("%H:%M:%S", time.localtime())

        self.updated_date_var.set(str(_date))
        self.updated_time_var.set(_time)

        Plans_Details_label_frame = LabelFrame(self.plan_details, text="Accommodation Plans And Details", border=2, relief=RIDGE, padx=2, font=("Calibre", 10))
        Plans_Details_label_frame.place(x=5, y=50, width=425, height=510)

        Plan_type_label = Label(Plans_Details_label_frame, text="Plan Type", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Plan_type_label.grid(row=0, column=0, sticky=W)
        Plan_type_label_combobox = ttk.Combobox(Plans_Details_label_frame, width=20, font=("arial", 12, "bold"), textvariable=self.planer_type_var)
        Plan_type_label_combobox["values"] = ("CP", "EP", "AP", "MAP")
        Plan_type_label_combobox.set("")
        Plan_type_label_combobox.grid(row=0, column=1, sticky=E, padx=4)

        Planer_ID_label = Label(Plans_Details_label_frame, text="Planer ID", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Planer_ID_label.grid(row=1, column=0, sticky=W)
        Planer_ID_label_entry = ttk.Entry(Plans_Details_label_frame, width=22, font=("arial", 12, "bold"), textvariable=self.planer_id_var)
        Planer_ID_label_entry.grid(row=1, column=1, sticky=E, padx=4)

        Single_room_cost_label = Label(Plans_Details_label_frame, text="Single Room Cost", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Single_room_cost_label.grid(row=2, column=0, sticky=W)
        Single_room_cost_label_entry = ttk.Entry(Plans_Details_label_frame, font=("arial", 12), width=22, textvariable=self.single_room_cost_var)
        Single_room_cost_label_entry.grid(row=2, column=1, sticky=E, padx=4)

        Double_room_cost_label = Label(Plans_Details_label_frame, text="Double Room Cost", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Double_room_cost_label.grid(row=3, column=0, sticky=W)
        Double_room_cost_label_entry = ttk.Entry(Plans_Details_label_frame, font=("arial", 12), width=22, textvariable=self.double_room_cost_var)
        Double_room_cost_label_entry.grid(row=3, column=1, sticky=E, padx=4)

        Luxury_room_cost_label = Label(Plans_Details_label_frame, text="Luxury Room Cost", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Luxury_room_cost_label.grid(row=4, column=0, sticky=W)
        Luxury_room_cost_label_entry = ttk.Entry(Plans_Details_label_frame, font=("arial", 12), width=22, textvariable=self.luxury_room_cost_var)
        Luxury_room_cost_label_entry.grid(row=4, column=1, sticky=E, padx=4)

        Delux_room_cost_label = Label(Plans_Details_label_frame, text="Delux Room Cost", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Delux_room_cost_label.grid(row=5, column=0, sticky=W)
        Delux_room_cost_label_enter = ttk.Entry(Plans_Details_label_frame, font=("arial", 12), width=22, textvariable=self.delux_room_cost_var)
        Delux_room_cost_label_enter.grid(row=5, column=1, sticky=E, padx=4)

        Super_Delux_room_cost_label = Label(Plans_Details_label_frame, text="Super Delux Room Cost", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Super_Delux_room_cost_label.grid(row=6, column=0, sticky=W)
        Super_Delux_room_cost_label_entry = ttk.Entry(Plans_Details_label_frame, font=("arial", 12), width=22, textvariable=self.super_delux_room_cost_var)
        Super_Delux_room_cost_label_entry.grid(row=6, column=1, sticky=E, padx=4)

        ############======================================================= Buttons =========================================================================

        Button_Frame = Frame(Plans_Details_label_frame, border=2, relief=RIDGE)
        Button_Frame.place(x=1, y=445, width=414, height=40)

        Add_Button = Button(Button_Frame, text="Add", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=9, cursor="hand2", command=add_planer)
        Add_Button.grid(row=0, column=0, padx=1, pady=2)

        Update_Button = Button(Button_Frame, text="Update", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=11, cursor="hand2", command=update_planner)
        Update_Button.grid(row=0, column=1, padx=1, pady=2)

        Delete_Button = Button(Button_Frame, text="Delete", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, cursor="hand2", command=delete_planner)
        Delete_Button.grid(row=0, column=2, padx=1, pady=2)

        Reset_button = Button(Button_Frame, text="Reset", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, cursor="hand2")
        Reset_button.grid(row=0, column=3, padx=1, pady=2)

        ############============================================================ Right Frame ===================================================================

        Details_and_search_system_frame = LabelFrame(self.plan_details, border=2, relief=RIDGE, text="Details and Search System", font=("Calibre", 10))
        Details_and_search_system_frame.place(x=440, y=50, width=865, height=510)

        Search_by_label = Label(Details_and_search_system_frame, font=("Calibre", 12, "bold"), text="Search By", background="red", foreground="white")
        Search_by_label.grid(row=0, column=0, sticky=W, padx=5)

        Search_by_table_name_combobox = ttk.Combobox(Details_and_search_system_frame, font=("Calibre", 12), width=20, state="readonly")
        Search_by_table_name_combobox["values"] = ("Sex", "Pin Code", "Contact No.", "Reference No.", "Nationality", "ID Proof")
        Search_by_table_name_combobox.set("")
        Search_by_table_name_combobox.grid(row=0, column=1, padx=2)

        Search_by_attribute_combobox = ttk.Combobox(Details_and_search_system_frame, font=("Calibre", 12), width=20)
        Search_by_attribute_combobox["values"] = ("")
        Search_by_attribute_combobox.set("")
        Search_by_attribute_combobox.grid(row=0, column=2, padx=2)

        Search_button = Button(Details_and_search_system_frame, text="Search", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, cursor="hand2")
        Search_button.grid(row=0, column=3, padx=10)

        ShowAll_button = Button(Details_and_search_system_frame, text="Show All", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, cursor="hand2")
        ShowAll_button.grid(row=0, column=4)

        refresh_button = Button(Details_and_search_system_frame, text="Refresh", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, cursor="hand2")
        refresh_button.grid(row=0, column=5, padx=10)

        ######========================================================== Show Data Table ========================================================================

        Date_table_frame = Frame(Details_and_search_system_frame, border=2, relief=RIDGE)
        Date_table_frame.place(x=0, y=40, width=860, height=450)

        scroll_bar_x = ttk.Scrollbar(Date_table_frame, orient=HORIZONTAL)
        scroll_bar_y = ttk.Scrollbar(Date_table_frame, orient=VERTICAL)

        self.Planner_details_table = ttk.Treeview(Date_table_frame, columns=("SlNo", "Planer ID", "Plans", "Single Room Cost", "Double Room Cost", "Luxury Room Cost", "Delux Room Cost", "Super Delux Room Cost", "Latest Update Date", "Latest Update Time"), xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

        scroll_bar_x.config(command=self.Planner_details_table.xview)
        scroll_bar_y.config(command=self.Planner_details_table.yview)

        self.Planner_details_table.heading("SlNo", text="Sl No.", anchor=CENTER)
        self.Planner_details_table.heading("Planer ID", text="Planer ID", anchor=CENTER)
        self.Planner_details_table.heading("Plans", text="Plans", anchor=CENTER)
        self.Planner_details_table.heading("Single Room Cost", text="Single Room Cost", anchor=CENTER)
        self.Planner_details_table.heading("Double Room Cost", text="Double Room Cost", anchor=CENTER)
        self.Planner_details_table.heading("Luxury Room Cost", text="Luxury Room Cost", anchor=CENTER)
        self.Planner_details_table.heading("Delux Room Cost", text="Delux Room Cost", anchor=CENTER)
        self.Planner_details_table.heading("Super Delux Room Cost", text="Super Delux Room Cost", anchor=CENTER)
        self.Planner_details_table.heading("Latest Update Date", text="Latest Update Date", anchor=CENTER)
        self.Planner_details_table.heading("Latest Update Time", text="Latest Update Time", anchor=CENTER)

        self.Planner_details_table["show"] = "headings"

        self.Planner_details_table.column("SlNo", width=40, anchor=CENTER)
        self.Planner_details_table.column("Planer ID", width=100, anchor=CENTER)
        self.Planner_details_table.column("Plans", width=100, anchor=CENTER)
        self.Planner_details_table.column("Single Room Cost", width=120, anchor=CENTER)
        self.Planner_details_table.column("Double Room Cost", width=120, anchor=CENTER)
        self.Planner_details_table.column("Luxury Room Cost", width=120, anchor=CENTER)
        self.Planner_details_table.column("Delux Room Cost", width=120, anchor=CENTER)
        self.Planner_details_table.column("Super Delux Room Cost", width=140, anchor=CENTER)
        self.Planner_details_table.column("Latest Update Date", width=120, anchor=CENTER)
        self.Planner_details_table.column("Latest Update Time", width=120, anchor=CENTER)

        self.Planner_details_table.pack(fill=BOTH, expand=1)
        self.Planner_details_table.bind("<ButtonRelease-1>", get_data)
        fetch_date()


if __name__ == '__main__':
    root = Tk()
    obg = PlanDetailsWindow(root)
    root.mainloop()
