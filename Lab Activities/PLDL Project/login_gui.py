import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class LoginGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x550")
        self.root.configure(bg='#2c3e50')

        # Style configuration
        style = ttk.Style()
        style.configure('TFrame', background='#2c3e50')
        style.configure('TLabel', background='#2c3e50', foreground='#ecf0f1', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))
        style.configure('TButton', background='#3498db', foreground='#000000', font=('Arial', 12, 'bold'))

        # Create a frame for the login form with additional padding at the top
        self.frame = ttk.Frame(self.root, padding="100 200 150 150")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Username label and entry
        self.username_label = ttk.Label(self.frame, text="Username:")
        self.username_label.grid(row=20, column=0, sticky=tk.W, pady=5)
        self.username_entry = ttk.Entry(self.frame, width=35)
        self.username_entry.grid(row=20, column=1, pady=5)

        # Password label and entry
        self.password_label = ttk.Label(self.frame, text="Password:")
        self.password_label.grid(row=30, column=0, sticky=tk.W, pady=5)

        # Frame for password entry and eye icon
        self.password_frame = ttk.Frame(self.frame)
        self.password_frame.grid(row=30, column=1, pady=5, sticky=tk.W)

        # Password entry
        self.password_entry = ttk.Entry(self.password_frame, width=30, show="*")
        self.password_entry.grid(row=0, column=0)

        # Load eye icon
        self.eye_icon = Image.open("eye_icon.png")
        self.eye_icon = self.eye_icon.resize((15, 15))
        self.eye_icon = ImageTk.PhotoImage(self.eye_icon)

        # Eye button
        self.show_password_button = ttk.Button(self.password_frame, image=self.eye_icon, command=self.toggle_password)
        self.show_password_button.grid(row=0, column=1, padx=5)

        # Login button
        self.login_button = ttk.Button(self.frame, text="Login")
        self.login_button.grid(row=40, column=1, sticky=tk.E, pady=5)

    def toggle_password(self):
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')
