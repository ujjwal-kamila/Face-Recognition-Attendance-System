from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector 
import cv2
from PIL import Image, ImageTk
 
class Student:  
    def __init__(self, window):
        self.window = window
        self.window.title("Face Recognition System")

        self.dep = StringVar()
        self.course = StringVar()
        self.semester = StringVar()
        self.year = StringVar()
        self.student_id = StringVar()
        self.dob = StringVar()
        self.student_name = StringVar()
        self.mobile = StringVar()
        self.parent_name = StringVar()
        self.email = StringVar()
        self.school = StringVar()
        self.address = StringVar()

        self.dob.set("YYYY-MM-DD")
        self.email.set("xyz@gmail.com")


        Label(self.window, text = "Student Management System", font = ("aerial",35,"bold"), bg = "#ffdab9", width = 1530 ).place(x = 0, y = 0, width = 1550, height = 70)

        frame = Frame(self.window, background = "#008080")
        frame.place(x = 0, y = 71, width = 1550, height = 650)

        left_frame = LabelFrame(frame, background="#fffaf0" , font = ("aerial",20,"bold"))
        left_frame.place(x = 20, y = 50, height = 600, width = 730)


        course = LabelFrame(left_frame, background= "#fffaf0")
        course.place(x = 0, y = 0, height = 180, width = 728)


        Label(course, text = "Course Information", font = ("Aerial",20,"bold"), background="#fffaf0").place(x=0,y=0)
        Label(course, text = "Department", font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 25, y = 50)
        Label(course, text = "Course", font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 400, y = 50)
        Label(course, text = "Semester", font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 25, y = 110)
        Label(course, text = "Year", font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 402, y = 110)

        colour_bg1 = "#008080"
        colour_fg1 = "WHITE"
        colour_bg2 = "#ffdab9"
        colour_fg2 = "BLACK"

        self.dep.set("Select Department")
        list_text = ["IT","Civil","CS","Electrical"]

        select_option = OptionMenu(course, self.dep, *list_text)

        select_option.config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2, activeforeground=colour_fg2,
                             font=("Aerial", 15, "bold"), pady=20, indicatoron=0)

        select_option.place(x = 185, y = 50, height = 39, width = 190)

        select_option["menu"].config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2,
                                     activeforeground=colour_fg2, font=("Aerial", 15, "bold"), border=0)

        self.course.set("Select Course")
        list_text2 = ["Data Structures","Web Developer","Artificial Intelligence","Machine Learning"]

        select_option = OptionMenu(course, self.course, *list_text2)

        select_option.config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2, activeforeground=colour_fg2,
                             font=("Aerial", 15, "bold"), pady=20, indicatoron=0)

        select_option.place(x = 508, y = 50, height = 39, width = 190)

        select_option["menu"].config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2,
                                     activeforeground=colour_fg2, font=("Aerial", 15, "bold"), border=0)

        self.semester.set("Select Semester")
        list_text3= ['1st Semester', '2nd Semester', '3rd Semester', '4th Semester', '5th Semester', "6th Semester", "7th Semester", "8th Semester"]

        select_option = OptionMenu(course, self.semester, *list_text3)

        select_option.config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2, activeforeground=colour_fg2,
                             font=("Aerial", 15, "bold"), pady=20, indicatoron=0)

        select_option.place(x = 185, y = 110, height = 39, width = 190)

        select_option["menu"].config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2,
                                     activeforeground=colour_fg2, font=("Aerial", 15, "bold"), border=0)

        self.year.set("Select Year")
        list_text4= [2024, 2023, 2022, 2021, 2020]

        select_option = OptionMenu(course, self.year, *list_text4)

        select_option.config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2, activeforeground=colour_fg2,
                             font=("Aerial", 15, "bold"), pady=20, indicatoron=0)

        select_option.place(x = 508, y = 110, height = 39, width = 190)

        select_option["menu"].config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2,
                                     activeforeground=colour_fg2, font=("Aerial", 15, "bold"), border=0)


        info = LabelFrame(left_frame, background= "#fffaf0")
        info.place(x = 0, y = 179, height = 300, width = 728)
        Label(info, text = "Student Information", font= ("aerial",20,"bold"), bg = "#fffaf0").place(x=0, y=0)

        Label(info, text = "Student ID", font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 20, y = 50)
        Label(info, text = "Student Name", font = ("Aerial",17,"bold"), background="#fffaf0").place(x = 20, y = 100)
        Label(info, text = "Parent Name", font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 20, y = 150)
        Label(info, text = "School Name", font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 20, y = 200)
        Label(info, text = "D.O.B", font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 400, y = 50)
        Label(info, text = "Mobile", font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 400, y = 100)
        Label(info, text = "Email", font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 400, y = 150)
        Label(info, text = "Address",  font = ("Aerial",18,"bold"), background="#fffaf0").place(x = 400, y = 200)


        id = Entry(info, font = ("Aerial",18,"bold"), background="#008080", fg = "white", textvariable=self.student_id)
        id.place(x = 185, y = 50, height = 33, width = 189)

        name = Entry(info, font = ("Aerial",18,"bold"), background="#008080", fg = "white", textvariable=self.student_name)
        name.place(x = 185, y = 100, height = 33, width = 189)

        parent = Entry(info, font = ("Aerial",18,"bold"), background="#008080", fg = "white", textvariable=self.parent_name)
        parent.place(x = 185, y = 150, height = 33, width = 189)

        school = Entry(info, font = ("Aerial",18,"bold"), background="#008080", fg = "white", textvariable=self.school)
        school.place(x = 185, y = 200, height = 33, width = 189)

        dob = Entry(info, font = ("Aerial",18,"bold"), background="#008080", fg = "white", textvariable=self.dob)
        dob.place(x = 508, y = 50, height = 33, width = 189)

        mobile = Entry(info, font = ("Aerial",18,"bold"), background="#008080", fg = "white", textvariable=self.mobile)
        mobile.place(x = 508, y = 100, height = 33, width = 189)

        email = Entry(info, font = ("Aerial",18,"bold"), background="#008080", fg = "white", textvariable=self.email)
        email.place(x = 508, y = 150, height = 33, width = 189)

        address = Entry(info, font = ("Aerial",18,"bold"), background="#008080", fg = "white", textvariable=self.address)
        address.place(x = 508, y = 200, height = 33, width = 189)


        buttons = LabelFrame(left_frame, background= "black")
        buttons.place(x = 0, y = 470, height = 180, width = 728)

        save = Button(buttons, text = "Save",command = self.add_data, background="#008080",foreground="white", activebackground="#ffdab9", font = ("aerial",15,"bold"), relief=RAISED, bd = 10, activeforeground="black", width=18)
        save.grid(row = 0, column = 0, pady = 3)

        update = Button(buttons, text = "Update", background="#008080",foreground="white", activebackground="#ffdab9", font = ("aerial",15,"bold"), relief=RAISED, bd = 10,activeforeground="black", width=18, command=self.update_data)
        update.grid(row = 0, column = 1)

        delete = Button(buttons, text = "Delete", background="#008080",foreground="white", activebackground= "#ffdab9", font = ("aerial",15,"bold"), relief=RAISED, bd = 10,activeforeground="black", width=18, command = self.delete_data)
        delete.grid(row = 0, column = 2)

        reset = Button(buttons, text = "Reset", background="#008080",foreground="white", activebackground="#ffdab9", font = ("aerial",15,"bold"), relief=RAISED, bd = 10, activeforeground="black", width=18, command = self.reset_data)
        reset.grid(row = 1, column = 0)

        update_photo = Button(buttons, text = "Update Photo Sample", background="#008080",foreground="white", activebackground="#ffdab9", font = ("aerial",15,"bold"), relief=RAISED, bd = 10,activeforeground="black", width=18, command = self.generate_dataset)
        update_photo.grid(row = 1, column = 1)

        previous = Button(buttons, text = "To Previous Page", command = self.back,background="#008080",foreground="white", activebackground= "#ffdab9", font = ("aerial",15,"bold"), relief=RAISED, bd = 10,activeforeground="black", width=18)
        previous.grid(row = 1, column = 2)

        arrow = Image.open("Images\\Left_Arrow.png")
        arrow = arrow.resize((100,68))
        self.arrow = ImageTk.PhotoImage(arrow)

        previous = Button(self.window, image = self.arrow, background="#ffdab9", borderwidth=0, activebackground = "#ffdab9", command = self.back)#"#ffdab9")
        previous.place(x = 0, y = 0)


        right_frame = LabelFrame(frame, background="#fffaf0", font = ("aerial",10,"bold"))
        right_frame.place(x = 780, y = 50, height = 600, width = 730)

        search_frame = LabelFrame(right_frame, background="#fffaf0")
        search_frame.place(x=0, y=0, width = 728, height = 115)

        Label(search_frame, text = "Search System", font = ("aerial",20,"bold"), background="#fffaf0").place(x = 0, y = 0)
        Label(search_frame, text = "Search By", font = ("aerial",18,"bold"), background="#fffaf0").place(x = 13, y = 52)

        self.category = StringVar()
        self.category.set("Category")
        list_text5 = ["StudentID","Name","Department", "Semester"]

        select_option = OptionMenu(search_frame, self.category, *list_text5)

        select_option.config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2, activeforeground=colour_fg2,
                             font=("Aerial", 15, "bold"), pady=20, indicatoron=0)

        select_option.place(x = 146, y = 50, height = 39, width = 160)

        select_option["menu"].config(bg=colour_bg1, fg=colour_fg1, activebackground=colour_bg2,
                                     activeforeground=colour_fg2, font=("Aerial", 15, "bold"), border=0)
        self.variable5 = StringVar()
        category = Entry(search_frame, font = ("Aerial",15,"bold"),textvariable = self.variable5, background="#008080", fg = "white")
        category.place(x = 327, y = 53, height = 33, width = 160)

        search = Button(search_frame, text = "Search", font = ("Aerial", 15, "bold"), command = self.search,background="#008080", fg = "white", activebackground="#ffdab9", relief= RAISED, bd = 7)
        search.place(x = 508, y = 53, height = 33, width = 93)

        show_all = Button(search_frame, text = "Show All", font = ("Aerial", 15, "bold"),command = self.fetch_data, background="#008080", fg = "white", activebackground="#ffdab9",
                          relief= RAISED, bd = 5)
        show_all.place(x = 620, y = 53, height = 33, width = 98)


        table = LabelFrame(right_frame, background="#fffaf0")
        table.place(x = 0, y = 114, width = 728, height = 483)

        scroll_x = ttk.Scrollbar(table, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table, orient= VERTICAL)

        self.student_table = ttk.Treeview(table, columns=("id","name","dep","course","sem","year","mobile","email","school","parent","dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set) # x direction and y direction me scroll krne ka set kiya h

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y )
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("id", text = "Student ID")
        self.student_table.heading("name", text = "Name")
        self.student_table.heading("dep", text = "Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("year", text = "Year")
        self.student_table.heading("mobile", text="Mobile")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("school", text="School")
        self.student_table.heading("parent", text="Parent Name")
        self.student_table.heading("dob", text = "Date of Birth")
        self.student_table.heading("address", text = "Address")
        self.student_table["show"] = "headings"

        self.student_table.pack(fill = BOTH, expand = 1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        self.student_table.column("id",width=90)
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=150)
        self.student_table.column("sem", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("mobile", width=100)
        self.student_table.column("dob", width=100)



    def add_data(self):
        if self.dep.get() == "Select Department" or self.student_id.get() == "" or self.student_name.get() == "":
            messagebox.showerror("Error", "All fields  are required.", parent = self.window)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", user = "root", password = "Ujjwal@81", database = "credentials")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                              self.student_id.get(),
                                                                                                              self.student_name.get(),
                                                                                                              self.dep.get(),
                                                                                                              self.course.get(),
                                                                                                              self.semester.get(),
                                                                                                              self.year.get(),
                                                                                                              self.mobile.get(),
                                                                                                              self.email.get(),
                                                                                                              self.school.get(),
                                                                                                              self.parent_name.get(),
                                                                                                              self.dob.get(),
                                                                                                              self.address.get()
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been registered.", parent = self.window)
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}", parent = self.window)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Ujjwal@81", database="credentials")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            data = my_cursor.fetchall()

        # clear the table first
            self.student_table.delete(*self.student_table.get_children())

        # insert rows if found
            for row in data:
                self.student_table.insert("", END, values=row)

            conn.close()

        except Exception as es:
            messagebox.showerror("Error", f"Due to {str(es)}", parent=self.window)

    

        # if len(data) != 0:
        #     self.student_table.delete(*self.student_table.get_children())
        #     for i in data:
        #         self.student_table.insert("",END,values = i)
        #     conn.commit()
        # conn.close()

    def get_cursor(self, event = ""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.student_id.set(data[0])
        self.student_name.set(data[1])
        self.dep.set(data[2])
        self.course.set(data[3])
        self.semester.set(data[4])
        self.year.set(data[5])
        self.mobile.set(data[6])
        self.email.set(data[7])
        self.school.set(data[8])
        self.parent_name.set(data[9])
        self.dob.set(data[10])
        self.address.set(data[11])


    def update_data(self):
        if self.dep.get() == "Select Department" or self.student_id.get() == "" or self.student_name.get() == "":
            messagebox.showerror("Error", "All fields  are required.", parent=self.window)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update details of this student", parent=self.window)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Ujjwal@81",
                                                       database="credentials")
                    mycursor = conn.cursor()
                    sql = """UPDATE student SET Name = %s, Department = %s, Course = %s, Semester = %s, Year = %s, Mobile = %s, Email = %s ,School = %s, Parent_Name = %s, DOB = %s, Address = %s WHERE StudentID = %s""" #(name, address) VALUES (%s, %s)"
                    mycursor.execute(sql, (self.student_name.get(), self.dep.get(), self.course.get(), self.semester.get(), self.year.get(), self.mobile.get(), self.email.get(), self.school.get(), self.parent_name.get(), self.dob.get(), self.address.get(), self.student_id.get()))
                    conn.commit()
                    conn.close()
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student Details successfully updated.", parent=self.window)

                self.fetch_data()

            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.window)


    def delete_data(self):
        if self.student_id.get() == "":
            messagebox.showerror("Error","Student ID is required.", parent = self.window)
        else:
            try:
                delete = messagebox.askyesno("Deleting Student Information","Do you want to delete this student's information",parent = self.window)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Ujjwal@81",
                                               database="credentials")
                    my_cursor = conn.cursor()
                    sql = "delete from student where StudentID = %s"
                    val = (self.student_id.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    conn.close()
                else:
                    if not delete:
                        return

                self.fetch_data()

                messagebox.showinfo("Delete","Successfully deleted student details ", parent = self.window)
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.window)


    def reset_data(self):
        self.dep.set("Select Department")
        self.course.set("Select Course")
        self.semester.set("Select Semester")
        self.year.set("Select Year")
        self.student_id.set("")
        self.dob.set("YYYY-MM-DD")
        self.student_name.set("")
        self.mobile.set("")
        self.parent_name.set("")
        self.email.set("xyz@gmail.com")
        self.school.set("")
        self.address.set("")



    def back(self):
        from A import Face_Recognition_System
        self.new_window = Toplevel(self.window)
        self.new_window.geometry("1540x800+-5+0")
        self.new_window.config(bg = "#008080")
        self.new = Face_Recognition_System(self.new_window)
        self.window.withdraw()

    def generate_dataset(self):
        if self.dep.get() == "Select Department" or self.student_id.get() == "" or self.student_name.get() == "":
            messagebox.showerror("Error", "All fields  are required.", parent=self.window)
        else:
            try:
                conn = mysql.connector.connect(
                host="localhost", user="root", password="Ujjwal@81", database="credentials"
                )
                mycursor = conn.cursor()

            # update DB with latest form values
                sql = """UPDATE student 
                     SET Name=%s, Department=%s, Course=%s, Semester=%s, Year=%s, Mobile=%s, 
                         Email=%s, School=%s, Parent_Name=%s, DOB=%s, Address=%s 
                     WHERE StudentID=%s"""
                mycursor.execute(sql, (
                self.student_name.get(), self.dep.get(), self.course.get(), self.semester.get(),
                self.year.get(), self.mobile.get(), self.email.get(), self.school.get(),
                self.parent_name.get(), self.dob.get(), self.address.get(), self.student_id.get()
                ))

                conn.commit()
                conn.close()

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(grey, 1.3, 5)
                    for (x, y, w, h) in faces:
                        return img[y:y + h, x:x + w]
                    return None

                cap = cv2.VideoCapture(0)
                img_id = 0
                student_id = self.student_id.get()  # ✅ use actual StudentID from entry

                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        file_path = f"Faces/user.{student_id}.{img_id}.jpg"  # ✅ fixed
                        cv2.imwrite(file_path, face)

                        cv2.putText(face, str(img_id), (50, 50),
                                cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 27 or img_id == 100:  # ESC or 100 images
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", f"Photo samples saved for Student ID {student_id}!")

            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.window)


    def search(self):
        if self.category.get() == "Category" or self.variable5.get() == "":
            messagebox.showerror("Error",
                                 "Select one of the categories and enter details before clicking on the search button!")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Ujjwal@81",
                                                   database="credentials")
                my_cursor = conn.cursor()

                my_cursor.execute("select * from student where " + str(self.category.get()) + " LIKE '%" + str(
                    self.variable5.get()) + "%'")
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.window)


if __name__ == "__main__":
    window = Tk()
    obj = Student(window)
    window.geometry("1540x800+-5+0")
    icon = PhotoImage(file = "Images\\M.png")
    window.iconphoto(True, icon)
    window.configure(background="#008080")
    window.mainloop()
