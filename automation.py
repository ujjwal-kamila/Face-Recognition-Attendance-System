# automation.py
# Contains functions for sending email and WhatsApp reports.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pywhatkit
import sqlite3
import csv
import os
from datetime import datetime
from config import (DB_PATH, ATTENDANCE_REPORTS_DIR, EMAIL_SENDER, EMAIL_PASSWORD, 
                    EMAIL_RECEIVER, SMTP_SERVER, SMTP_PORT, WHATSAPP_RECEIVER_PHONE)

def generate_daily_report_csv():
    today_date = datetime.now().strftime("%Y-%m-%d")
    filepath = os.path.join(ATTENDANCE_REPORTS_DIR, f"attendance_{today_date}.csv")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT student_id, name, date, time, status FROM attendance WHERE date=?", (today_date,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return None

    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow()
        writer.writerows(rows)
    
    return filepath

def send_email_report():
    report_path = generate_daily_report_csv()
    if not report_path:
        raise Exception("No attendance records for today to send.")

    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg = EMAIL_RECEIVER
    msg = f"Attendance Report - {datetime.now().strftime('%Y-%m-%d')}"

    body = "Please find the attached attendance report for today."
    msg.attach(MIMEText(body, 'plain'))

    with open(report_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name=os.path.basename(report_path))
        part = f'attachment; filename="{os.path.basename(report_path)}"'
        msg.attach(part)

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
    server.quit()

def send_whatsapp_summary():
    today_date = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM attendance WHERE date=?", (today_date,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        message = f"No students were marked present on {today_date}."
    else:
        names = ", ".join([row for row in rows])
        message = f"Attendance Summary for {today_date}:\n\nPresent: {len(rows)} students.\nNames: {names}"

    now = datetime.now()
    pywhatkit.sendwhatmsg(WHATSAPP_RECEIVER_PHONE, message, now.hour, now.minute + 1)