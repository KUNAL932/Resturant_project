import tkinter as tk
from tkinter import font
from tkinter import *
import tkinter.messagebox as tm
import sqlite3
import random
from tkinter import ttk
root=tk.Tk()
root.title("menu")

###########----------------------------sqlite3 database-------------------------------------------------------------------

conn=sqlite3.connect('resturant.db')
table_name="table_name"
table_id="table_id"
rice_meal="rice_meal"
daal_meal="daal_meal"
plain_roti="plain_roti"
tandoori_roti="tandoori_roti"
totl_price="totl_price"

pricing_all_items="pricing_all_items"
conn.execute("CREATE TABLE IF NOT EXISTS "+table_name+"( "+table_id+"  INTEGER PRIMARY KEY AUTOINCREMENT,"
             +rice_meal+" INTEGER,"+daal_meal+" INTEGER,"+plain_roti+" INTEGER,"+tandoori_roti+" INTEGER ); ")
print("table created")


#----------------------------labels----------------------------------------------------------------------


appHighlightFont = font.Font(family='Helvetica', size=12, weight='bold')
displayLabel=tk.Label(root,text="Rawat Resturant",bg="#ffff99",fg="#8B0000",font="Times")
displayLabel.grid(row=0,column=0,columnspan="2")

menu_1=tk.Label(root,text="Rice",fg="#ff8000")
menu_1.grid(row=1,column=0)

price_1=tk.Label(root,text="50",fg="#ff8000").grid(row=1,column=1)

menu_2=tk.Label(root,text="Daal",fg="#ff8000").grid(row=2,column=0)
price_2=tk.Label(root,text="70",fg="#ff8000").grid(row=2,column=1)

menu_3=tk.Label(root,text="Plain Roti",fg="#ff8000").grid(row=3,column=0)
price_3=tk.Label(root,text="5",fg="#ff8000").grid(row=3,column=1)


menu_4=tk.Label(root,text="Tandoori Roti",fg="#ff8000").grid(row=4,column=0)
price_4=tk.Label(root,text="10",fg="#ff8000").grid(row=4,column=1)


show_details_history=tk.Button(root,text="Show Details",fg="#00CC00",width="15",command=lambda:newWindow()).grid(row=5,column=0)
place_order_button=tk.Button(root,text="Place Order",fg="#00CC00",width="15",command=lambda :Place_order_delete_window()).grid(row=5,column=1)
#-------------------------------functions to be used in buttons for new window-------------------------
def newWindow():

    root.destroy()
    class LoginFrame(Frame):

        def __init__(self, master):
            super().__init__(master)

            self.loginNamelabel = tk.Label(self, text="Name")
            self.passwordlabel = Label(self, text="password")

            self.loginEntry = Entry(self, width="10")
            self.passwordEntry = Entry( self,width="10", show="*")

            self.loginNamelabel.grid(row=1, column=0)
            self.passwordlabel.grid(row=2, column=0)
            self.loginEntry.grid(row=1, column=1)
            self.passwordEntry.grid(row=2, column=1)

            self.checkbox = Checkbutton(self, text="Keep me logged in")
            self.checkbox.grid(row=5, column=0)

            self.logbtn = Button(self, text="Login", command=lambda :self.btn_clicked())
            self.logbtn.grid(row=6, column=0)
            self.pack()

        def btn_clicked(self):
            # print("Clicked")
            username = self.loginEntry.get()
            password = self.passwordEntry.get()

            # print(username, password)

            if username == "kunal" and password == "password":
                tm.showinfo("Login info", "Welcome")
            else:
                tm.showerror("Login error", "Incorrect username")
    root3=tk.Tk()

    lf = LoginFrame(root3)

    root3.mainloop()

price_01=0
price_02=0
price_03=0
price_04=0


