from tkinter import *
from PIL import Image, ImageTk
from customer import CustomerWindow
from rooms_booking import RoomBooking
from room_details import RoomDetailsWindow
from bill_details import BillWindow
from plan_details import PlanDetailsWindow
import time
import datetime
from babel.numbers import *
from babel.dates import *


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        self.root.maxsize(1550, 800)
        self.root.minsize(1550, 800)

        def customer_details():
            self.Customer_Window = Toplevel(self.root)
            self.app = CustomerWindow(self.Customer_Window)

        def room_data():
            self.Room_Window = Toplevel(self.root)
            self.app = RoomBooking(self.Room_Window)

        def room_details():
            self.Room_Details_Window = Toplevel(self.root)
            self.app = RoomDetailsWindow(self.Room_Details_Window)

        def bill_details():
            self.Bill_Details_Window = Toplevel(self.root)
            self.app = BillWindow(self.Bill_Details_Window)

        def planner_details():
            self.Planner_Details_Windows = Toplevel(self.root)
            self.app = PlanDetailsWindow(self.Planner_Details_Windows)

        ###===========================================Top Image==============================================

        image1 = Image.open(r"Images\hotel1.png")
        image1 = image1.resize((1550, 140), Image.ANTIALIAS)
        self.photo_image_1 = ImageTk.PhotoImage(image1)

        Image_Label = Label(self.root, image=self.photo_image_1, borderwidth=3, relief=RIDGE)
        Image_Label.place(x=0, y=0, width=1550, height=140)

        ###========================================================Top Logo============================================================

        image_2 = Image.open(r"Images\logohotel.png")
        image_2 = image_2.resize((230, 140), Image.ANTIALIAS)
        self.photo_image_logo_2 = ImageTk.PhotoImage(image_2)

        Image_logo_Label = Label(self.root, image=self.photo_image_logo_2, borderwidth=3, relief=RIDGE)
        Image_logo_Label.place(x=0, y=0, width=230, height=140)

        ##############================================================================= Title ===============================================================================

        Title_Label = Label(self.root, text="Hotel Management System", font=("Calibre", 30, "bold"), background="black", foreground="gold", border=4, relief=RIDGE)
        Title_Label.place(x=0, y=140, width=1550, height=50)

        exit_button = Button(self.root, text="Exit", font=("Calibre", 20, "bold"), background="black", foreground="red", border=0, relief=RIDGE, cursor="hand2", command=self.root.destroy)
        exit_button.place(x=1470, y=145, width=70, height=40)

        ##################===========================================================Main Frame============================================================================

        main_frame = Frame(self.root, border=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        ###=================================================MENU LABEL=================================================

        Manu_label = Label(main_frame, text="MENU", font=("Calibre", 20, "bold"), background="black", foreground="gold", border=4, relief=RIDGE)
        Manu_label.place(x=0, y=0, width=230)

        #####=======================================================Button Frame==================================================================

        button_frame = Frame(main_frame, border=4, relief=RIDGE, cursor="hand2")
        button_frame.place(x=0, y=40, width=230, height=190)

        room_details_button = Button(button_frame, text="Room Details", font=("Calibre", 14, "bold"), background="black", foreground="gold", border=0, width=18, cursor="hand2", command=room_details)
        room_details_button.grid(row=0, column=0, pady=1)

        accommodation_plan_button = Button(button_frame, text="Plan Details", font=("Calibre", 14, "bold"), background="black", foreground="gold", border=0, width=18, cursor="hand2", command=planner_details)
        accommodation_plan_button.grid(row=1, column=0, pady=1)

        customer_button = Button(button_frame, text="Customer Data", font=("Calibre", 14, "bold"), background="black", foreground="gold", border=0, width=18, cursor="hand2", command=customer_details)
        customer_button.grid(row=2, column=0, pady=1)

        room_booking_button = Button(button_frame, text="Room Booking", font=("Calibre", 14, "bold"), background="black", foreground="gold", border=0, width=18, cursor="hand2", command=room_data)
        room_booking_button.grid(row=3, column=0, pady=1)

        bill_details_button = Button(button_frame, text="Bill Details", font=("Calibre", 14, "bold"), background="black", foreground="gold", border=0, width=18, cursor="hand2", command=bill_details)
        bill_details_button.grid(row=4, column=0, pady=1)



        '''
        logout_button = Button(button_frame, text="LogOut", font=("Calibre", 14, "bold"), background="black", foreground="gold", border=0, width=18, cursor="hand2")
        logout_button.grid(row=4, column=0, pady=1)'''

        #################=====================================================MAIN FRAME IMAGE===========================================================================

        image_3 = Image.open(r"Images\silde3.png")
        image_3 = image_3.resize((1320, 605), Image.ANTIALIAS)
        self.Main_Frame_Image = ImageTk.PhotoImage(image_3)

        Main_Frame_Image_label = Label(main_frame, image=self.Main_Frame_Image, border=4, relief=RIDGE)
        Main_Frame_Image_label.place(x=225, y=0, width=1320, height=605)

        ##########################================================================================ Image on Bottom Of Main FRAME====================================================

        image_4 = Image.open(r"Images\myh.png")
        image_4 = image_4.resize((230, 190), Image.ANTIALIAS)
        self.Image_on_bottom_of_Main_1_Frame = ImageTk.PhotoImage(image_4)

        Image_on_bottom_of_Main_Frame_1_label = Label(main_frame, image=self.Image_on_bottom_of_Main_1_Frame, border=4,
                                                      relief=RIDGE)
        Image_on_bottom_of_Main_Frame_1_label.place(x=0, y=225, width=230, height=190)

        image_5 = Image.open(r"Images\khana.png")
        image_5 = image_5.resize((230, 190), Image.ANTIALIAS)
        self.Image_on_bottom_of_Main_2_Frame = ImageTk.PhotoImage(image_5)

        Image_on_bottom_of_Main_Frame_2_label = Label(main_frame, image=self.Image_on_bottom_of_Main_2_Frame, border=4,
                                                      relief=RIDGE)
        Image_on_bottom_of_Main_Frame_2_label.place(x=0, y=415, width=230, height=190)


if __name__ == '__main__':
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
