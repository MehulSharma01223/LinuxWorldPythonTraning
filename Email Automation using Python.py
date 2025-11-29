import smtplib
import ssl
from email.message import EmailMessage
EMAIL = "mainak.sharma04@gmail.com"
APP_PASSWORD="auru hpse xloa btvo"
RECIVER ="ghanshyamseervi1296@gmail.com"
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECIVER
msg["Subject"]="Hello For PYTHON..."
msg.set_content("This email was shared")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465 ,context=context) as server :
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)
    print("Mail sent")
