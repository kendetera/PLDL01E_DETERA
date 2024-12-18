import tkinter as tk
from tkinter import Label, Text, Button, ttk
from PIL import Image, ImageTk

class PayrollGUI:
    def __init__(self, window):
        self.window = window
        self.window.title('Payroll Check GUI')
        self.window.geometry("900x1520")

    def create_label(self, x, y, text, font=('Arial', 10)):
        label = Label(self.window, text=text, font=font)
        label.place(x=x, y=y)
        return label

    def create_textbox(self, x, y, width=25, height=1, fg='black', bg='white', font=('Arial', 12)):
        textbox = Text(self.window, width=width, height=height, fg=fg, bg=bg, font=font)
        textbox.place(x=x, y=y)
        return textbox

    def create_button(self, x, y, text, width=10, bg='red', fg='white'):
        button = Button(self.window, width=width, text=text, bg=bg, fg=fg, cursor='hand2', border=5)
        button.place(x=x, y=y)
        return button

    def create_button1(self, x, y, text, width=10, bg='red', fg='white', relief='raised'):
        button = Button(self.window, width=width, text=text, bg=bg, fg=fg, cursor='hand2', border=2, relief='solid')
        button.place(x=x, y=y)
        return button

    def create_image(self, image_path, x, y, width, height):
        image = Image.open(image_path)
        resized_image = ImageTk.PhotoImage(image.resize((width, height)))
        label = Label(self.window, image=resized_image)
        label.image = resized_image  # Keep a reference to avoid garbage collection
        label.place(x=x, y=y)
        return label

