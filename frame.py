from tkinter import *
import database, adminhome
from tkinter import messagebox
import employeehome

class FrameWindow:
   def __init__(self, isEmployee=False):
      self.isEmployee = isEmployee
      self.root = Tk()
      self.root.title("Add New Medicine")

      # Setting the window size and disabling resize
      self.root.geometry('600x400')
      self.root.resizable(False, False)

      # Adding back button
      self.backbtn = Button(self.root, text='Back', bg='white', fg='black', font=('Arial', 10, 'bold'), command=self.backButton)
      self.backbtn.place(x=10, y=10)

      # Creating a main frame
      self.main_frame = Frame(self.root, bg='#f2f2f2', bd=2, relief=RIDGE)
      self.main_frame.place(x=50, y=50, width=500, height=300)

      # Adding a title
      self.title = Label(self.main_frame, text="Add New Medicine", font=('Helvetica', 20, 'bold'), fg='#333', bg='#f2f2f2')
      self.title.pack(side=TOP, pady=20)

      # Creating a form frame inside the main frame
      self.form_frame = Frame(self.main_frame, bg='#f2f2f2')
      self.form_frame.pack(pady=10)

      # Reference ID
      self.ref_lbl = Label(self.form_frame, text='Ref ID:', bg='#f2f2f2', fg='black', font=('Arial', 12, 'bold'))
      self.ref_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)
      self.ide = Entry(self.form_frame, bg='white', font=('Arial', 12))
      self.ide.grid(row=0, column=1, padx=10, pady=5)

      # Name
      self.name_lbl = Label(self.form_frame, text='Name:', bg='#f2f2f2', fg='black', font=('Arial', 12, 'bold'))
      self.name_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)
      self.ide1 = Entry(self.form_frame, bg='white', font=('Arial', 12))
      self.ide1.grid(row=1, column=1, padx=10, pady=5)

      # Price
      self.price_lbl = Label(self.form_frame, text='Price:', bg='#f2f2f2', fg='black', font=('Arial', 12, 'bold'))
      self.price_lbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)
      self.ide2 = Entry(self.form_frame, bg='white', font=('Arial', 12))
      self.ide2.grid(row=2, column=1, padx=10, pady=5)

      # Quantity
      self.quantity_lbl = Label(self.form_frame, text='Quantity:', bg='#f2f2f2', fg='black', font=('Arial', 12, 'bold'))
      self.quantity_lbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)
      self.ide3 = Entry(self.form_frame, bg='white', font=('Arial', 12))
      self.ide3.grid(row=3, column=1, padx=10, pady=5)

      # Submit button
      self.submitbtn = Button(self.main_frame, text='Submit', bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'), command=self.insertdata)
      self.submitbtn.place(x=150, y=250)

      # Cancel button
      self.cancelbtn = Button(self.main_frame, text='Cancel', bg='#f44336', fg='white', font=('Arial', 12, 'bold'), command=self.root.quit)
      self.cancelbtn.place(x=250, y=250)

      self.root.mainloop()

   def insertdata(self):
      if self.ide.get().strip() and self.ide1.get().strip() and self.ide2.get().strip() and self.ide3.get().strip():
         details = (self.ide.get().strip(), self.ide1.get(), self.ide2.get().strip(), self.ide3.get().strip())

         new = database.insertdata(details)
         if new:
            messagebox.showinfo('Success', 'Medicine Added Successfully')
            self.backButton()
         else:
            messagebox.showwarning('Alert', 'Error, Something Went Wrong')
      else:
            messagebox.showwarning('Alert', 'Fill all details')

   def backButton(self):
        self.root.destroy()
        if self.isEmployee:
            employeehome.EmployeeHomeWindow()
        else:
            adminhome.AdminHomeWindow()

if __name__ == '__main__':
   FrameWindow()
