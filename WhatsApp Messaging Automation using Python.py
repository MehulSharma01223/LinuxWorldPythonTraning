import pywhatkit
import schedule
import time

# Your Google Form / Website booking link
booking_link = "https://forms.gle/your-google-form-link"   # Replace with your actual link

def send_marketing_message():
    message = f"""
*Habbitt Laundry Management System* 
"""

    # WhatsApp message sending
    pywhatkit.sendwhatmsg_instantly("+917878891296", message)
    print("Marketing message sent successfully!")


# ============ DAILY SCHEDULING ============
schedule.every().day.at("09:00").do(send_marketing_message)

print("Auto-scheduler started... message will be sent daily at 9 AM.")

# Keep program running
while True:
    schedule.run_pending()
    time.sleep(1)
