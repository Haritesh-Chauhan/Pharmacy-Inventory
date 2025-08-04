from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import database
from tkinter import messagebox
import showMedicinesCart, adminhome, employeehome

class SelectMedicinesForCartWindow():
    def __init__(self, medicineCart=[], isEmployee=False):
        self.isEmployee = isEmployee
        self.selectedMedicine = []
        self.medicineCart = medicineCart
        self.root = Tk()

        self.root.geometry('1100x450')
        self.root.title("Select Medicines")
        self.root.resizable(True, True)

        self.frame = Frame(self.root, bg='white')
        self.frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.backbtn = Button(self.frame, text='Back', bg='#f0f0f0', fg='black', font=('Arial', 10, 'bold'), command=self.backButton)
        self.backbtn.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.col = ['ID', 'Ref ID', 'Medicine Name', 'Price', 'Quantity']
        self.treeView = ttk.Treeview(self.frame, columns=self.col, show='headings')
        for col in self.col:
            self.treeView.heading(col, text=col)
            self.treeView.column(col, anchor=CENTER)
        self.treeView.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        s = ttk.Style(self.frame)
        s.theme_use("clam")

        res = database.fetch_data()
        for i, row in enumerate(res):
            self.treeView.insert('', i, values=(row[0], row[1], row[2], row[3], row[4]))
        self.treeView.bind('<Double-1>', self.actions)

        details_frame = Frame(self.frame, bg='white')
        details_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

        self.create_label(details_frame, 'Medicine:', 0, 0)
        self.medicineLabel = self.create_label(details_frame, '', 0, 1)

        self.create_label(details_frame, 'Max Stock:', 1, 0)
        self.maxStockLabel = self.create_label(details_frame, '0', 1, 1)

        self.create_label(details_frame, 'Stock to Buy:', 2, 0)
        self.stockToBuyLabel = self.create_label(details_frame, '0', 2, 1)

        self.addbtn = Button(details_frame, text='+', bg='#f0f0f0', fg='black', font=('Arial', 10, 'bold'), command=self.addClick)
        self.addbtn.grid(row=2, column=2, padx=5)

        self.minusbtn = Button(details_frame, text='-', bg='#f0f0f0', fg='black', font=('Arial', 10, 'bold'), command=self.minusClick)
        self.minusbtn.grid(row=2, column=3, padx=5)

        self.create_label(details_frame, 'Medicine Price:', 3, 0)
        self.priceLabel = self.create_label(details_frame, '0', 3, 1)

        self.addbtn = Button(details_frame, text='Add', bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'), command=self.addToList)
        self.addbtn.grid(row=4, column=0, columnspan=4, pady=10)

        self.root.mainloop()

    def create_label(self, parent, text, row, col):
        label = Label(parent, text=text, bg='white', fg='black', font=('Arial', 10, 'bold'))
        label.grid(row=row, column=col, padx=10, pady=5, sticky=W)
        return label

    def backButton(self):
        self.root.destroy()
        if len(self.medicineCart) == 0:
            if self.isEmployee:
                employeehome.EmployeeHomeWindow()
            else:
                adminhome.AdminHomeWindow()
        else:
            showMedicinesCart.ShowMedicineCartWindow(self.medicineCart, self.isEmployee)

    def actions(self, e):
        tt = self.treeView.focus()
        itemSelected = self.treeView.item(tt)
        self.selectedMedicine = list(itemSelected.get('values'))
        self.selectedMedicine.append(1) 

        for medicine in self.medicineCart:
            if medicine[0] == self.selectedMedicine[0]:
                res = messagebox.askyesno("Already Added", "Already in Cart, do you want to remove it from cart and add again?")
                if res:
                    self.medicineCart.remove(medicine)
                break

        self.updateLabels()

    def updateLabels(self):
        self.medicineLabel['text'] = self.selectedMedicine[2]
        self.stockToBuyLabel['text'] = self.selectedMedicine[5]
        self.maxStockLabel['text'] = self.selectedMedicine[4]
        self.priceLabel['text'] = self.selectedMedicine[3] * self.selectedMedicine[5]

    def addClick(self):
        if self.selectedMedicine[5] >= self.selectedMedicine[4]:
            messagebox.showerror('Alert', 'Max Limit Reached')
        else:
            self.selectedMedicine[5] += 1
            self.updateLabels()

    def minusClick(self):
        if self.selectedMedicine[5] <= 1:
            messagebox.showerror('Alert', 'Value cannot be 0')
        else:
            self.selectedMedicine[5] -= 1
            self.updateLabels()

    def addToList(self):
        if not self.selectedMedicine:
            messagebox.showerror('Alert', 'Select Medicine to add')
        else:
            self.medicineCart.append(self.selectedMedicine)
            self.root.destroy()
            showMedicinesCart.ShowMedicineCartWindow(self.medicineCart, self.isEmployee)

if __name__ == '__main__':
    SelectMedicinesForCartWindow()
