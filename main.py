import smtplib
import openpyxl
from email.message import EmailMessage
from dotenv import load_dotenv
from datetime import datetime
from jinja2 import Template
import json
import argparse
import os




LOG_FILE = "logs/log.json"

def log_result(name, email, status, error_message=None):
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "name": name,
        "email": email,
        "status": status
    }
    if error_message:
        log_entry["error_message"] = error_message

    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")

def send_emails(file_path = "data/sample.pdf", template_path="templates/template.html"):
    load_dotenv()
    EMAIL_USER = os.getenv('EMAIL_USER')
    EMAIL_PASS = os.getenv('EMAIL_PASS')

    wb = openpyxl.load_workbook('data/recipients.xlsx')
    sheet = wb.active

    file_name = os.path.basename(file_path)

    # Load HTML template
    with open(template_path, "r") as f:
        template = Template(f.read())

    print(f"Sending emails using file: {file_path} and template: {template_path}")
    for row in sheet.iter_rows(min_row=2, values_only=True):
        name, email = row
        msg = EmailMessage()
        msg['Subject'] = 'Hello from Python'
        msg['From'] = EMAIL_USER
        msg['To'] = email
        html_content = template.render(
            name=name,
            link="https://www.example.com",
            date=datetime.now().strftime("%Y-%m-%d %H:%M")
        )
        msg.set_content(f"Hi {name}, this is a plain text fallback.")
        msg.add_alternative(html_content, subtype='html')
        
        with open(file_path,"rb") as f:
            file_data = f.read()
            file_type = file_name.split(".")[-1]

            msg.add_attachment(file_data,maintype="application", subtype=file_type, filename=file_name)


        try:
            # Connect to Gmail SMTP server and send email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_USER, EMAIL_PASS)
                smtp.send_message(msg)
            log_result(name, email, "success")
            print(f"Email to {email} sent and logged.")

        except Exception as e:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_message = str(e)
            log_result(name, email, "error", error_message)
            print(f'Failed to send email to {email}: {e}')

def show_log():
    print(f"Reading logs from {LOG_FILE}:")
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                print("Log file is empty.")
                return
            for line in lines:
                entry = json.loads(line)
                print(f"{entry['timestamp']} | {entry['name']} | {entry['email']} | Status: {entry['status']}")
                if entry.get("error_message"):
                    print(f"  Error: {entry['error_message']}")
    except FileNotFoundError:
        print("Log file not found.")


def main():
    parser = argparse.ArgumentParser(description="Email Automation Tool")
    parser.add_argument("--send", action="store_true", help="Run email sending")
    parser.add_argument("--log", action="store_true", help="Show email sending logs")
    parser.add_argument("--file", type=str, help="Path to Excel file with emails")
    parser.add_argument("--template", type=str, help="Path to HTML email template")

    args = parser.parse_args()

    if args.send:
        send_emails(file_path=args.file, template_path=args.template)
    elif args.log:
        show_log()
    else:
        print("Use --help to see available commands")

if __name__ == "__main__":
    main()
