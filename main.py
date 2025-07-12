import smtplib
import schedule
import time
import threading
from flask import Flask
from datetime import datetime

app = Flask(__name__)

# --- EMAIL CONFIG ---
EMAIL_ADDRESS = "rrr.rooprajesh@gmail.com"
EMAIL_PASSWORD = "eptvtiewlflpyrgg"
#TO_EMAIL = "rrr.rooprajesh@gmail.com"
TO_EMAIL = ['rrr.rooprajesh@gmail.com', 'rooprajesh.rrr@gmail.com']


def send_email():
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)            
            #subject = "Automated Email from Replit"
            #body = f"This email was sent at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            date_time = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            subject = f"Automated Email from Replit sent at {date_time}"
            body = f"This email was sent at {date_time} using Replit (similar to AWS or any cloud)"
            msg = f"Subject: {subject}\n\n{body}"
            #server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg)
            for TO_EMAIL_SPLIT in TO_EMAIL:
                server.sendmail(EMAIL_ADDRESS, TO_EMAIL_SPLIT, msg)
            #print("Email sent.")
            print(f"Email sent at {date_time}.")
    except Exception as e:
        print(f"Failed to send email: {e}")


# --- SCHEDULER ---
schedule.every(1).minutes.do(send_email)


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


# --- FLASK SERVER ---
@app.route('/')
def home():
    return "Email Scheduler is Running."


def run_flask():
    app.run(host='0.0.0.0', port=8080)


# --- START BOTH THREADS ---
if __name__ == "__main__":
    threading.Thread(target=run_schedule).start()
    run_flask()
