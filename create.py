from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import database
import adminhome, employeehome
import view_employees

class CreateWindow():
  def __init__(self, isEmployee = False):
   self.isEmployee = isEmployee
   self.root = Tk()
 
   self.root.geometry('800x400')

   self.root.resizable(False, False)

   self.frame = Frame(self.root, width=800, height=400)
   self.frame.place(x = 0, y = 0)

   self.img = Image.open('images/back.jpg').resize((800, 400))
   self.imgTk = ImageTk.PhotoImage(self.img)
   self.imgLbl = Label(self.frame, image = self.imgTk)
   self.imgLbl.place(x = 200, y = 0)

   self.img1 = Image.open('images/img1.jpg').resize((300, 300))
   self.img1Tk = ImageTk.PhotoImage(self.img1)
   self.img1Lbl = Label(self.frame, image = self.img1Tk)
   self.img1Lbl.place(x = 60, y = 50)

   self.frame1 = Frame(self.root,width = 350 , height=300 ,bg='white' )
   self.frame1.place(x=360 , y= 50)

   self.firstLbl = Label(self.frame1, text = 'Create Employee Account', bg = 'white', font = ('times new roman', 20,'bold'))
   self.firstLbl.place(x = 30, y = 30)

   self.name_lbl = Label(self.frame1, text = 'Name:', bg = 'white' ,fg='black', font = ('times new roman', 12))
   self.name_lbl.place(x = 30, y = 80)

   self.email_lbl = Label(self.frame1, text = 'Email:', bg = 'white',fg = 'black', font = ('times new roman', 12))
   self.email_lbl.place(x = 30, y = 110)

   self.ph_lbl = Label(self.frame1, text = 'Phone number:', bg = 'white', font = ('times new roman', 12), justify='left')
   self.ph_lbl.place(x = 30, y = 140)
   
   self.user_lbl = Label(self.frame1, text = 'Username:', bg = 'white', font = ('times new roman', 12), justify='left')
   self.user_lbl.place(x = 30, y = 170)
   
   self.pass_Lbl = Label(self.frame1, text = 'Password:', bg = 'white', font = ('times new roman', 12), justify='left')
   self.pass_Lbl.place(x = 30, y = 200)

   self.nameEntry = Entry(self.frame1,bg='white')
   self.nameEntry.place(x = 130, y = 80)

   self.emailEntry = Entry(self.frame1,bg='white')
   self.emailEntry.place(x =130, y = 110)

   self.phEntry = Entry(self.frame1,bg='white')
   self.phEntry.place(x =130, y = 140)

   self.userEntry = Entry(self.frame1,bg='white')
   self.userEntry.place(x =130, y = 170)

   self.passEntry = Entry(self.frame1,bg='white',show='*')
   self.passEntry.place(x =130, y = 200)

   self.registerbtn = Button(self.frame1, text = 'Register', bg = 'white',fg='black', font = ('sans-serif', 10, 'bold'),command=self.registerUser)
   self.registerbtn.place(x = 130, y = 230)

  #  self.viewbtn = Button(self.frame1, text = 'View Employee', bg = 'white',fg='black', font = ('sans-serif', 10, 'bold'),command=self.nextpage)
  #  self.viewbtn.place(x = 160, y = 265)

   self.backbtn = Button(self.frame1, text = 'Back', bg = 'white',fg='black', font = ('sans-serif', 10, 'bold'),command=self.backLogin)
   self.backbtn.place(x = 220, y = 230)

   self.root.mainloop()

  def registerUser(self):
   if self.nameEntry.get().strip() and self.emailEntry.get() and self.phEntry.get().strip() and self.userEntry.get().strip() and self.passEntry.get().strip():
     details = (self.nameEntry.get().strip(),self.emailEntry.get(), self.phEntry.get().strip(),self.userEntry.get().strip(),self.passEntry.get().strip())
           
     new = database.registerUser(details)
     if new:
      messagebox.showinfo('Success', 'Registration is successful.')
     else:
      messagebox.showwarning('Alert', 'Error, Something Went Wrong')

  def backLogin(self):
        self.root.destroy()
        if self.isEmployee:
            employeehome.EmployeeHomeWindow()
        else:
            adminhome.AdminHomeWindow()
  
  def nextpage(self):
        self.root.destroy()
        view_employees.ViewEmployeesWindow()

if __name__ == '__main__':
 CreateWindow()