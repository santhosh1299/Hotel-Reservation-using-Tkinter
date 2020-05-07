from tkinter import *
import sqlite3
import tkinter.messagebox
conn = sqlite3.connect('database.db')
c = conn.cursor()
class Application:
    def __init__(self, master):
        self.master = master
        self.left = Frame(master, width=800, height=720, bg='white')
        self.left.pack(side=LEFT)

       

        
        self.heading = Label(self.left, text="HILTON", font=('c 48 bold'), fg='red', bg='white')
        self.heading.place(x=270, y=0)
        
        self.name = Label(self.left, text="Name", font=(' arial 18 bold'), fg='black', bg='white')
        self.name.place(x=180, y=100)
        self.room = Label(self.left, text="Rooms Required", font=('arial 18 bold'), fg='black', bg='white')
        self.room.place(x=180, y=140)
        self.day = Label(self.left, text="Days", font=('arial 18 bold'), fg='black',bg='white')
        self.day.place(x=180, y=180)
        self.location = Label(self.left, text="Address", font=('arial 18 bold'), fg='black', bg='white')
        self.location.place(x=180, y=220)
        self.mail = Label(self.left, text="E-Mail", font=('arial 18 bold'), fg='black', bg='white')
        self.mail.place(x=180, y=260)
        self.phone = Label(self.left, text="Phone Number", font=('arial 18 bold'), fg='black', bg='white')
        self.phone.place(x=180, y=300)

        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=450, y=100)

        self.room_ent = Entry(self.left, width=30)
        self.room_ent.place(x=450, y=140)
    
        self.day_ent = Entry(self.left, width=30)
        self.day_ent.place(x=450, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=450, y=220)

        self.mail_ent = Entry(self.left, width=30)
        self.mail_ent.place(x=450, y=260)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=450, y=300)
        self.submit = Button(self.left, text=" Submit ", width=17, height=2, bg='red', command=self.college)
        self.submit.place(x=340, y=360)
        
        
       
    def college(self):
        self.val1 = self.name_ent.get()
        self.val2 = self.room_ent.get()
        self.val3 = self.day_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.mail_ent.get()
        self.val6 = self.phone_ent.get()

        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            sql = "INSERT INTO 'hotel' (name, room, day, address, email, phone) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            sql2 = "SELECT ID FROM hotel "
            self.res = c.execute(sql2)
            self.a=[]
            for self.i in self.res:
               self.a.append(self.i)
            tkinter.messagebox.showinfo("Success", "Bookings for " +str(self.val1) + " has been created")
            tkinter.messagebox.showinfo("NOTE","Your Room Number Is " + str (self.a[len(self.a)-1]))
def basic():
 root = Tk()
 b = Application(root)

 root.geometry("800x720+0+0")

 root.resizable(False, False)

 root.mainloop()
basic()           
