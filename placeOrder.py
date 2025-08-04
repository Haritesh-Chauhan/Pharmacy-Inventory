from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from tkinter import messagebox
import showMedicinesCart, database, receiptScreen

class PlaceOrderWindow:
    def __init__(self, medicineCart=[], isEmployee=False):
        self.isEmployee = isEmployee
        self.medicineCart = medicineCart
        self.root = Tk()

        self.root.geometry('1200x550')
        self.root.title("Place Order")
        self.root.resizable(True, True)

        self.frame = Frame(self.root, bg='white')
        self.frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.backbtn = Button(self.frame, text='Back', bg='#f0f0f0', fg='black', font=('Arial', 10, 'bold'), command=self.backButton)
        self.backbtn.grid(row=0, column=0, sticky=W, padx=10, pady=10)

        self.col = ['ID', 'Ref ID', 'Medicine Name', 'Price', 'Quantity to Buy', "Final Price"]
        self.treeView = ttk.Treeview(self.frame, columns=self.col, show='headings')
        for col in self.col:
            self.treeView.heading(col, text=col)
            self.treeView.column(col, anchor=CENTER, width=120)

        self.treeView.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

        for i, row in enumerate(medicineCart):
            self.treeView.insert('', i, values=(row[0], row[1], row[2], row[3], row[5], row[3] * row[5]))
        self.totalPrice = sum(row[3] * row[5] for row in medicineCart)

        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        details_frame = Frame(self.frame, bg='white')
        details_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

        Label(details_frame, text='Total Price:', bg='white', font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.totalPriceLabel = Label(details_frame, text=f"Rs. {self.totalPrice:.2f}", bg='white', font=('Arial', 12))
        self.totalPriceLabel.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        Label(details_frame, text='Name:', bg='white', font=('Arial', 12, 'bold')).grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.nameEntry = Entry(details_frame, font=('Arial', 12), width=30)
        self.nameEntry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        Label(details_frame, text='Phone No.:', bg='white', font=('Arial', 12, 'bold')).grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.phoneNoEntry = Entry(details_frame, font=('Arial', 12), width=30)
        self.phoneNoEntry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        
        Label(details_frame, text='Email:', bg='white', font=('Arial', 12, 'bold')).grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.emailEntry = Entry(details_frame, font=('Arial', 12), width=30)
        self.emailEntry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        Label(details_frame, text='Order Date:', bg='white', font=('Arial', 12, 'bold')).grid(row=4, column=0, padx=10, pady=5, sticky=W)
        self.orderDateEntry = DateEntry(details_frame, date_pattern='yyyy/mm/dd', font=('Arial', 12))
        self.orderDateEntry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        self.nextbtn = Button(details_frame, text='Next', bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'), command=self.nextClick)
        self.nextbtn.grid(row=5, column=1, padx=10, pady=10, sticky=E)

        self.root.mainloop()

    def backButton(self):
        self.root.destroy()
        showMedicinesCart.ShowMedicineCartWindow(self.medicineCart, self.isEmployee)

    def nextClick(self):
        if self.nameEntry.get().strip() and self.phoneNoEntry.get().strip():
            for medicine in self.medicineCart:
                details = (medicine[4] - medicine[5], medicine[0])
                if not database.updateMedQuantity(details):
                    messagebox.showwarning('Alert', 'Error Occurred')
                    return

            name = self.nameEntry.get().strip()
            phoneNo = self.phoneNoEntry.get().strip()
            date = self.orderDateEntry.get().strip()
            mail= self.emailEntry.get().strip()
            details = (name, phoneNo, date, self.totalPrice)
            if not database.placeOrder(details):
                messagebox.showwarning('Alert', 'Error Occurred')
                return

            self.root.destroy()
            receiptScreen.ReceiptScreenWindow(name, phoneNo,mail, date, self.totalPrice, self.medicineCart, self.isEmployee)
        else:
            messagebox.showwarning('Alert', 'Fill all details')

if __name__ == '__main__':
    PlaceOrderWindow()
