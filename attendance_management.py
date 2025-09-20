# attendance_management.py
# Contains the GUI frame for displaying and managing attendance records.

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
import os
from datetime import datetime
from config import ATTENDANCE_REPORTS_DIR, DB_PATH
import sqlite3

class AttendanceManagementFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Attendance Records")
        
        self.create_widgets()
        self.update_attendance_display()

    def create_widgets(self):
        tree_frame = ttk.Frame(self)
        tree_frame.pack(pady=10, padx=10, fill="both", expand=True)

        scroll_x = ttk.Scrollbar(tree_frame, orient="horizontal")
        scroll_y = ttk.Scrollbar(tree_frame, orient="vertical")

        self.attendance_tree = ttk.Treeview(tree_frame, 
                                            columns=("id", "name", "date", "time", "status"),
                                            show="headings",
                                            xscrollcommand=scroll_x.set, 
                                            yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")
        scroll_x.config(command=self.attendance_tree.xview)
        scroll_y.config(command=self.attendance_tree.yview)

        self.attendance_tree.heading("id", text="Student ID")
        self.attendance_tree.heading("name", text="Name")
        self.attendance_tree.heading("date", text="Date")
        self.attendance_tree.heading("time", text="Time")
        self.attendance_tree.heading("status", text="Status")

        for col in ("id", "name", "date", "time", "status"):
            self.attendance_tree.column(col, width=120, anchor="center")
        
        self.attendance_tree.pack(fill="both", expand=True)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10, fill="x", side="bottom")

        ttk.Button(btn_frame, text="Import CSV", command=self.import_csv).pack(side="left", expand=True, padx=5)
        ttk.Button(btn_frame, text="Export CSV", command=self.export_csv).pack(side="left", expand=True, padx=5)
        ttk.Button(btn_frame, text="Reset", command=self.reset_data).pack(side="left", expand=True, padx=5)

    def update_attendance_display(self):
        self.attendance_tree.delete(*self.attendance_tree.get_children())
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            today_date = datetime.now().strftime("%Y-%m-%d")
            cursor.execute("SELECT student_id, name, date, time, status FROM attendance WHERE date=?", (today_date,))
            rows = cursor.fetchall()
            for row in rows:
                self.attendance_tree.insert("", "end", values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("DB Error", f"Failed to fetch attendance data: {e}", parent=self)

    def import_csv(self):
        filepath = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                              filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                                              parent=self)
        if not filepath: return
        
        try:
            with open(filepath, "r") as f:
                csv_reader = csv.reader(f)
                next(csv_reader)
                self.attendance_tree.delete(*self.attendance_tree.get_children())
                for row in csv_reader:
                    self.attendance_tree.insert("", "end", values=row)
            messagebox.showinfo("Success", "Data imported successfully.", parent=self)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to import data: {e}", parent=self)

    def export_csv(self):
        try:
            if not self.attendance_tree.get_children():
                messagebox.showerror("Error", "No data to export.", parent=self)
                return
            
            today_date = datetime.now().strftime("%Y-%m-%d")
            filepath = filedialog.asksaveasfilename(initialdir=ATTENDANCE_REPORTS_DIR,
                                                    initialfile=f"attendance_{today_date}.csv",
                                                    title="Save CSV",
                                                    filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                                                    parent=self)
            if not filepath: return

            with open(filepath, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow()
                for row_id in self.attendance_tree.get_children():
                    row = self.attendance_tree.item(row_id)["values"]
                    writer.writerow(row)
            messagebox.showinfo("Success", f"Data exported to {os.path.basename(filepath)}", parent=self)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export data: {e}", parent=self)

    def reset_data(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all attendance records from the display?", parent=self):
            self.attendance_tree.delete(*self.attendance_tree.get_children())