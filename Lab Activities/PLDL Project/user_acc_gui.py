import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class UserAccountGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("User Account")
        self.root.geometry("1500x600")
        self.root.configure(bg='#f2f0e3')

        # Style configuration
        style = ttk.Style()
        style.configure('TFrame', bg='#f0f0f0')
        style.configure('TLabel', bg='#f8f3f3', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))

        self.header = tk.Label(self.root, text="User Account Page", bg='#f2f0e3', font=('Arial', 24))
        self.header.pack(pady=80)

        # Create a frame for the user account page
        self.frame = tk.Frame(self.root, width=1300, height=350, bg='#f8f3f3', relief='raised', borderwidth=10)
        self.frame.place(x=100, y=180)

        # First row Labels
        self.first_name = ttk.Label(self.frame, text="First Name", background='#f8f3f3')
        self.first_name.place(x=220, y=20)
        self.middle_name = ttk.Label(self.frame, text="Middle Name", background='#f8f3f3')
        self.middle_name.place(x=420, y=20)
        self.last_name = ttk.Label(self.frame, text="Last Name", background='#f8f3f3')
        self.last_name.place(x=620, y=20)
        self.suffix = ttk.Label(self.frame, text="Suffix", background='#f8f3f3')
        self.suffix.place(x=820, y=20)
        self.department = ttk.Label(self.frame, text="Department", background='#f8f3f3')
        self.department.place(x=1020, y=20)

        # First row labels' entries
        self.first_name_entry = ttk.Entry(self.frame, width=25)
        self.first_name_entry.place(x=220, y=50)
        self.middle_name_entry = ttk.Entry(self.frame, width=25)
        self.middle_name_entry.place(x=420, y=50)
        self.last_name_entry = ttk.Entry(self.frame, width=25)
        self.last_name_entry.place(x=620, y=50)
        self.suffix_entry = ttk.Entry(self.frame, width=25)
        self.suffix_entry.place(x=820, y=50)
        self.department_entry = ttk.Entry(self.frame, width=25)
        self.department_entry.place(x=1020, y=50)

        # second row labels
        self.description = ttk.Label(self.frame, text="Description", background='#f8f3f3')
        self.description.place(x=220, y=100)
        self.username = ttk.Label(self.frame, text="Username", background='#f8f3f3')
        self.username.place(x=530, y=100)
        self.password = ttk.Label(self.frame, text="Password", background='#f8f3f3')
        self.password.place(x=860, y=100)

        # second row labels' entries
        self.description_entry = ttk.Entry(self.frame, width=40)
        self.description_entry.place(x=220, y=130)
        self.username_entry = ttk.Entry(self.frame, width=40)
        self.username_entry.place(x=530, y=130)
        self.password_entry = ttk.Entry(self.frame, width=40)
        self.password_entry.place(x=860, y=130)

        # Third row labels
        self.confirm_password = ttk.Label(self.frame, text="Confirm Password", background='#f8f3f3')
        self.confirm_password.place(x=50, y=200)
        self.user_type = ttk.Label(self.frame, text="User Type", background='#f8f3f3')
        self.user_type.place(x=350, y=200)
        self.user_status = ttk.Label(self.frame, text="User Status", background='#f8f3f3')
        self.user_status.place(x=650, y=200)
        self.employee_number = ttk.Label(self.frame, text="Employee Number", background='#f8f3f3')
        self.employee_number.place(x=950, y=200)

        # Third row labels' entries
        self.confirm_password_entry = ttk.Entry(self.frame, width=35)
        self.confirm_password_entry.place(x=50, y=230)
        self.user_type_entry = ttk.Entry(self.frame, width=35)
        self.user_type_entry.place(x=350, y=230)
        self.user_status_entry = ttk.Entry(self.frame, width=35)
        self.user_status_entry.place(x=650, y=230)
        self.employee_number_entry = ttk.Entry(self.frame, width=35)
        self.employee_number_entry.place(x=950, y=230)

        # Create the Three buttons below
        self.update_button = tk.Button(self.frame, width=10, text="Update", bg='#007bff', fg='white', font=('Arial', 12))
        self.update_button.place(x=900, y=285)
        self.delete_button = tk.Button(self.frame, width=10, text="Delete", bg='#ffc107', fg='black', font=('Arial', 12))
        self.delete_button.place(x=1025, y=285)
        self.cancel_button = tk.Button(self.frame, width=10, text="Cancel", font=('Arial', 12))
        self.cancel_button.place(x=1150, y=285)

        # profile icon
        photo = Image.open("profile_circle.png")
        photo = photo.resize((150, 150))
        icon = ImageTk.PhotoImage(photo)
        user_icon = tk.Label(self.root, image=icon, bg='#f8f3f3')
        user_icon.image = icon
        user_icon.place(x=135, y=195)