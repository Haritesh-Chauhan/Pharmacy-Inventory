from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import database
import create
from tkinter import messagebox

class EmployeeWindow():
    def __init__(self):
     self.root=Tk()

     self.root.geometry('800x400')

     self.root.resizable(True,True)

     self.img = Image.open('images/back.jpg').resize((800, 400))
     self.imgTk = ImageTk.PhotoImage(self.img)
     self.imgLbl = Label(self.root, image = self.imgTk)
     self.imgLbl.place(x = 0, y = 0)

     self.title = Label(self.root, text="List Of Employees",font=('times new roman',20,'bold'),fg='black')
     self.title.pack(side=TOP)

     s = ttk.Style(self.root)
     s.theme_use("clam")

     #s.configure('self.Treeview.heading' , fg='black',font =('times new roman',13,'underline'))

     self.col = ['Name' ,'Email', 'Phone Number', 'Username']
     self.tree = ttk.Treeview(self.root, columns=self.col, show='headings')

     self.tree.heading('Name', text='Name')
     self.tree.heading('Email', text='Email')
     self.tree.heading('Phone Number', text='Phone Number')
     self.tree.heading('Username', text='Username')
     
     i = 0
     res = database.fetchnew_data()
     for row in res:
        self.tree.insert('',i,text=row[0],values=(row[0],row[1],row[2],row[3]))
        i= i + 1

     self.tree.place(x = 30,y=50)

     self.insertbtn = Button(self.root, text = 'Add new Employee', bg = 'gray',fg='black', font = ('sans-serif', 10, 'bold'),command=self.page1)
     self.insertbtn.place(x =300, y = 300)
     
     #self.deletebtn = Button(self.root, text = 'Delete', bg = 'gray',fg='black', font = ('sans-serif', 10, 'bold'),command=self.actions)
     #self.deletebtn.place(x = 450, y = 300)

     self.tree.bind('<Double-Button-1>', self.actions)
     self.tree.pack()
     self.root.mainloop()

    def page1(self):
        self.root.destroy()
        create.CreateWindow()

    def actions(self, e):
        print("i am e",e)

        col = self.tree.identify_column(e.x)
        print(f'cols {col}')

        tt = self.tree.focus()
        itemSelected = self.tree.item(tt)
        print(itemSelected)

        gup = (
            self.tree.item(tt).get('text'),
         )

        print("i am gup",gup, col)

        if col == '#4':
            res = messagebox.askyesno("Delete", "Do You Really Want to delete this item.")
            if res:
                dels = database.deleteUser(gup)
                if dels:
                    messagebox.showinfo("Success","Deleted Successfully")
                    self.root.destroy()
                    EmployeeWindow()
                else:
                    messagebox.showerror('Alert', 'Something went wrong.')

        if col == '#3':
            # self.root.destroy()
            print('edit is called')

if __name__ == '__main__':
 EmployeeWindow()