import tkinter as tk
from user_acc_gui import UserAccountGUI

def main():
    root = tk.Tk()
    _app = UserAccountGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()