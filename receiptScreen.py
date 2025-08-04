from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import adminhome, employeehome, view_billing
from jinja2 import Template
import mail
from datetime import date
class ReceiptScreenWindow():
    def __init__(self, name, phone,mail, d, totalPrice, medicineCart = [], isEmployee = False):
        self.name = name
        self.phone = phone
        self.date = date
        self.totalPrice = totalPrice
        self.isEmployee = isEmployee
        self.medicineCart = medicineCart
        self.root = Tk()
        self.today=date.today()

        self.root.geometry('600x600')
        self.root.resizable(False, False)
        self.root.title("Receipt")
        self.mail= mail

        self.frame = Frame(self.root, bg='white')
        self.frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        self.backbtn = Button(self.frame, text='Back', bg='white', fg='black', font=('sans-serif', 10, 'bold'), command=self.backButton)
        self.backbtn.grid(row=0, column=0, sticky=W)

        self.saveReceiptBTN = Button(self.frame, text='Save Receipt', bg='white', fg='black', font=('sans-serif', 10, 'bold'), command=self.saveReceipt)
        self.saveReceiptBTN.grid(row=0, column=1, sticky=E)

        self.billReceiptText = self.generateReceiptText()
        self.billReceiptLabel = Label(self.frame, text=self.billReceiptText, bg='white', fg='black', font=('sans-serif', 10), justify=LEFT, anchor=NW)
        self.billReceiptLabel.grid(row=1, column=0, columnspan=2, pady=20)

        self.root.mainloop()

    def generateReceiptText(self):
        billReceiptText = ""
        billReceiptText += "\tSuperMarket\n"
        billReceiptText += "********************************************************\n"
        billReceiptText += "\t supermarket.com\n"
        billReceiptText += "\t Address Dummy\n"
        billReceiptText += "\twww.instagram.com/superMarket\n"
        billReceiptText += "\t 9876543210\n"
        billReceiptText += "********************************************************\n"
        billReceiptText += "****************     Bill     **************************\n"
        billReceiptText += "********************************************************\n"
        billReceiptText += f"\tCustomer Name: {self.name}\n"
        billReceiptText += f"\tCustomer Phone No.: {self.phone}\n"
        billReceiptText += f"\tOrder Date: {self.date}\n"
        billReceiptText += "********************************************************\n"
        billReceiptText += "Medicine\tPrice\tQuantity\tTotal\n"
        billReceiptText += "********************************************************\n"
        
        for medicine in self.medicineCart:
            productname = medicine[2]
            price = medicine[3]
            qty = medicine[5]
            finalPrice = price * qty
            billReceiptText += f"{productname}\t{price}\t{qty}\t{finalPrice}\n"
        
        billReceiptText += "********************************************************\n"
        billReceiptText += f"\tTotal Price: \t{self.totalPrice}\n"
        billReceiptText += "********************************************************\n"
        billReceiptText += "**************       THANK YOU       *******************\n"
        billReceiptText += "****************   COME AGAIN   ************************\n"

        return billReceiptText

    def backButton(self):
        self.root.destroy()
        if self.isEmployee:
            employeehome.EmployeeHomeWindow()
        else:
            adminhome.AdminHomeWindow()

    def saveReceipt(self):
        with open(f"{self.name}_{self.phone}.txt", 'w') as file:
            file.write(self.billReceiptText)
        messagebox.showinfo('Alert', 'Receipt Saved')
        subject = "Medicine Receipt"
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <body style="font-family: Arial, sans-serif; margin: 20px;">
        <div style="max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ccc; border-radius: 5px;">
            <div style="text-align: center; margin-bottom: 20px;">
                <h1 style="margin: 0;">PharmAssist</h1>
                <h4>Near MBD Mall,Jalandhar</h4>
                <h4>+91 9876543210</h4>
            </div>
            <div style="margin-bottom: 20px;">
                <p><strong>Customer Name:</strong> {{ customer_name }}</p>
                <p><strong>Customer Phone:</strong> {{ customer_phone }}</p>
                <p><strong>Date:</strong> {{ dated }}</p>
            </div>
            <div style="margin-bottom: 20px;">
                <h2>Medicines</h2>
                <table style="width: 100%; border-collapse: collapse;">
                    <thead>
                        <tr>
                            <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Medicine Name</th>
                            <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Price</th>
                            <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Quantity</th>
                            <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for medicine in medicines %}
                        <tr>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">{{ medicine.name }}</td>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">{{ medicine.price }}</td>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">{{ medicine.quantity }}</td>
                            <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">{{ medicine.total }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
            <div style="text-align: right;">
                <p><strong>Total Price:</strong> {{ total_price }}</p>
            </div>
        </div>
        </body>
        </html>

        """
        template = Template(html_content)
        
        medicines = []
        for medicine in self.medicineCart:
            productname = medicine[2]
            price = medicine[3]
            qty = medicine[5]
            finalPrice = price * qty
            li= {'name': productname, 'price': price, 'quantity': qty, 'total': finalPrice}
            medicines.append(li)
            # Render the template with variables
        rendered_html = template.render(
                customer_name=self.name,
                customer_phone= self.phone,
                total_price= self.totalPrice,
                dated= self.date,
                medicines= medicines,
                # your_name=your_name,
                # your_contact_information=your_contact_information
            )
        to_email = self.mail
        from_email = "testermail038@gmail.com"
        smtp_server = "smtp.gmail.com"
        smtp_port = 587  # Usually 587 for TLS, 465 for SSL
        smtp_user = "testermail038@gmail.com"
        smtp_password = "oual xlep jfdl pbtw"
        mail.send_email(subject, rendered_html, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password)
        
        

if __name__ == '__main__':
    ReceiptScreenWindow("Name", "Phone", "Date", "123")
