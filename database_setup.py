# database_setup.py
# This script initializes the database and creates the necessary tables.
# Run this script once before starting the main application for the first time.

import sqlite3
import os
from config import DB_PATH, FACES_DIR, MODELS_DIR, ATTENDANCE_REPORTS_DIR

def setup_database():
    """
    Creates the necessary directories and the SQLite database with the required tables.
    """
    # Create necessary directories if they don't exist
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    os.makedirs(FACES_DIR, exist_ok=True)
    os.makedirs(MODELS_DIR, exist_ok=True)
    os.makedirs(ATTENDANCE_REPORTS_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create the 'students' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        dob TEXT,
        email TEXT,
        dept TEXT,
        course TEXT,
        semester TEXT,
        year TEXT
    )
    """)

    # Create the 'attendance' table with a unique constraint
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT NOT NULL,
        name TEXT,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        status TEXT,
        UNIQUE(student_id, date)
    )
    """)

    conn.commit()
    conn.close()
    print("Database and directories set up successfully.")

if __name__ == "__main__":
    setup_database()