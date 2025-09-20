from tkinter import *
from tkinter import ttk, messagebox, filedialog
import os
import csv
from PIL import Image, ImageTk

class Attendance:
    def __init__(self, window, parent=None):
        self.window = window
        self.parent = parent
        self.window.title("Attendance Management System")
        self.window.geometry("1540x800+-5+0")
        self.window.config(background="#008080")

        icon = PhotoImage(file="Images\\M.png")
        self.window.iconphoto(True, icon)

        self.my_data = []

        # Variables
        self.student_id = StringVar()
        self.name = StringVar()
        self.date = StringVar()
        self.time = StringVar()
        self.attendance = StringVar()

        # UI Setup
        Label(self.window, text="Attendance Management System", font=("aerial", 35, "bold"), bg="#ffdab9").pack(side=TOP, fill=X)

        main_frame = Frame(self.window, background="#008080")
        main_frame.pack(fill=BOTH, expand=True)

        # Left Frame
        left_frame = LabelFrame(main_frame, text="Attendance Details", background="#fffaf0", font=("aerial", 20, "bold"))
        left_frame.place(x=20, y=20, width=730, height=600)
        
        # Back button
        arrow_img = Image.open("Images\\Left_Arrow.png").resize((100, 68))
        self.arrow_photo = ImageTk.PhotoImage(arrow_img)
        Button(self.window, image=self.arrow_photo, background="#ffdab9", borderwidth=0, activebackground="#ffdab9", command=self.back, cursor="hand2").place(x=0, y=0)

        # Form elements in Left Frame
        Label(left_frame, text="StudentID", font=("Aerial",18,"bold"), bg="#fffaf0").place(x=25, y=75)
        Entry(left_frame, textvariable=self.student_id, font=("Aerial",18,"bold"), bg="#008080", fg="white", state='readonly').place(x=185, y=77, height=33, width=189)
        Label(left_frame, text="Date", font=("Aerial",18,"bold"), bg="#fffaf0").place(x=412, y=75)
        Entry(left_frame, textvariable=self.date, font=("Aerial",18,"bold"), bg="#008080", fg="white", state='readonly').place(x=508, y=77, height=33, width=189)
        
        Label(left_frame, text="Name", font=("Aerial",18,"bold"), bg="#fffaf0").place(x=25, y=135)
        Entry(left_frame, textvariable=self.name, font=("Aerial",18,"bold"), bg="#008080", fg="white", state='readonly').place(x=185, y=137, height=33, width=189)
        Label(left_frame, text="Time", font=("Aerial",18,"bold"), bg="#fffaf0").place(x=412, y=135)
        Entry(left_frame, textvariable=self.time, font=("Aerial",18,"bold"), bg="#008080", fg="white", state='readonly').place(x=508, y=137, height=33, width=189)

        Label(left_frame, text="Attendance Status", font=("Aerial",18,"bold"), bg="#fffaf0").place(x=25, y=195)
        self.attendance.set("Present")
        OptionMenu(left_frame, self.attendance, "Present", "Absent").place(x=260, y=195, height=39, width=190)

        # Buttons in Left Frame
        Button(left_frame, text="Update", font=("Aerial", 25, "bold"), command=self.update, background="#008080", fg="white").place(x=-1, y=448, height=75, width=365)
        Button(left_frame, text="Reset", font=("Aerial", 25, "bold"), command=self.reset, background="#008080", fg="white").place(x=364, y=448, height=75, width=365)
        Button(left_frame, text="Import File", command=self.importCsv, font=("Aerial", 25, "bold"), background="#008080", fg="white").place(x=-1, y=523, height=75, width=365)
        Button(left_frame, text="Export File", command=self.export_csv, font=("Aerial", 25, "bold"), background="#008080", fg="white").place(x=364, y=523, height=75, width=365)
        
        # Right Frame
        right_frame = LabelFrame(main_frame, text="Attendance Records", background="#fffaf0", font=("aerial", 20, "bold"))
        right_frame.place(x=780, y=20, width=730, height=600)
        
        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=5, width=715, height=550)
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.attendance_table = ttk.Treeview(table_frame, columns=("id", "name", "date", "time", "status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("id", text="Student ID"); self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("date", text="Date"); self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("status", text="Status")
        self.attendance_table["show"] = "headings"
        self.attendance_table.pack(fill=BOTH, expand=1)
        self.attendance_table.bind("<ButtonRelease>", self.get_cursor)

    def fetch_data(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("", END, values=i)

    def importCsv(self):
        self.my_data.clear()
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.window)
        if file_name:
            with open(file_name, 'r') as myfile:
                read = csv.reader(myfile)
                for r in read:
                    self.my_data.append(r)
                self.fetch_data(self.my_data)

    def export_csv(self):
        try:
            if len(self.my_data) < 1:
                messagebox.showerror("No Data", "No data found to export.", parent=self.window)
                return
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.window)
            if file_name:
                with open(file_name, "w", newline="") as myfile:
                    write_new_file = csv.writer(myfile, delimiter=",")
                    for i in self.my_data:
                        write_new_file.writerow(i)
                    messagebox.showinfo("Success", f"Data exported to {os.path.basename(file_name)} successfully.", parent=self.window)
        except Exception as es:
            messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.window)

    def get_cursor(self, event=""):
        cursor_row = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_row)
        rows = content.get('values', [])
        if rows:
            self.student_id.set(rows[0])
            self.name.set(rows[1])
            self.date.set(rows[2])
            self.time.set(rows[3])
            self.attendance.set(rows[4])

    def reset(self):
        self.student_id.set(""); self.name.set(""); self.date.set("")
        self.time.set(""); self.attendance.set("Present")

    def update(self):
        messagebox.showerror("Error", "Attendance records cannot be altered from this menu.", parent=self.window)

    def back(self):
        self.window.destroy()
        if self.parent:
            self.parent.deiconify()

if __name__ == "__main__":
    window = Tk()
    app = Attendance(window)
    window.mainloop()