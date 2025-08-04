from tkinter import *
from tkinter import ttk

class BillingWindow():
    def __init__(self):
     self.root=Tk()

     self.root.geometry('800x400')

     self.root.resizable(False , False)

     self.frame = Frame(self.root, width=300, height=380,bd=4,relief='ridge',bg='lightblue')
     self.frame.place(x=10,y=10)

     self.frame1 = Frame(self.root, width=450, height=380,relief='ridge',bd=4,bg='lightblue')
     self.frame1.place(x=340,y=10)

     self.f_lbl = Label(self.frame , text='Patient Info',bg='lightblue', font=('times new roman',20,'bold','underline'))
     self.f_lbl.place(x=80,y=20)

     self.name_lbl = Label(self.frame, text = 'Name:', bg = 'lightblue' ,fg='black', font = ('times new roman', 13))
     self.name_lbl.place(x = 10, y = 70)

     self.email_lbl = Label(self.frame, text = 'Phone Number:', bg = 'lightblue',fg = 'black', font = ('times new roman', 13))
     self.email_lbl.place(x = 10, y = 100)

     self.ph_lbl = Label(self.frame, text = 'Email:', bg = 'lightblue', font = ('times new roman', 13))
     self.ph_lbl.place(x = 10, y = 130)
   
     self.user_lbl = Label(self.frame, text = 'Insurance:', bg = 'lightblue', font = ('times new roman', 13))
     self.user_lbl.place(x = 10, y = 160)
   
     self.pass_Lbl = Label(self.frame, text = 'Gender:', bg = 'lightblue', font = ('times new roman', 13))
     self.pass_Lbl.place(x = 10, y = 190)

     self.pass_Lbl = Label(self.frame, text = 'Address:', bg = 'lightblue', font = ('times new roman', 13))
     self.pass_Lbl.place(x = 10, y = 220)

     self.nameEntry = Entry(self.frame,bg='white',bd=2)
     self.nameEntry.place(x = 130, y = 70)
    
     self.phEntry = Entry(self.frame,bg='white',bd=2)
     self.phEntry.place(x =130, y = 100)

     self.emailEntry = Entry(self.frame,bg='white',bd=2)
     self.emailEntry.place(x =130, y = 130)

     self.emEntry = Entry(self.frame,bg='white',bd=2)
     self.emEntry.place(x =130, y = 160)

     self.genderEntry = ttk.Combobox(self.frame, font=('new times roman',8,'bold'))
     self.genderEntry['values']=('male','female','other')
     self.genderEntry.place(x=130,y=190)

     self.addEntry = Text(self.frame,bg='white',bd=2,width=15,height=4)
     self.addEntry.place(x =130, y = 220)

     #frame1 
     self.f_lbl = Label(self.frame1 , text='Billing Info',bg='lightblue', font=('times new roman',20,'bold','underline'))
     self.f_lbl.place(x=120,y=20)

     self.root.mainloop()

BillingWindow()