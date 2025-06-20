import schedule
import time
from main import send_emails

schedule.every().day.at("9:00").do(send_emails)

print("🕒 Scheduler is running. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)
