from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import adminhome, employeehome,database

class ViewBillingWindow():

    def __init__(self, isEmployee = False):
        self.isEmployee = isEmployee
        self.root=Tk()

        self.root.geometry('800x400')

        self.root.resizable(True,True)

        self.img = Image.open('images/back.jpg').resize((800, 400))
        self.imgTk = ImageTk.PhotoImage(self.img)
        self.imgLbl = Label(self.root, image = self.imgTk)
        self.imgLbl.place(x = 0, y = 0)

        self.title = Label(self.root, text="Billing",font=('times new roman',20,'bold'),fg='black')
        self.title.pack(side=TOP)

        s = ttk.Style(self.root)
        s.theme_use("clam")

     #s.configure('self.Treeview.heading' , fg='black',font =('times new roman',13,'underline'))

        self.col = ['Name' , 'Phone Number','Date', 'Total Price']
        self.tree = ttk.Treeview(self.root, columns=self.col, show='headings')

        self.tree.heading('Name', text='Name')
        self.tree.heading('Phone Number', text='Phone Number')
        self.tree.heading('Date', text='Date')
        self.tree.heading('Total Price', text='Total Price')
     
        i = 0
        res = database.fetchbill_data()
        for row in res:
          self.tree.insert('',i,text=row[0],values=(row[1],row[2],row[3],row[4]))
        i= i + 1

        self.tree.place(x = 0,y=50)


        self.backbtn = Button(self.root, text = 'Back', bg = 'white',fg='black', font = ('sans-serif', 10, 'bold'),command=self.backButton)
        self.backbtn.place(x = 0, y = 0)

        self.root.mainloop()

    def backButton(self):
        self.root.destroy()
        if self.isEmployee:
            employeehome.EmployeeHomeWindow()
        else:
            adminhome.AdminHomeWindow()


if __name__ == '__main__':
    ViewBillingWindow()