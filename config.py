# config.py
# This file centralizes all configuration variables for the application.

# --- File and Directory Paths ---
DB_PATH = "database/attendance.db"
STUDENTS_CSV_PATH = "database/students.csv"
ATTENDANCE_REPORTS_DIR = "attendance_reports/"
FACES_DIR = "faces/"
MODELS_DIR = "models/"
MODEL_PATH = f"{MODELS_DIR}classifier.xml"
HAAR_CASCADE_PATH = "haarcascade_frontalface_default.xml"

# --- Email Automation Settings ---
# IMPORTANT: Use a Gmail "App Password" for security, not your regular password.
# See: https://support.google.com/accounts/answer/185833
EMAIL_SENDER = "ujjwalkamil85@gmail.com"
EMAIL_PASSWORD = "8101193171"
EMAIL_RECEIVER = "ujjwalkamila87@example.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# --- WhatsApp Automation Settings ---
# NOTE: Include the country code with a '+' (e.g., "+1234567890")
# This feature is for demonstration only and may be unreliable.
WHATSAPP_RECEIVER_PHONE = "+918101193171"

# --- Face Recognition Settings ---
# The confidence score is a distance measure (lower is better).
# A value around 50-75 is a good starting point.
RECOGNITION_CONFIDENCE_THRESHOLD = 75

# --- GUI Settings ---
THEME_NAME = "clam" # Options: "clam", "alt", "default", "classic"