from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import database
import adminhome, employeehome

class ProjectWindow:
  def __init__(self):
   self.root = Tk()
 
   self.root.geometry('800x400')  
   self.root.title("Login")
   self.root.resizable(False, True)

   self.frame = Frame(self.root, width=800, height=400)
   self.frame.place(x = 0, y = 0)

   self.img = Image.open('images/loginpage.jpg').resize((800, 400))

   self.imgTk = ImageTk.PhotoImage(self.img)

   self.imgLbl = Label(self.frame, image = self.imgTk)
   self.imgLbl.place(x = 0, y = 0)

   self.firstLbl = Label(self.frame, text = 'Username', bg = '#E5F2F8', font = ('comic sans ms', 14), justify='left')
   self.firstLbl.place(x = 280, y = 100)

   self.firstLbl = Label(self.frame, text = 'Password', bg = '#E5F2F8', font = ('comic sans ms', 14), wraplength=400, justify='center')
   self.firstLbl.place(x = 280, y = 130)

   self.userEntry = Entry(self.frame)
   self.userEntry.place(x = 380, y = 100)

   self.passEntry = Entry(self.frame, show='*')
   self.passEntry.place(x = 380, y = 130)

   self.loginBtn = Button(self.frame, text = 'Login', bg = 'white', font = ('sans-serif', 10, 'bold'),command=self.loginUser)
   self.loginBtn.place(x = 350, y = 180)

   self.root.mainloop()

  def loginUser(self):
  
   if self.userEntry.get().strip() and self.passEntry.get().strip():
     
     if  self.userEntry.get().strip() == 'admin@gmail.com' and self.passEntry.get() == '123456':
      self.root.destroy()
      adminhome.AdminHomeWindow()
     else:

      details = (self.userEntry.get().strip(),self.passEntry.get())
      new = database.loginUser(details)
      if new:
        messagebox.showinfo('Success', 'Login successful.')
        self.root.destroy()
        employeehome.EmployeeHomeWindow()
      else:
        messagebox.showwarning('Alert', 'Error, Something Went Wrong')

if __name__ == '__main__':
 ProjectWindow()