import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, html_content, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the HTML content
        msg.attach(MIMEText(html_content, 'html'))

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection

        # Login to the SMTP server
        server.login(smtp_user, smtp_password)

        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())

        # Disconnect from the server
        server.quit()

        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Usage

subject = "Medine Receipt"

html_content = """
<!DOCTYPE html>
<html lang="en">
<body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
    <div style="max-width: 600px; margin: auto; background: white; padding: 20px; border: 1px solid #ddd;">
        <h2 style="text-align: center; color: #4CAF50;">Pharmacy Name</h2>
        <p style="text-align: center; margin: 0;">Mobile: +1-234-567-8901</p>
        <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">

        <h3 style="color: #333;">Customer Bill Receipt</h3>

        <p><strong>Date:</strong> {{ current_date }}</p>
        <p><strong>Customer Name:</strong> {{ customer_name }}</p>

        <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
            <thead>
                <tr>
                    <th style="border: 1px solid #ddd; padding: 8px; background: #f0f0f0; text-align: left;">Medicine Name</th>
                    <th style="border: 1px solid #ddd; padding: 8px; background: #f0f0f0; text-align: right;">Quantity</th>
                    <th style="border: 1px solid #ddd; padding: 8px; background: #f0f0f0; text-align: right;">Price</th>
                </tr>
            </thead>
            <tbody>
                {{#each medicines}}
                <tr>
                    <td style="border: 1px solid #ddd; padding: 8px;">{{ this.name }}</td>
                    <td style="border: 1px solid #ddd; padding: 8px; text-align: right;">{{ this.quantity }}</td>
                    <td style="border: 1px solid #ddd; padding: 8px; text-align: right;">${{ this.price }}</td>
                </tr>
                {{/each}}
            </tbody>
            <tfoot>
                <tr>
                    <td colspan="2" style="border: 1px solid #ddd; padding: 8px; text-align: right; font-weight: bold;">Total</td>
                    <td style="border: 1px solid #ddd; padding: 8px; text-align: right; font-weight: bold;">${{ total_price }}</td>
                </tr>
            </tfoot>
        </table>

        <p style="margin-top: 20px;">Thank you for your purchase!</p>
        <p style="color: #777; font-size: 12px; text-align: center;">Pharmacy Address | Email: pharmacy@example.com</p>
    </div>
</body>
</html>

"""
to_email = "gurminder7267@gmail.com"
from_email = "testermail038@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Usually 587 for TLS, 465 for SSL
smtp_user = "testermail038@gmail.com"
smtp_password = "  "


if __name__=="__main__":
    send_email(subject, html_content, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password)
