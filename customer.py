import random
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from babel.numbers import *
from babel.dates import *


class CustomerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Details")
        self.root.geometry("1313x573+232+222")
        self.root.maxsize(1313, 573)
        self.root.minsize(1313, 573)

        ##### Customer Table #####

        mydb = sqlite3.connect("hotel_management_system.db")
        my_cursor = mydb.cursor()

        my_cursor.execute("""CREATE TABLE if not exists customer (
                            Customer_ID	INTEGER UNIQUE,
                            Customer_Name TEXT,
                            Sex	TEXT,
                            Address TEXT,
                            Pin_Code INTEGER,
                            Contact_No INTEGER,
                            eMail TEXT,
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

        ####=============================================================== All Functions =======================================================================

        def Add_data():
            if self.Customer_Name_var.get() == "":
                messagebox.showerror("Error", "Please Enter Name", parent=self.root)

            elif self.Customer_Sex_var.get() == "":
                messagebox.showerror("Error", "Please Enter Sex Type", parent=self.root)

            elif self.Customer_Address_var.get() == "":
                messagebox.showerror("Error", "Please Enter Address", parent=self.root)

            elif self.Customer_Pin_var.get() == "":
                messagebox.showerror("Error", "Please Enter Pin Code", parent=self.root)

            elif self.Customer_contact_no_var.get() == "":
                messagebox.showerror("Error", "Please Enter Contact No", parent=self.root)

            elif self.Customer_email_var.get() == "":
                messagebox.showerror("Error", "Please Enter eMail ID", parent=self.root)

            elif self.Customer_Nationality_var.get() == "":
                messagebox.showerror("Error", "Please Enter Nationality", parent=self.root)

            elif self.Customer_ID_type_var.get() == "":
                messagebox.showerror("Error", "Please Enter I.D. Type", parent=self.root)

            elif self.Customer_ID_proof_No_var.get() == "":
                messagebox.showerror("Error", "Please Enter I.D. No.", parent=self.root)

            else:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    my_cursor.execute(
                        "INSERT INTO customer VALUES (:Customer_ID_label_entry, :Customer_Name_label_entry, :Customer_Sex_label_combobox, :Customer_Address_label_entry, :Customer_PinCode_label_entry, :Customer_ContactNo_label_entry, :Customer_eMail_label_entry, :Customer_Nationality_label_combobox, :Customer_IDProof_label_combobox, :Customer_ID_No_label_entry)",
                        {
                            'Customer_ID_label_entry': self.Customer_ID_var.get(),
                            'Customer_Name_label_entry': self.Customer_Name_var.get(),
                            'Customer_Sex_label_combobox': self.Customer_Sex_var.get(),
                            'Customer_Address_label_entry': self.Customer_Address_var.get(),
                            'Customer_PinCode_label_entry': self.Customer_Pin_var.get(),
                            'Customer_ContactNo_label_entry': self.Customer_contact_no_var.get(),
                            'Customer_eMail_label_entry': self.Customer_email_var.get(),
                            'Customer_Nationality_label_combobox': self.Customer_Nationality_var.get(),
                            'Customer_IDProof_label_combobox': self.Customer_ID_type_var.get(),
                            'Customer_ID_No_label_entry': self.Customer_ID_proof_No_var.get()
                        })
                    mydb.commit()
                    mydb.close()

                    messagebox.showinfo("DataBase", "Customer Data has been saved", parent=self.root)
                    fetch_data()

                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.root)

            self.Customer_ID_var.set(int(x))
            Customer_Name_label_entry.delete(0, END)
            Customer_Sex_label_combobox.set("")
            Customer_Address_label_entry.delete(0, END)
            self.Customer_Pin_var.set(0)
            self.Customer_contact_no_var.set(0)
            Customer_eMail_label_entry.delete(0, END)
            Customer_Nationality_label_combobox.set("")
            Customer_IDProof_label_combobox.set("")
            self.Customer_ID_proof_No_var.set(0)

        def update_data():
            if self.Customer_Name_var.get() == "":
                messagebox.showerror("Error", "Name section is Empty, Please Enter Name", parent=self.root)

            elif self.Customer_Sex_var.get() == "":
                messagebox.showerror("Error", "Sex section is Empty, Please Enter Sex Type", parent=self.root)

            elif self.Customer_Address_var.get() == "":
                messagebox.showerror("Error", "Address section is Empty, Please Enter Address", parent=self.root)

            elif self.Customer_Pin_var.get() == "":
                messagebox.showerror("Error", "Pin Code section is Empty, Please Enter Pin Code", parent=self.root)

            elif self.Customer_contact_no_var.get() == "":
                messagebox.showerror("Error", "Contact No. section is Empty, Please Enter Contact No", parent=self.root)

            elif self.Customer_email_var.get() == "":
                messagebox.showerror("Error", "eMail section is Empty, Please Enter eMail ID", parent=self.root)

            elif self.Customer_Nationality_var.get() == "":
                messagebox.showerror("Error", "Nationality section is Empty, Please Enter Nationality", parent=self.root)

            elif self.Customer_ID_type_var.get() == "":
                messagebox.showerror("Error", "ID Proof section is Empty, Please Enter I.D. Type", parent=self.root)

            elif self.Customer_ID_proof_No_var.get() == "":
                messagebox.showerror("Error", "IN No. section is Empty, Please Enter I.D. No.", parent=self.root)

            else:
                query = messagebox.askyesno("Warning!", "Do you want to update Customer Data?", parent=self.root)
                if query == 1:
                    try:
                        mydb = sqlite3.connect("hotel_management_system.db")
                        my_cursor = mydb.cursor()
                        my_cursor.execute("""UPDATE customer SET
                                        Customer_Name = :name,
                                        Sex = :sex,
                                        Address = :address,
                                        Pin_Code = :pin,
                                        Contact_No = :contact,
                                        eMail= :mail,
                                        Nationality = :nationality,
                                        ID_Type = :id_type,
                                        ID_No = :id_no
                                        
                                        WHERE Customer_ID = :oid""",
                                          {

                                              'name': self.Customer_Name_var.get(),
                                              'sex': self.Customer_Sex_var.get(),
                                              'address': self.Customer_Address_var.get(),
                                              'pin': self.Customer_Pin_var.get(),
                                              'contact': self.Customer_contact_no_var.get(),
                                              'mail': self.Customer_email_var.get(),
                                              'nationality': self.Customer_Nationality_var.get(),
                                              'id_type': self.Customer_ID_type_var.get(),
                                              'id_no': self.Customer_ID_proof_No_var.get(),
                                              'oid': self.Customer_ID_var.get()
                                          })

                        mydb.commit()
                        mydb.close()
                        messagebox.showinfo("Update", "Customer Data has been Updated Successfully", parent=self.root)
                        fetch_data()

                    except Exception as e:
                        messagebox.showerror("Error", f"Something went WRONG {str(e)}", parent=self.root)
                else:
                    pass
            fetch_data()

            x = random.randint(1000, 9000)
            self.Customer_ID_var.set(int(x))
            Customer_Name_label_entry.delete(0, END)
            Customer_Sex_label_combobox.set("")
            Customer_Address_label_entry.delete(0, END)
            self.Customer_Pin_var.set(0)
            self.Customer_contact_no_var.set(0)
            Customer_eMail_label_entry.delete(0, END)
            Customer_Nationality_label_combobox.set("")
            Customer_IDProof_label_combobox.set("")
            self.Customer_ID_proof_No_var.set(0)

        def delete_data():
            delete = messagebox.askyesno("Delete", "Please confirm If you want to Delete it?", parent=self.root)
            if delete == 1:
                try:
                    mydb = sqlite3.connect("hotel_management_system.db")
                    my_cursor = mydb.cursor()

                    my_cursor.execute(f"DELETE FROM customer WHERE Customer_ID={self.Customer_ID_var.get()}")

                    mydb.commit()
                    mydb.close()

                    messagebox.showinfo("Delete", "Customer Data is Deleted", parent=self.root)

                    self.Customer_ID_var.set(int(x))
                    Customer_Name_label_entry.delete(0, END)
                    Customer_Sex_label_combobox.set("")
                    Customer_Address_label_entry.delete(0, END)
                    self.Customer_Pin_var.set(0)
                    self.Customer_contact_no_var.set(0)
                    Customer_eMail_label_entry.delete(0, END)
                    Customer_Nationality_label_combobox.set("")
                    Customer_IDProof_label_combobox.set("")
                    self.Customer_ID_proof_No_var.set(0)

                except Exception as e:
                    messagebox.showerror("Error", f"Something went Wrong{e}")

            else:
                pass
            fetch_data()

        def reset():
            x = random.randint(1000, 9000)
            self.Customer_ID_var.set(int(x))
            self.Customer_Name_var.set("")
            self.Customer_Sex_var.set("")
            self.Customer_Address_var.set("")
            self.Customer_Pin_var.set("")
            self.Customer_contact_no_var.set("")
            self.Customer_email_var.set("")
            self.Customer_Nationality_var.set("")
            self.Customer_ID_type_var.set("")
            self.Customer_ID_proof_No_var.set("")

            fetch_data()

        def fetch_data():
            mydb = sqlite3.connect("hotel_management_system.db")
            my_cursor = mydb.cursor()

            my_cursor.execute("SELECT * FROM customer")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.Customer_details_table.delete(* self.Customer_details_table.get_children())
                for i in data:
                    self.Customer_details_table.insert("", END, value=i)
                mydb.commit()
            mydb.close()

        def get_treeview(event):
            try:
                cursor_row = self.Customer_details_table.focus()
                content = self.Customer_details_table.item(cursor_row)
                content_value = content["values"]

                self.Customer_ID_var.set(int(content_value[0])),
                self.Customer_Name_var.set(content_value[1]),
                self.Customer_Sex_var.set(content_value[2]),
                self.Customer_Address_var.set(content_value[3]),
                self.Customer_Pin_var.set(int(content_value[4])),
                self.Customer_contact_no_var.set(int(content_value[5])),
                self.Customer_email_var.set(content_value[6]),
                self.Customer_Nationality_var.set(content_value[7]),
                self.Customer_ID_type_var.set(content_value[8]),
                self.Customer_ID_proof_No_var.set(int(content_value[9]))

            except Exception as e:
                pass

        def refresh():
            x = random.randint(1000, 9000)
            self.Customer_ID_var.set(int(x))
            Customer_Name_label_entry.delete(0, END)
            Customer_Sex_label_combobox.set("")
            Customer_Address_label_entry.delete(0, END)
            self.Customer_Pin_var.set(0)
            self.Customer_contact_no_var.set(0)
            Customer_eMail_label_entry.delete(0, END)
            Customer_Nationality_label_combobox.set("")
            Customer_IDProof_label_combobox.set("")
            self.Customer_ID_proof_No_var.set(0)
            self.Search_by_table_var.set("")
            Search_by_attribute_combobox["values"] = ("")
            Search_by_attribute_combobox.config(state=NORMAL)
            self.Search_by_attribute_var.set("")

            fetch_data()

        def search():
            mydb = sqlite3.connect("hotel_management_system.db")
            my_cursor = mydb.cursor()

            try:
                if self.Search_by_table_var.get() == "Name":
                    my_cursor.execute(f"SELECT * FROM customer WHERE Customer_Name = {self.Search_by_attribute_var.get()}")
                    print(self.Search_by_attribute_var.get())
                    data = my_cursor.fetchall()
                    if len(data) >= 1:
                        self.Customer_details_table.delete(*self.Customer_details_table.get_children())
                        for i in data:
                            self.Customer_details_table.insert("", END, values=i)
                        mydb.commit()
                    mydb.close()

                elif self.Search_by_table_var.get() == "Contact No.":
                    my_cursor.execute(f"SELECT * FROM customer WHERE Contact_No = {self.Search_by_attribute_var.get()}")
                    data = my_cursor.fetchall()
                    if len(data) >= 1:
                        self.Customer_details_table.delete(*self.Customer_details_table.get_children())
                        for i in data:
                            self.Customer_details_table.insert("", END, values=i)
                        mydb.commit()
                    mydb.close()

                elif self.Search_by_table_var.get() == "Sex":
                    my_cursor.execute(f"SELECT * FROM customer WHERE Sex = '{self.Search_by_attribute_var.get()}'")
                    data = my_cursor.fetchall()
                    if len(data) >= 1:
                        self.Customer_details_table.delete(*self.Customer_details_table.get_children())
                        for i in data:
                            self.Customer_details_table.insert("", END, values=i)

                    else:
                        self.Customer_details_table.delete(*self.Customer_details_table.get_children())
                        mydb.commit()
                    mydb.close()

                elif self.Search_by_table_var.get() == "Reference No.":
                    my_cursor.execute(f"SELECT * FROM customer WHERE Ref_No = {self.Search_by_attribute_var.get()}")
                    data = my_cursor.fetchall()
                    if len(data) != 0:
                        self.Customer_details_table.delete(*self.Customer_details_table.get_children())
                        for i in data:
                            self.Customer_details_table.insert("", END, values=i)
                        mydb.commit()
                    mydb.close()

                elif self.Search_by_table_var.get() == "Nationality":
                    my_cursor.execute(f"SELECT * FROM customer WHERE Nationality = '{self.Search_by_attribute_var.get()}'")
                    data = my_cursor.fetchall()
                    if len(data) != 0:
                        self.Customer_details_table.delete(*self.Customer_details_table.get_children())
                        for i in data:
                            self.Customer_details_table.insert("", END, values=i)

                    else:
                        self.Customer_details_table.delete(*self.Customer_details_table.get_children())
                        mydb.commit()
                    mydb.close()

                elif self.Search_by_table_var.get() == "Pin Code":
                    my_cursor.execute(f"SELECT * FROM customer WHERE Pin_Code = {self.Search_by_attribute_var.get()}")
                    data = my_cursor.fetchall()
                    if len(data) != 0:
                        self.Customer_details_table.delete(*self.Customer_details_table.get_children())
                        for i in data:
                            self.Customer_details_table.insert("", END, values=i)

                    else:
                        self.Customer_details_table.delete(*self.Customer_details_table.get_children())
                        mydb.commit()
                    mydb.close()

                elif self.Search_by_table_var.get() == "ID Proof":
                    my_cursor.execute(f"SELECT * FROM customer WHERE ID_Proof = '{self.Search_by_attribute_var.get()}'")
                    data = my_cursor.fetchall()
                    if len(data) != 0:
                        self.Customer_details_table.delete(*self.Customer_details_table.get_children())
                        for i in data:
                            self.Customer_details_table.insert("", END, values=i)

                    else:
                        self.Customer_details_table.delete(*self.Customer_details_table.get_children())
                        mydb.commit()
                    mydb.close()

                else:
                    messagebox.showwarning("Warning", "Something went Wrong! Please check the Inputs")

            except Exception as e:
                messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.root)
                print(e)

        def search_attribute(event):
            try:
                if self.Search_by_table_var.get() == "Sex":
                    Search_by_attribute_combobox["values"] = ("Male", "Female", "Others")
                    Search_by_attribute_combobox.set("")
                    Search_by_attribute_combobox.config(state="readonly")

                elif self.Search_by_table_var.get() == "Nationality":
                    Search_by_attribute_combobox["values"] = ("India", "Bangladesh", "Nepal", "Bhutan", "Myanmar", "Sri Lanka")
                    Search_by_attribute_combobox.set("")
                    Search_by_attribute_combobox.config(state="readonly")

                elif self.Search_by_table_var.get() == "ID Proof":
                    Search_by_attribute_combobox["values"] = ("Adhaar Card", "Pan Card", "Voter Card", "PassPort", "Driving Licence", "Ration Card")
                    Search_by_attribute_combobox.set("")
                    Search_by_attribute_combobox.config(state="readonly")

                elif self.Search_by_table_var.get() == "Pin Code":
                    Search_by_attribute_combobox["values"] = ("")
                    Search_by_attribute_combobox.set("")
                    Search_by_attribute_combobox.config(state=NORMAL)

                elif self.Search_by_table_var.get() == "Contact No.":
                    Search_by_attribute_combobox["values"] = ("")
                    Search_by_attribute_combobox.set("")
                    Search_by_attribute_combobox.config(state=NORMAL)

                elif self.Search_by_table_var.get() == "Reference No.":
                    Search_by_attribute_combobox["values"] = ("")
                    Search_by_attribute_combobox.set("")
                    Search_by_attribute_combobox.config(state=NORMAL)

                elif self.Search_by_table_var.get() == "Name":
                    Search_by_attribute_combobox["values"] = ("")
                    Search_by_attribute_combobox.set("")
                    Search_by_attribute_combobox.config(state=NORMAL)

            except Exception as e:
                messagebox.showerror("Error", f"Something went Wrong {str(e)}", parent=self.root)

        ##################=================================================== Title Section ============================================================

        title_label = Label(self.root, text="Customer Details", font=("Calibre", 20, "bold"), background="black", foreground="gold", border=1, relief=RIDGE)
        title_label.place(x=0, y=0, width=1313, height=50)

        image_logo = Image.open(r"Images\logohotel.png")
        image_logo = image_logo.resize((100, 45), Image.ANTIALIAS)
        self.image_logo = ImageTk.PhotoImage(image_logo)

        image_logo_label = Label(self.root, image=self.image_logo, border=0, relief=RIDGE)
        image_logo_label.place(x=2, y=2, width=100, height=45)
        
        exit_button = Button(self.root, text="Exit", font=("Calibre", 20, "bold"), background="black", foreground="red", border=0, relief=RIDGE, cursor="hand2", command=self.root.destroy)
        exit_button.place(x=1240, y=5, width=70, height=40)

        ####============================== Variables ============================================

        self.Customer_ID_var = IntVar()
        x = random.randint(1000, 9000)
        self.Customer_ID_var.set(int(x))
        self.Customer_Name_var = StringVar()
        self.Customer_Sex_var = StringVar()
        self.Customer_Address_var = StringVar()
        self.Customer_Pin_var = IntVar()
        self.Customer_contact_no_var = IntVar()
        self.Customer_email_var = StringVar()
        self.Customer_Nationality_var = StringVar()
        self.Customer_ID_type_var = StringVar()
        self.Customer_ID_proof_No_var = IntVar()
        self.Search_by_table_var = StringVar()
        self.Search_by_attribute_var = StringVar()

        ###################=============================================== Label Frame =============================================================

        Customer_Details_label_frame = LabelFrame(self.root, text="Customer Details", border=2, relief=RIDGE, padx=2, font=("Calibre", 10))
        Customer_Details_label_frame.place(x=5, y=50, width=425, height=510)

        Customer_ID_label = Label(Customer_Details_label_frame, text="Ref No", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Customer_ID_label.grid(row=0, column=0, sticky=W)
        Customer_ID_label_entry = ttk.Entry(Customer_Details_label_frame, textvariable=self.Customer_ID_var, width=30, font=("arial", 12), state="readonly")
        Customer_ID_label_entry.grid(row=0, column=1, sticky=E, padx=4)

        Customer_Name_label = Label(Customer_Details_label_frame, text="Customer Name", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Customer_Name_label.grid(row=1, column=0, sticky=W)
        Customer_Name_label_entry = ttk.Entry(Customer_Details_label_frame, textvariable=self.Customer_Name_var, width=30, font=("arial", 12))
        Customer_Name_label_entry.grid(row=1, column=1, sticky=E, padx=4)

        Customer_Sex_label = Label(Customer_Details_label_frame, text="Sex", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Customer_Sex_label.grid(row=2, column=0, sticky=W)
        Customer_Sex_label_combobox = ttk.Combobox(Customer_Details_label_frame, textvariable=self.Customer_Sex_var, width=28, font=("arial", 12), state="readonly")
        Customer_Sex_label_combobox["value"] = ('Male', 'Female', 'Others')
        Customer_Sex_label_combobox.set("")
        Customer_Sex_label_combobox.grid(row=2, column=1, sticky=E, padx=4)

        Customer_Address_label = Label(Customer_Details_label_frame, text="Address", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Customer_Address_label.grid(row=3, column=0, sticky=W)
        Customer_Address_label_entry = ttk.Entry(Customer_Details_label_frame, textvariable=self.Customer_Address_var, width=30, font=("arial", 12))
        Customer_Address_label_entry.grid(row=3, column=1, sticky=E, padx=4)

        Customer_PinCode_label = Label(Customer_Details_label_frame, text="Pin Code", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Customer_PinCode_label.grid(row=4, column=0, sticky=W)
        Customer_PinCode_label_entry = ttk.Entry(Customer_Details_label_frame, textvariable=self.Customer_Pin_var, width=30, font=("arial", 12))
        Customer_PinCode_label_entry.grid(row=4, column=1, sticky=E, padx=4)

        Customer_ContactNo_label = Label(Customer_Details_label_frame, text="Contact No", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Customer_ContactNo_label.grid(row=5, column=0, sticky=W)
        Customer_ContactNo_label_entry = ttk.Entry(Customer_Details_label_frame, textvariable=self.Customer_contact_no_var, width=30, font=("arial", 12))
        Customer_ContactNo_label_entry.grid(row=5, column=1, sticky=E, padx=4)

        Customer_eMail_label = Label(Customer_Details_label_frame, text="Email", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Customer_eMail_label.grid(row=6, column=0, sticky=W)
        Customer_eMail_label_entry = ttk.Entry(Customer_Details_label_frame, textvariable=self.Customer_email_var, width=30, font=("arial", 12))
        Customer_eMail_label_entry.grid(row=6, column=1, sticky=E, padx=4)

        Customer_Nationality_label = Label(Customer_Details_label_frame, text="Nationality", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Customer_Nationality_label.grid(row=7, column=0, sticky=W)
        Customer_Nationality_label_combobox = ttk.Combobox(Customer_Details_label_frame, textvariable=self.Customer_Nationality_var, width=28, font=("arial", 12), state="readonly")
        Customer_Nationality_label_combobox["values"] = ("India", "Bangladesh", "Nepal", "Bhutan", "Myanmar", "Sri Lanka")
        Customer_Nationality_label_combobox.set("")
        Customer_Nationality_label_combobox.grid(row=7, column=1, sticky=E, padx=4)

        Customer_IDProof_label = Label(Customer_Details_label_frame, text="ID Proof", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Customer_IDProof_label.grid(row=8, column=0, sticky=W)
        Customer_IDProof_label_combobox = ttk.Combobox(Customer_Details_label_frame, textvariable=self.Customer_ID_type_var, width=28, font=("arial", 12), state="readonly")
        Customer_IDProof_label_combobox["value"] = ("Adhaar Card", "Pan Card", "Voter Card", "PassPort", "Driving Licence", "Ration Card")
        Customer_IDProof_label_combobox.set("")
        Customer_IDProof_label_combobox.grid(row=8, column=1, sticky=E, padx=4)

        Customer_ID_proof_No_label = Label(Customer_Details_label_frame, text="ID No", font=("Calibre", 12, "bold"), padx=4, pady=8)
        Customer_ID_proof_No_label.grid(row=9, column=0, sticky=W)
        Customer_ID_proof_No_label_entry = ttk.Entry(Customer_Details_label_frame, textvariable=self.Customer_ID_proof_No_var, width=30, font=("arial", 12))
        Customer_ID_proof_No_label_entry.grid(row=9, column=1, sticky=E, padx=4)

        ############======================================================= Buttons =========================================================================

        Button_Frame = Frame(Customer_Details_label_frame, border=2, relief=RIDGE)
        Button_Frame.place(x=3, y=445, width=412, height=40)

        Add_Button = Button(Button_Frame, text="Add", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, command=Add_data, cursor="hand2")
        Add_Button.grid(row=0, column=0, padx=1, pady=2)

        Update_Button = Button(Button_Frame, text="Update", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, command=update_data, cursor="hand2")
        Update_Button.grid(row=0, column=1, padx=1, pady=2)

        Delete_Button = Button(Button_Frame, text="Delete", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, command=delete_data, cursor="hand2")
        Delete_Button.grid(row=0, column=2, padx=1, pady=2)

        Reset_button = Button(Button_Frame, text="Reset", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, command=reset, cursor="hand2")
        Reset_button.grid(row=0, column=3, padx=1, pady=2)

        ############============================================================ Right Frame ===================================================================

        Details_and_search_system_frame = LabelFrame(self.root, border=2, relief=RIDGE, text="Details and Search System", font=("Calibre", 10))
        Details_and_search_system_frame.place(x=440, y=50, width=865, height=510)

        Search_by_label = Label(Details_and_search_system_frame, font=("Calibre", 12, "bold"), text="Search By", background="red", foreground="white")
        Search_by_label.grid(row=0, column=0, sticky=W, padx=5)

        Search_by_table_name_combobox = ttk.Combobox(Details_and_search_system_frame, font=("Calibre", 12), width=20, state="readonly", textvariable=self.Search_by_table_var)
        Search_by_table_name_combobox["values"] = ("Name", "Sex", "Pin Code", "Contact No.", "Reference No.", "Nationality", "ID Proof")
        Search_by_table_name_combobox.set("")
        Search_by_table_name_combobox.bind("<<ComboboxSelected>>", search_attribute)
        Search_by_table_name_combobox.grid(row=0, column=1, padx=2)

        Search_by_attribute_combobox = ttk.Combobox(Details_and_search_system_frame, font=("Calibre", 12), width=20, textvariable=self.Search_by_attribute_var)
        Search_by_attribute_combobox["values"] = ("")
        Search_by_attribute_combobox.set("")
        Search_by_attribute_combobox.grid(row=0, column=2, padx=2)

        Search_button = Button(Details_and_search_system_frame, text="Search", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, command=search, cursor="hand2")
        Search_button.grid(row=0, column=3, padx=10)

        ShowAll_button = Button(Details_and_search_system_frame, text="Show All", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, command=fetch_data, cursor="hand2")
        ShowAll_button.grid(row=0, column=4)

        refresh_button = Button(Details_and_search_system_frame, text="Refresh", font=("Calibre", 11, "bold"), background="black", foreground="gold", width=10, command=refresh, cursor="hand2")
        refresh_button.grid(row=0, column=5, padx=10)

        ######========================================================== Show Data Table ========================================================================

        Date_table_frame = Frame(Details_and_search_system_frame, border=2, relief=RIDGE)
        Date_table_frame.place(x=0, y=40, width=860, height=450)

        scroll_bar_x = ttk.Scrollbar(Date_table_frame, orient=HORIZONTAL)
        scroll_bar_y = ttk.Scrollbar(Date_table_frame, orient=VERTICAL)

        self.Customer_details_table = ttk.Treeview(Date_table_frame, columns=("Customer ID", "Name", "Sex", "Address", "Pin", "Contact", "eMail", "Nationality", "ID Proof", "ID No"), xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

        scroll_bar_x.config(command=self.Customer_details_table.xview)
        scroll_bar_y.config(command=self.Customer_details_table.yview)

        self.Customer_details_table.heading("Customer ID", text="Customer ID", anchor=CENTER)
        self.Customer_details_table.heading("Name", text="Customer Name", anchor=CENTER)
        self.Customer_details_table.heading("Sex", text="Sex", anchor=CENTER)
        self.Customer_details_table.heading("Address", text="Address", anchor=CENTER)
        self.Customer_details_table.heading("Pin", text="Pin Code", anchor=CENTER)
        self.Customer_details_table.heading("Contact", text="Contact No", anchor=CENTER)
        self.Customer_details_table.heading("eMail", text="eMail ID", anchor=CENTER)
        self.Customer_details_table.heading("Nationality", text="Nationality", anchor=CENTER)
        self.Customer_details_table.heading("ID Proof", text="ID Proof", anchor=CENTER)
        self.Customer_details_table.heading("ID No", text="ID No ", anchor=CENTER)

        self.Customer_details_table["show"] = "headings"

        self.Customer_details_table.column("Customer ID", width=80, anchor=CENTER)
        self.Customer_details_table.column("Name", width=120, anchor=CENTER)
        self.Customer_details_table.column("Sex", width=50, anchor=CENTER)
        self.Customer_details_table.column("Address", width=150, anchor=CENTER)
        self.Customer_details_table.column("Pin", width=60, anchor=CENTER)
        self.Customer_details_table.column("Contact", width=70, anchor=CENTER)
        self.Customer_details_table.column("eMail", width=200, anchor=CENTER)
        self.Customer_details_table.column("Nationality", width=50, anchor=CENTER)
        self.Customer_details_table.column("ID Proof", width=80, anchor=CENTER)
        self.Customer_details_table.column("ID No", width=130, anchor=CENTER)

        self.Customer_details_table.pack(fill=BOTH, expand=1)
        self.Customer_details_table.bind("<ButtonRelease-1>", get_treeview)
        fetch_data()


if __name__ == '__main__':
    root = Tk()
    obj = CustomerWindow(root)
    root.mainloop()
