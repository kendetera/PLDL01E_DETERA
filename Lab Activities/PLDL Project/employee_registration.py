import tkinter as tk
from employee_registration_gui import EmployeeRegistrationGUI

def main():
    window = tk.Tk()
    _app = EmployeeRegistrationGUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()