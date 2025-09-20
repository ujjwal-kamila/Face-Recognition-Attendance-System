from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import os
import csv 
from tkinter import filedialog 
from PIL import Image, ImageTk
 
my_data = []
class Attendance:
    def __init__(self, window):
        self.window = window
        self.window.title("Face Recognition System")

        Label(self.window, text = "Attendance Management System",font = ("aerial",35,"bold"), bg = "#ffdab9", width = 1530 ).place(x = 0, y = 0, width = 1550, height = 70)

        frame = Frame(self.window, background="black", bg = "#008080")
        frame.place(x=0,y=70, height = 650, width = 1540)

        left_frame = LabelFrame(frame, background="#fffaf0" , font = ("aerial",20,"bold"))
        left_frame.place(x = 20, y = 50, height = 600, width = 730)

        Label(left_frame, text = "Student Attendance Details", font = ("Aerial",20,"bold"), background= "#ffdab9", width = 42, padx = 15, pady = 6).place(x=0,y=0)

        Label(left_frame, text = "StudentID", font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 25, y = 75)

        Label(left_frame, text = "Date", font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 412, y = 75)

        Label(left_frame, text = "Name", font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 25, y = 135)

        Label(left_frame, text = "Time", font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 412, y = 135)

        Label(left_frame, text = "Attendance Status", font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 25, y = 195)

        self.student_id = StringVar()
        id = Entry(left_frame, font = ("Aerial",18,"bold"), background="#008080", fg = "white", textvariable = self.student_id)
        id.place(x = 185, y = 77, height = 33, width = 189)

        self.date = StringVar()
        name = Entry(left_frame, font = ("Aerial",18,"bold"), background="#008080", fg = "white", textvariable=self.date)
        name.place(x = 508, y = 77, height = 33, width = 189)

        self.time = StringVar()
        date = Entry(left_frame, font = ("Aerial",18,"bold"), background="#008080", fg = "white", textvariable=self.time)
        date.place(x = 508, y = 137, height = 33, width = 189)

        self.name = StringVar()
        dep = Entry(left_frame, font=("Aerial", 18, "bold"), background="#008080", fg="white", textvariable=self.name)
        dep.place(x=185, y=137, height=33, width=189)

        update = Button(left_frame, text = "Update", font=("Aerial", 25, "bold"), command = self.update ,background="#008080", activebackground= "#ffdab9", fg="white", relief=RAISED, bd = 15,activeforeground="black")
        update.place(x=-1, y=448, height=75, width=365)

        reset = Button(left_frame, text = "Reset", font=("Aerial", 25, "bold"), command = self.reset, background="#008080", activebackground= "#ffdab9", fg="white", relief=RAISED, bd = 15,activeforeground="black")
        reset.place(x=364, y=448, height=75, width=365)

        import1 = Button(left_frame, text = "Import File",command = self.importCsv, font=("Aerial", 25, "bold"), background="#008080", activebackground= "#ffdab9", fg="white", relief=RAISED, bd = 15,activeforeground="black")
        import1.place(x=-1, y=523, height=75, width=365)

        export = Button(left_frame, text = "Export File", pady = 0,command = self.export_csv, font=("Aerial", 25, "bold"), background="#008080", activebackground= "#ffdab9", fg="white", relief=RAISED, bd = 15,activeforeground="black")
        export.place(x=364, y = 523, height=75, width=365)

        arrow = Image.open("Images\\Left_Arrow.png")
        arrow = arrow.resize((100,68))
        self.arrow = ImageTk.PhotoImage(arrow)

        previous = Button(self.window, image = self.arrow, background="#ffdab9", borderwidth=0, activebackground = "#ffdab9", command = self.back)#"#ffdab9")
        previous.place(x = 0, y = 0)


        # Comboboxes
        colour_bg1 = "#008080"
        colour_fg1 = "WHITE"
        colour_bg2 = "#ffdab9"
        colour_fg2 = "BLACK"
        # dep combo
        self.attendance = StringVar()
        self.attendance.set("Present")
        list_text = ["Present","Absent"]

        select_option = OptionMenu(left_frame, self.attendance, *list_text)

        select_option.config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2, activeforeground=colour_fg2,
                             font=("Aerial", 20, "bold"), pady=20, indicatoron=0)

        select_option.place(x = 260, y = 195, height = 39, width = 190)

        select_option["menu"].config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2,
                                     activeforeground=colour_fg2, font=("Aerial", 20, "bold"), border=0)


        right_frame = LabelFrame(frame, background="#fffaf0")
        right_frame.place(x = 780, y = 50, height = 600, width = 730)

        Label(right_frame, text = "Attendance Details", font = ("Aerial",20,"bold"), background= "#ffdab9", width = 42, padx = 15, pady = 6).place(x=0,y=0)
        Label(self.window, text="Attendance Details", font=("aerial", 20, "bold"))

        table = LabelFrame(right_frame, background="#fffaf0")
        table.place(x = 0, y = 50, width = 728, height = 550)

        scroll_x = ttk.Scrollbar(table, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table, orient= VERTICAL)

        self.attendance_table = ttk.Treeview(table, columns=("id","name","date","time","status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set) # x direction and y direction me scroll krne ka set kiya h

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y )
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)


        self.attendance_table.heading("id", text = "Student ID")
        self.attendance_table.heading("name", text = "Name")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("time", text = "Time")
        self.attendance_table.heading("status", text="Status")
        self.attendance_table["show"] = "headings"

        self.attendance_table.pack(fill = BOTH, expand = 1)
        self.attendance_table.bind("<ButtonRelease>", self.get_cursor)

        self.attendance_table.column("id", width=70)
        self.attendance_table.column("date", width=100)
        self.attendance_table.column("time", width=100)
        self.attendance_table.column("status", width=100)


    def fetch_data(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END, values=i)


    def importCsv(self):
        global my_data
        my_data.clear()
        file_name = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Open CSV ", filetypes = (("CSV File","*csv"),("ALL Files","*.*")), parent = self.window)
        with open(file_name) as myfile:
            read = csv.reader(myfile, delimiter = ",")
            for r in read:
                my_data.append(r)
            self.fetch_data(my_data)


    def export_csv(self):
        try:
            if len(my_data) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent = self.window)
                return False
            file_name = filedialog.asksaveasfilename(initialdir = os.getcwd(), title = "Open CSV ", filetypes = (("CSV File","*csv"),("ALL Files","*.*")), parent = self.window)
            with open(file_name, "w", newline = "") as myfile:
                write_new_file = csv.writer(myfile, delimiter = ",")
                for i in my_data:
                    write_new_file.writerow(i)
                messagebox.showinfo("File succefully saved","Your data was exported to " + os.path.basename(file_name) + " successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to {str(es)}", parent=self.window)


    def get_cursor(self, event = ""):
        cursor_row = self.attendance_table.focus()
        content = self.attendance_table.item(cursor_row)
        rows = content['values']
        self.student_id.set(rows[0])
        self.name.set(rows[1])
        self.date.set(rows[2])
        self.time.set(rows[3])
        self.attendance.set(rows[4])


    def reset(self):
        self.student_id.set("")
        self.name.set("")
        self.date.set("")
        self.time.set("")
        self.attendance.set("Present")

    def back(self):
        import A
        self.new = Toplevel(self.window)
        self.new.geometry("1540x800+-10+0")
        self.new.config(background = "#008080")
        self.window.withdraw()
        self.new_window = A.Face_Recognition_System(self.new)

    def update(self):
        messagebox.showerror("Error", "You can't alter the attendance.")



if __name__ == "__main__":
    window = Tk()
    window.config(background="#008080")
    obj = Attendance(window)
    window.geometry("1540x800+-5+0")
    icon = PhotoImage(file = "Images\\M.png")
    window.iconphoto(True, icon)
    window.mainloop()