def main():
    window = tk.Tk()
    gui = PayrollGUI(window)

    # Heading
    gui.create_label(x=260, y=20, text="SE-RI'S CHOICE PAYROLL", font=('Times New Roman', 30, 'bold'))

    # Employee Basic Info Labels
    gui.create_label(x=40, y=290, text='Employee Number')
    gui.create_label(x=40, y=330, text='Search Employee')
    gui.create_label(x=40, y=360, text='Department')
    gui.create_label(x=450, y=120, text='First Name')
    gui.create_label(x=450, y=150, text='Middle Name')
    gui.create_label(x=450, y=180, text='Surname')
    gui.create_label(x=450, y=210, text='Civil Status')
    gui.create_label(x=450, y=240, text='Qualified Dependents Status')
    gui.create_label(x=450, y=270, text='Pay Date')
    gui.create_label(x=450, y=300, text='Employee Status')
    gui.create_label(x=450, y=330, text='Designation')

    # Employee Basic Info Textboxes
    gui.create_textbox(x=180, y=290)
    gui.create_textbox(x=180, y=360)
    gui.create_textbox(x=640, y=120)
    gui.create_textbox(x=640, y=150)
    gui.create_textbox(x=640, y=180)
    gui.create_textbox(x=640, y=210)
    gui.create_textbox(x=640, y=240)
    gui.create_textbox(x=640, y=270)
    gui.create_textbox(x=640, y=300)
    gui.create_textbox(x=640, y=330)

    # Basic Income Labels
    gui.create_label(x=40, y=440, text='Rate / Hour')
    gui.create_label(x=40, y=470, text='No. of Hours / Cut Off')
    gui.create_label(x=40, y=500, text='Income / Cut Off')

    # Basic Income Textboxes
    gui.create_textbox(x=180, y=440)
    gui.create_textbox(x=180, y=470)
    gui.create_textbox(x=180, y=500)

    # Honorarium Income Labels
    gui.create_label(x=40, y=580, text='Rate / Hour')
    gui.create_label(x=40, y=610, text='No. of Hours / Cut Off')
    gui.create_label(x=40, y=640, text='Income / Cut Off')

    # Honorarium Income Textboxes
    gui.create_textbox(x=180, y=580)
    gui.create_textbox(x=180, y=610)
    gui.create_textbox(x=180, y=640)

    # Other Income Labels
    gui.create_label(x=40, y=720, text='Rate / Hour')
    gui.create_label(x=40, y=750, text='No. of Hours / Cut Off')
    gui.create_label(x=40, y=780, text='Income / Cut Off')

    # Other Income Textboxes
    gui.create_textbox(x=180, y=710)
    gui.create_textbox(x=180, y=740)
    gui.create_textbox(x=180, y=770)

    # Summary Income Labels
    gui.create_label(x=40, y=860, text='GROSS INCOME')
    gui.create_label(x=40, y=890, text='NET INCOME')

    # Summary Income Textboxes
    gui.create_textbox(x=180, y=860)
    gui.create_textbox(x=180, y=890)

    # Regular Deductions Labels
    gui.create_label(x=450, y=410, text='SSS Contribution')
    gui.create_label(x=450, y=440, text='PhilHealth Contribution')
    gui.create_label(x=450, y=470, text='Pagibig Contribution')
    gui.create_label(x=450, y=500, text='Income Tax Contribution')

    # Regular Deductions Textboxes
    gui.create_textbox(x=640, y=410)
    gui.create_textbox(x=640, y=440)
    gui.create_textbox(x=640, y=470)
    gui.create_textbox(x=640, y=500)

    # Other Deductions Labels
    gui.create_label(x=450, y=580, text='SSS Loan')
    gui.create_label(x=450, y=610, text='Pagibig Loan')
    gui.create_label(x=450, y=640, text='Faculty Savings Deposit')
    gui.create_label(x=450, y=670, text='Faculty Savings Loan')
    gui.create_label(x=450, y=700, text='Salary Loan')
    gui.create_label(x=450, y=730, text='Other Loan')

    # Other Deductions Textboxes
    gui.create_textbox(x=640, y=580)
    gui.create_textbox(x=640, y=610)
    gui.create_textbox(x=640, y=640)
    gui.create_textbox(x=640, y=670)
    gui.create_textbox(x=640, y=700)
    gui.create_textbox(x=640, y=730)

    # Deduction Summary Label
    gui.create_label(x=450, y=810, text='Total Deduction')

    # Deduction Summary Textbox
    gui.create_textbox(x=640, y=810, bg='light gray')

    # Section Labels
    gui.create_label(x=20, y=100, text='EMPLOYEE BASIC INFO:', font=('Arial', 12, 'bold'))
    gui.create_label(x=30, y=400, text='BASIC INCOME:', font=('Arial', 12, 'bold'))
    gui.create_label(x=30, y=540, text='HONORARIUM INCOME:', font=('Arial', 12, 'bold'))
    gui.create_label(x=30, y=680, text='OTHER INCOME:', font=('Arial', 12, 'bold'))
    gui.create_label(x=30, y=820, text='SUMMARY INCOME:', font=('Arial', 12, 'bold'))
    gui.create_label(x=430, y=370, text='REGULAR DEDUCTIONS:', font=('Arial', 12, 'bold'))
    gui.create_label(x=430, y=540, text='OTHER DEDUCTIONS:', font=('Arial', 12, 'bold'))
    gui.create_label(x=430, y=770, text='DEDUCTION SUMMARY:', font=('Arial', 12, 'bold'))

    # Buttons
    gui.create_button1(x=180, y=320, text='SEARCH')
    gui.create_button(x=430, y=870, text='GROSS INCOME', bg='blue')
    gui.create_button(x=528, y=870, text='NET INCOME', bg='blue')
    gui.create_button(x=620, y=870, text='SAVE', bg='cyan', fg='black')
    gui.create_button(x=698, y=870, text='UPDATE', bg='cyan', fg='black')
    gui.create_button(x=776, y=870, text='NEW', bg='yellow', fg='black')

    # Combo Box for Civil Status
    civil_status = tk.StringVar()
    civil_status_combo = ttk.Combobox(window, width=34, textvariable=civil_status)
    civil_status_combo['values'] = (' Single', ' Married', ' Widow', ' Divorced', ' Annulled')
    civil_status_combo.place(x=640, y=210)
    civil_status_combo.current()

    # Profile Image
    gui.create_image(image_path='no_profile.jpg', x=1, y=1, width=260, height=180)

    window.mainloop()

if __name__ == '__main__':
    main()