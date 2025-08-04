from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import create,frame, med, selectMedicinesForCart, view_billing, view_employees, login

class AdminHomeWindow:

    def __init__(self):
        self.root=Tk()

        self.root.geometry('800x400')

        self.root.resizable(True,True)

        self.img = Image.open('images/admin1.jpg').resize((800, 400))
        self.imgTk = ImageTk.PhotoImage(self.img)
        self.imgLbl = Label(self.root, image = self.imgTk)
        self.imgLbl.place(x = 0, y = 0)
        
        self.firstLbl = Label(self.root, text = 'ADMIN DASHBOARD', bg = '#5F9EA0',fg='white',font = ('comic sans ms', 20,'bold'), justify='left')
        self.firstLbl.place(x =0, y = 0,relwidth=1,height=70)

        self.logoutBTN = Button(self.root, text = 'Logout', bg = 'white',fg='black', font = ('sans-serif', 10, 'bold'),command=self.logout)
        self.logoutBTN.place(x=0, y = 0)

        self.frame1 = Frame(self.root, bg= '#7AC5CD')
        self.frame1.place(x=70,y=100,width=200,height=100)

        self.insertMedicinesBTN = Button(self.frame1, text = 'Insert Medicine', bg = 'WHITE',fg='black', font = ('sans-serif', 10, 'bold'),command=self.insertMedicines)
        self.insertMedicinesBTN.place(x=45, y =37)

        self.frame2 = Frame(self.root, bg= '#7AC5CD')
        self.frame2.place(x=300,y=100,width=200,height=100)

        self.viewMedicinesBTN = Button(self.frame2, text = 'View Medicines', bg = 'white',fg='black', font = ('sans-serif', 10, 'bold'),command=self.viewMedicines)
        self.viewMedicinesBTN.place(x=45, y = 37)

        self.frame3 = Frame(self.root, bg= '#7AC5CD')
        self.frame3.place(x=530,y=100,width=200,height=100)

        self.createacbtn = Button(self.frame3, text = 'Create Employee Account', bg = 'white',fg='black', font = ('sans-serif', 10, 'bold'),command=self.createEmployee)
        self.createacbtn.place(x = 15, y = 37)

        self.frame4 = Frame(self.root, bg= '#7AC5CD')
        self.frame4.place(x=70,y=230,width=200,height=100)

        self.viewEmployeeBTN = Button(self.frame4, text = 'View Employees', bg = 'white',fg='black', font = ('sans-serif', 10, 'bold'),command=self.viewEmployee)
        self.viewEmployeeBTN.place(x =45, y = 37)

        self.frame5 = Frame(self.root, bg= '#7AC5CD')
        self.frame5.place(x=300,y=230,width=200,height=100)

        self.billingBTN = Button(self.frame5, text = 'Create Billing', bg = 'white',fg='black', font = ('sans-serif', 10, 'bold'),command=self.createBilling)
        self.billingBTN.place(x = 45, y = 37)

        self.frame6 = Frame(self.root, bg= '#7AC5CD')
        self.frame6.place(x=530,y=230,width=200,height=100)

        self.viewBillingBTN = Button(self.frame6, text = 'View Billing', bg = 'white',fg='black', font = ('sans-serif', 10, 'bold'),command=self.viewBilling)
        self.viewBillingBTN.place(x =45, y = 37)
        
        self.root.mainloop()

    def insertMedicines(self):
        self.root.destroy()
        frame.FrameWindow()

    def viewMedicines(self):
        self.root.destroy()
        med.MedicineWindow()

    def createEmployee(self):
        self.root.destroy()
        create.CreateWindow()

    def viewEmployee(self):
        self.root.destroy()
        view_employees.ViewEmployeesWindow()

    def createBilling(self):
        self.root.destroy()
        selectMedicinesForCart.SelectMedicinesForCartWindow(medicineCart=[], isEmployee=False)

    def viewBilling(self):
        self.root.destroy()
        view_billing.ViewBillingWindow()

    def logout(self):
        res = messagebox.askyesno("Logout?", "Do You Really Want to logout from this account?")
        if res:
            self.root.destroy()
            login.ProjectWindow()


if __name__ == '__main__':
    AdminHomeWindow()