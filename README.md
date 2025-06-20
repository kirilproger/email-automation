# 📧 Email Automation Tool (Python)

A powerful yet simple Python tool for sending HTML email campaigns using data from Excel, with optional attachments and automated scheduling.

---

## 🚀 Features

- ✅ Sends emails using SMTP (Gmail, Outlook, etc.)
- ✅ Uses HTML templates with Jinja2 dynamic fields (e.g. `{{ name }}`, `{{ link }}`)
- ✅ Supports attachments (e.g. `sample.pdf`)
- ✅ Command-line interface (CLI)
- ✅ Logging to `logs/log.json`
- ✅ Scheduling with `scheduler.py`
- ✅ Modular and ready for CI/CD integration

---

## 🧱 Project Structure

```
email-automation/
├── main.py                 # CLI tool
├── scheduler.py            # Scheduled sending (daily at 09:00)
├── .env                    # SMTP credentials (not included in Git)
├── requirements.txt        # Dependencies
├── .gitignore
├── README.md
│
├── templates/
│   └── template.html       # Email template with Jinja2 tags
│
├── data/
│   ├── recipients.xlsx     # List of recipients (name, email, etc.)
│   └── sample.pdf          # PDF attachment sent with each email
│
├── logs/
│   └── log.json            # Logs of email results
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/kirilproger/email-automation.git
cd email-automation
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
EMAIL_USER=your@email.com
EMAIL_PASS=your_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

> **Tip:** If using Gmail, enable "App Passwords" and use it instead of your main password.

---

## 🧪 Usage

### ▶️ Send emails manually

```bash
python main.py --send
```

This uses the default:
- Excel: `data/recipients.xlsx`
- Template: `templates/template.html`
- Attachment: `data/sample.pdf` (if implemented)

You can also specify your own files:

```bash
python main.py --send --file data/custom.xlsx --template templates/custom_template.html
```

### 📄 View email logs

```bash
python main.py --log
```

---

## ⏰ Automate with Scheduler

Run this to send emails automatically every day at 09:00:

```bash
python scheduler.py
```

You can adjust the time inside `scheduler.py` using the `schedule` module.

---

## 📂 Example Excel (`data/recipients.xlsx`)

| name       | email              | link                |
|------------|--------------------|---------------------|
| John Doe   | john@example.com   | https://example.com |
| Jane Smith | jane@example.com   | https://example.org |

---

## ✅ Coming Soon

- CLI option for choosing attachment: `--attachment path/to/file.pdf`
- Per-recipient custom attachments
- Web interface (Flask or Telegram bot)

---

## 🧠 License

MIT — free to use, modify, and share. If you found this useful, star ⭐ the repo!

---

## ✍️ Author

Created by Kyryl Petrushchenko.  
If you have any questions or suggestions, feel free to open an issue or PR.
