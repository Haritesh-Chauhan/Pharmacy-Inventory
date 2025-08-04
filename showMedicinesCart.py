from tkinter import *
from tkinter import ttk
import database
from tkinter import messagebox
import placeOrder, selectMedicinesForCart, adminhome, employeehome

class ShowMedicineCartWindow:
    def __init__(self, medicineCart=[], isEmployee=False):
        self.isEmployee = isEmployee
        self.medicineCart = medicineCart
        self.root = Tk()

        self.root.geometry('1200x400')
        self.root.title("Medicine Cart")
        self.root.resizable(True, True)

        self.frame = Frame(self.root, bg='white')
        self.frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        s = ttk.Style(self.frame)
        s.theme_use("clam")

        self.backbtn = Button(self.frame, text='Back', bg='#f0f0f0', fg='black', font=('Arial', 10, 'bold'), command=self.backButton)
        self.backbtn.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.col = ['ID', 'Ref ID', 'Medicine Name', 'Price', 'Quantity to Buy', "Delete"]
        self.treeView = ttk.Treeview(self.frame, columns=self.col, show='headings')
        for col in self.col:
            self.treeView.heading(col, text=col)
            self.treeView.column(col, anchor=CENTER,width=120)
        self.treeView.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

        for i, row in enumerate(medicineCart):
            self.treeView.insert('', i, values=(row[0], row[1], row[2], row[3], row[5], 'Delete'))
        self.totalPrice = sum(row[3] * row[5] for row in medicineCart)

        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.treeView.bind('<Double-1>', self.actions)

        details_frame = Frame(self.frame, bg='white')
        details_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

        Label(details_frame, text='Total Price:', bg='white', font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.totalPriceLabel = Label(details_frame, text=f"Rs. {self.totalPrice:.2f}", bg='white', font=('Arial', 12))
        self.totalPriceLabel.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        self.addbtn = Button(details_frame, text='Add More Medicines', bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'), command=self.addMoreMedicines)
        self.addbtn.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.nextbtn = Button(details_frame, text='Next', bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'), command=self.nextClick)
        self.nextbtn.grid(row=1, column=1, padx=10, pady=10, sticky=E)

        self.root.mainloop()

    def backButton(self):
        self.root.destroy()
        if self.isEmployee:
            employeehome.EmployeeHomeWindow()
        else:
            adminhome.AdminHomeWindow()

    def actions(self, e):
        tt = self.treeView.focus()
        itemSelected = self.treeView.item(tt)
        selectedMedicine = list(itemSelected.get('values'))

        # to get col which is clicked, i.e. edit or delete
        col = self.treeView.identify_column(e.x)

        if col == '#6':
            res = messagebox.askyesno("Delete", "Do you really want to delete this item?")
            if res:
                for medicine in self.medicineCart:
                    if medicine[0] == selectedMedicine[0]:
                        self.medicineCart.remove(medicine)
                self.root.destroy()
                ShowMedicineCartWindow(self.medicineCart, self.isEmployee)

    def addMoreMedicines(self):
        self.root.destroy()
        selectMedicinesForCart.SelectMedicinesForCartWindow(self.medicineCart, self.isEmployee)

    def nextClick(self):
        if len(self.medicineCart) == 0:
            messagebox.showerror('Alert', 'Select Medicine to place order')
        else:
            self.root.destroy()
            placeOrder.PlaceOrderWindow(self.medicineCart, self.isEmployee)

if __name__ == '__main__':
    ShowMedicineCartWindow()