def Place_order_delete_window():
    root.destroy()
    global price_01,price_02,price_03,price_04


    root2=tk.Tk()

    root2.title("Order")

    # click_button=StringVar()

    menu_01=tk.Label(root2,text="Rice",fg="#00CC00").grid(row=1,column=0)
    price_01=tk.Entry(root2,width="5")
    price_01.grid(row=1,column=1)

    menu_02=tk.Label(root2,text="Daal",fg="#00CC00").grid(row=2,column=0)
    price_02=tk.Entry(root2,width="5")
    price_02.grid(row=2,column=1)


    menu_03=tk.Label(root2,text="Plain Roti",fg="#00CC00").grid(row=3,column=0)
    price_03=tk.Entry(root2,width="5")
    price_03.grid(row=3,column=1)
    takeinputButton = tk.Button(root2, text="Take Input", fg="#800080", command=lambda: takeInput()).grid(row=5,
                                                                                                          column=1)

    menu_04=tk.Label(root2,text="Tandoori Roti",fg="#00CC00").grid(row=4,column=0)
    price_04=tk.Entry(root2,width="5")
    price_04.grid(row=4,column=1)
    input1=0
    input2=0
    input3=0
    input4=0
    def takeInput():
        global input1, input2, input3, input4
        input1=int(price_01.get())
        input2=int(price_02.get())
        input3=int(price_03.get())
        input4=int(price_04.get())

        conn.execute(" INSERT INTO " + table_name + "(" + rice_meal + "," + daal_meal + ",\
                     " + plain_roti + "," + tandoori_roti + " )VALUES\
                     (" +str(input1) + "," + str(input2) + "," + str(input3) + "," + str(input4) + ");  ")
        conn.commit()
        print("values entered")




    def Reset():
        global  price_01,price_02,price_03,price_04
        price_01.delete(0, "end")
        price_02.delete(0, 'end')
        price_03.delete(0, 'end')
        price_04.delete(0, 'end')
        pricing_entry.delete(0,'end')
        total_items_entry.delete(0,'end')


    resetButton=tk.Button(root2,text="Reset",width="12",fg="#800080",command=lambda :Reset()).grid(row=5,column=0)
    total_items_show=tk.Button(root2,text="Total Item",fg="#800080",width="12",command=lambda :adding_value_to_price()).grid(row=6,column=0)
    total_items_entry=tk.Entry(root2,width="5")
    total_items_entry.grid(row=6,column=1)
    # operator=""
    def adding_value_to_price():
        global input1,input2,input3,input4
        add_entry=int(input1) + int(input2) + int(input3) + int(input4)
        total_items_entry.insert(0, add_entry)

    def total_price_fuction():
        global input1,input2,input3,input4
        price_add_1=(input1*50)
        price_add_2=(input2*70)
        price_add_3=(input3*5)
        price_add_4=(input4*10)
        pricing_all_items=int(price_add_1) + int(price_add_2) + int(price_add_3) + int(price_add_4)
        pricing_entry.insert(0,pricing_all_items)
    #
    # def btn_click(number):
    #     global operator
    #     operator=operator+str(number)
    #     click_button.set(operator)
    total_price_label=tk.Button(root2,text="Total Price",width="12",fg="#800080",command= lambda :total_price_fuction())
    total_price_label.grid(row=7,column=0)
    pricing_entry=tk.Entry(root2,width="5")
    pricing_entry.grid(row=7,column=1)
    # new=tk.Entry(root2, textvariable=click_button,width="5")
    # new.grid(row=8,column=1)
    # newButton=tk.Button(root2,text="7",command=lambda :btn_click(7))
    # newButton.grid(row=8,column=0)

    print_Button=tk.Button(root2,text="PRINT",width="12",command= lambda :print_screen() )
    print_Button.grid(row=8,column=1)

    def print_screen():
        root2.destroy()

        root4=tk.Tk()
        root4.title('database')
        tree=ttk.Treeview(root4)
        tree['column']=(1,2,3,4)
        tree.heading(1,text="rice")
        tree.heading(2,text="daal")
        tree.heading(3,text="Roti")
        tree.heading(4,text="tandoori Roti")
        cursor=conn.execute("SELECT * FROM "+table_name+";")
        i=0
        for row in cursor:
            tree.insert('',i, text=str(".") + str(row[0]), values= \
                (row[1], row[2], row[3], row[4]))
            i=i+1
        tree.pack()

        root4.mainloop()



    root2.mainloop()





root.mainloop()