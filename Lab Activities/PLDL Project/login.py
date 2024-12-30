import tkinter as tk
from login_gui import LoginGUI

def main():
    root = tk.Tk()
    _app = LoginGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()