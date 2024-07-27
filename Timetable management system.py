import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="timetable_db"
    )
class TimetableApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Timetable Management System")
        self.root.geometry("1000x600")

        self.create_widgets()

    def create_widgets(self):
        # Tabs
        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.pack(expand=1, fill='both')
        self.tab_add_teacher = ttk.Frame(self.tab_control)
        self.tab_add_subject = ttk.Frame(self.tab_control)
        self.tab_add_timetable = ttk.Frame(self.tab_control)
        self.tab_view_timetable = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_add_teacher, text='Add Teacher')
        self.tab_control.add(self.tab_add_subject, text='Add Subject')
        self.tab_control.add(self.tab_add_timetable, text='Add Timetable')
        self.tab_control.add(self.tab_view_timetable, text='View Timetable')
        self.create_add_teacher_tab()
        self.create_add_subject_tab()
        self.create_add_timetable_tab()
        self.create_view_timetable_tab()

    def create_add_teacher_tab(self):
        tk.Label(self.tab_add_teacher, text="Teacher Name:").grid(row=0, column=0, padx=10, pady=10)
        self.teacher_name_entry = ttk.Entry(self.tab_add_teacher)
        self.teacher_name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.tab_add_teacher, text="Department:").grid(row=1, column=0, padx=10, pady=10)
        self.teacher_dept_entry = ttk.Entry(self.tab_add_teacher)
        self.teacher_dept_entry.grid(row=1, column=1, padx=10, pady=10)
        self.add_teacher_button = ttk.Button(self.tab_add_teacher, text="Add Teacher", command=self.add_teacher)
        self.add_teacher_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def create_add_subject_tab(self):
        tk.Label(self.tab_add_subject, text="Subject Code:").grid(row=0, column=0, padx=10, pady=10)
        self.subject_code_entry = ttk.Entry(self.tab_add_subject)
        self.subject_code_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.tab_add_subject, text="Subject Name:").grid(row=1, column=0, padx=10, pady=10)
        self.subject_name_entry = ttk.Entry(self.tab_add_subject)
        self.subject_name_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.tab_add_subject, text="MNE:").grid(row=2, column=0, padx=10, pady=10)
        self.subject_mne_entry = ttk.Entry(self.tab_add_subject)
        self.subject_mne_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.tab_add_subject, text="Teacher ID:").grid(row=3, column=0, padx=10, pady=10)
        self.subject_teacher_id_entry = ttk.Entry(self.tab_add_subject)
        self.subject_teacher_id_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.tab_add_subject, text="Periods as per Syllabus:").grid(row=4, column=0, padx=10, pady=10)
        self.subject_periods_entry = ttk.Entry(self.tab_add_subject)
        self.subject_periods_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self.tab_add_subject, text="Allotted Periods:").grid(row=5, column=0, padx=10, pady=10)
        self.subject_allotted_entry = ttk.Entry(self.tab_add_subject)
        self.subject_allotted_entry.grid(row=5, column=1, padx=10, pady=10)

        self.add_subject_button = ttk.Button(self.tab_add_subject, text="Add Subject", command=self.add_subject)
        self.add_subject_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def create_add_timetable_tab(self):
        tk.Label(self.tab_add_timetable, text="Day:").grid(row=0, column=0, padx=10, pady=10)
        self.day_entry = ttk.Entry(self.tab_add_timetable)
        self.day_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.tab_add_timetable, text="Time Slot:").grid(row=1, column=0, padx=10, pady=10)
        self.time_slot_entry = ttk.Entry(self.tab_add_timetable)
        self.time_slot_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.tab_add_timetable, text="Subject ID:").grid(row=2, column=0, padx=10, pady=10)
        self.subject_id_entry = ttk.Entry(self.tab_add_timetable)
        self.subject_id_entry.grid(row=2, column=1, padx=10, pady=10)

        self.add_timetable_button = ttk.Button(self.tab_add_timetable, text="Add Timetable Entry", command=self.add_timetable_entry)
        self.add_timetable_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def create_view_timetable_tab(self):
        self.timetable_grid = ttk.Frame(self.tab_view_timetable)
        self.timetable_grid.pack(expand=1, fill='both')
        self.view_button = ttk.Button(self.tab_view_timetable, text="Refresh Timetable", command=self.view_timetable)
        self.view_button.pack(pady=10)
        self.clear_button = ttk.Button(self.tab_view_timetable, text="Clear All Data", command=self.clear_data)
        self.clear_button.pack(pady=10)

    def add_teacher(self):
        name = self.teacher_name_entry.get()
        dept = self.teacher_dept_entry.get()
        db = connect_db()
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO teachers (name, dept) VALUES (%s, %s)", (name, dept))
            db.commit()
            messagebox.showinfo("Success", "Teacher added successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            db.close()
    def add_subject(self):
        code = self.subject_code_entry.get()
        name = self.subject_name_entry.get()
        mne = self.subject_mne_entry.get()
        teacher_id = self.subject_teacher_id_entry.get()
        periods = self.subject_periods_entry.get()
        allotted = self.subject_allotted_entry.get()
        db = connect_db()
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO subjects (code, name, mne, teacher_id, periods_as_per_syllabus, allotted_periods) VALUES (%s, %s, %s, %s, %s, %s)", 
                           (code, name, mne, teacher_id, periods, allotted))
            db.commit()
            messagebox.showinfo("Success", "Subject added successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            db.close()

    def add_timetable_entry(self):
        day = self.day_entry.get()
        time_slot = self.time_slot_entry.get()
        subject_id = self.subject_id_entry.get()
        db = connect_db()
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO timetable (day, time_slot, subject_id) VALUES (%s, %s, %s)",
                           (day, time_slot, subject_id))
            db.commit()
            messagebox.showinfo("Success", "Timetable entry added successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            db.close()

    def view_timetable(self):
        for widget in self.timetable_grid.winfo_children():
            widget.destroy()

        db = connect_db()
        cursor = db.cursor()
        try:
            cursor.execute("""
                SELECT timetable.day, timetable.time_slot, subjects.mne
                FROM timetable
                JOIN subjects ON timetable.subject_id = subjects.id
                ORDER BY 
                    CASE
                        WHEN timetable.day = 'MON' THEN 1
                        WHEN timetable.day = 'TUE' THEN 2
                        WHEN timetable.day = 'WED' THEN 3
                        WHEN timetable.day = 'THU' THEN 4
                        WHEN timetable.day = 'FRI' THEN 5
                        ELSE 6
                    END, timetable.time_slot
            """)
            rows = cursor.fetchall()

            days = ['MON', 'TUE', 'WED', 'THU', 'FRI']
            times = ["8.15-9.05 AM", "9.05-9.55 AM", "10.10-11.00 AM", "11.00-11.50 AM", "11.50-12.40 PM", 
                     "1.30-2.15 PM", "2.15-3.00 PM", "3.00-3.45 PM", "4.00-5.00 PM"]

            timetable = {day: {time: "" for time in times} for day in days}

            for row in rows:
                day, time_slot, mne = row
                timetable[day][time_slot] = mne

            for i, day in enumerate(days):
                tk.Label(self.timetable_grid, text=day, borderwidth=1, relief="solid").grid(row=i+1, column=0, sticky="nsew")

            for j, time in enumerate(times):
                tk.Label(self.timetable_grid, text=time, borderwidth=1, relief="solid").grid(row=0, column=j+1, sticky="nsew")

            for i, day in enumerate(days):
                for j, time in enumerate(times):
                    tk.Label(self.timetable_grid, text=timetable[day][time], borderwidth=1, relief="solid").grid(row=i+1, column=j+1, sticky="nsew")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            db.close()

    def clear_data(self):
        db = connect_db()
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM timetable")
            cursor.execute("DELETE FROM teachers")
            cursor.execute("DELETE FROM subjects")
            db.commit()
            messagebox.showinfo("Success", "All data cleared successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            db.close()

if _name_ == "_main_":
    root = tk.Tk()
    app = TimetableApp(root)
    root.mainloop()
