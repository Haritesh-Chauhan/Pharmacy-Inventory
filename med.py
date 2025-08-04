from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import database, adminhome, employeehome
from tkinter import messagebox

class MedicineWindow():
    def __init__(self, isEmployee = False):
     self.isEmployee = isEmployee
     self.root=Tk()

     self.root.geometry('800x400')

     self.root.resizable(True,True)

     self.img = Image.open('images/back.jpg').resize((800, 400))
     self.imgTk = ImageTk.PhotoImage(self.img)
     self.imgLbl = Label(self.root, image = self.imgTk)
     self.imgLbl.place(x = 0, y = 0)

     self.backbtn = Button(self.root, text = 'Back', bg = 'white',fg='black', font = ('sans-serif', 10, 'bold'),command=self.backButton)
     self.backbtn.place(x = 0, y = 0)

     self.title = Label(self.root, text="Medicines Management",font=('times new roman',20,'bold'),fg='black')
     self.title.pack(side=TOP)

     s = ttk.Style(self.root)
     s.theme_use("clam")

     #s.configure('self.Treeview.heading' , fg='black',font =('times new roman',13,'underline'))

     self.col = ['Ref ID' ,'Medicine Name', 'Price', 'Quantity']
     self.tree = ttk.Treeview(self.root, columns=self.col, show='headings')

     self.tree.heading('Ref ID', text='Ref ID')
     self.tree.heading('Medicine Name', text='Medicine Name')
     self.tree.heading('Price', text='Price')
     self.tree.heading('Quantity', text='Quantity')

     i = 0
     res = database.fetch_data()
     for row in res:
        self.tree.insert('',i,text=row[0],values=(row[0],row[1],row[2],row[3]))
        i= i + 1

     self.tree.place(x = 30,y=50)
     
     self.tree.bind('<Double-Button-1>', self.actions)
     self.tree.pack()

     self.root.mainloop()

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
                dels = database.deleteUser1(gup)
                if dels:
                    messagebox.showinfo("Success","Deleted Successfully")
                    self.root.destroy()
                    MedicineWindow()
                else:
                    messagebox.showerror('Alert', 'Something went wrong.')

        if col == '#3':
            # self.root.destroy()
            print('edit is called')

    def backButton(self):
        self.root.destroy()
        if self.isEmployee:
            employeehome.EmployeeHomeWindow()
        else:
            adminhome.AdminHomeWindow()
            
if __name__ == '__main__':
    MedicineWindow()

