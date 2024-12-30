import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class EmployeeRegistrationGUI:
    def __init__(self, window):
        self.window = window
        self.window.title('Employee Registration')
        self.window.geometry("900x800")
        self.window.configure(bg='#f2f0e3')

        # Heading
        self.heading = tk.Label(self.window,
                                text="Se-Ri's Employee's Personal Information",
                                fg='black',
                                bg='#f2f0e3',
                                font=('Times New Roman', 22, 'bold'))
        self.heading.pack(pady=20)

        # Frames
        self.frame1 = tk.Frame(self.window, width=800, height=130, border=0, bg='#f8f3f3', relief='raised', borderwidth=5)
        self.frame1.place(x=50, y=80)
        self.frame2 = tk.Frame(self.window, width=800, height=130, border=0, bg='#f8f3f3', relief='raised', borderwidth=5)
        self.frame2.place(x=50, y=220)
        self.frame3 = tk.Frame(self.window, width=800, height=110, border=0, bg='#f8f3f3', relief='raised', borderwidth=5)
        self.frame3.place(x=50, y=380)
        self.frame4 = tk.Frame(self.window, width=800, height=220, border=0, bg='#f8f3f3', relief='raised', borderwidth=5)
        self.frame4.place(x=50, y=520)

        # Image
        self.image = Image.open("no_profile.jpg")
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((120, 120)))
        self.profile_icon = tk.Label(self.window, image=self.bck_pic, borderwidth=2, relief='solid')
        self.profile_icon.place(x=60, y=25)

        # Labels and Textboxes in Frame 1
        self.no_file_chosen = tk.Label(self.window, text="No File Chosen", bg='#f8f3f3', font=('Arial', 10))
        self.no_file_chosen.place(x=75, y=182)
        self.first_name = tk.Label(self.window, text="First Name", bg='#f8f3f3', font=('Arial', 10))
        self.first_name.place(x=200, y=90)
        self.middle_name = tk.Label(self.window, text="Middle Name", bg='#f8f3f3', font=('Arial', 10))
        self.middle_name.place(x=390, y=90)
        self.last_name = tk.Label(self.window, text="Last Name", bg='#f8f3f3', font=('Arial', 10))
        self.last_name.place(x=520, y=90)
        self.suffix = tk.Label(self.window, text="Suffix", bg='#f8f3f3', font=('Arial', 10))
        self.suffix.place(x=710, y=90)
        self.date_of_birth = tk.Label(self.window, text="Date of Birth", bg='#f8f3f3', font=('Arial', 10))
        self.date_of_birth.place(x=200, y=140)
        self.gender = tk.Label(self.window, text="Gender", bg='#f8f3f3', font=('Arial', 10))
        self.gender.place(x=420, y=140)
        self.nationality = tk.Label(self.window, text="Nationality", bg='#f8f3f3', font=('Arial', 10))
        self.nationality.place(x=550, y=140)
        self.civil_status = tk.Label(self.window, text="Civil Status", bg='#f8f3f3', font=('Arial', 10))
        self.civil_status.place(x=680, y=140)

        self.first_name_entry = ttk.Entry(self.window, width=30, font=('Arial', 8))
        self.first_name_entry.place(x=200, y=110)
        self.middle_name_entry = ttk.Entry(self.window, width=20, font=('Arial', 8))
        self.middle_name_entry.place(x=390, y=110)
        self.last_name_entry = ttk.Entry(self.window, width=30, font=('Arial', 8))
        self.last_name_entry.place(x=520, y=110)
        self.suffix_entry = ttk.Entry(self.window, width=20, font=('Arial', 8))
        self.suffix_entry.place(x=710, y=110)

        self.gender_entry = ttk.Entry(self.window, width=20, font=('Arial', 8))
        self.gender_entry.place(x=420, y=160)
        self.nationality_entry = ttk.Entry(self.window, width=20, font=('Arial', 8))
        self.nationality_entry.place(x=550, y=160)
        self.civil_status_entry = ttk.Entry(self.window, width=25, font=('Arial', 8))
        self.civil_status_entry.place(x=680, y=160)

        # Labels and Textboxes in Frame 2
        self.department = tk.Label(self.window, text="Department", bg='#f8f3f3', font=('Arial', 10))
        self.department.place(x=75, y=230)
        self.designation = tk.Label(self.window, text="Designation", bg='#f8f3f3', font=('Arial', 10))
        self.designation.place(x=387, y=230)
        self.qualified_dependents_status = tk.Label(self.window, text="Qualified Dep. Status", bg='#f8f3f3', font=('Arial', 10))
        self.qualified_dependents_status.place(x=610, y=230)
        self.employee_status = tk.Label(self.window, text="Employee Status", bg='#f8f3f3', font=('Arial', 10))
        self.employee_status.place(x=75, y=280)
        self.pay_date = tk.Label(self.window, text="Pay Date", bg='#f8f3f3', font=('Arial', 10))
        self.pay_date.place(x=448, y=280)
        self.employee_number = tk.Label(self.window, text="Employee Number", bg='#f8f3f3', font=('Arial', 10))
        self.employee_number.place(x=610, y=280)

        self.department_entry = ttk.Entry(self.window, width=50, font=('Arial', 8))
        self.department_entry.place(x=75, y=250)
        self.designation_entry = ttk.Entry(self.window, width=35, font=('Arial', 8))
        self.designation_entry.place(x=387, y=250)
        self.qualified_dependents_status_entry = ttk.Entry(self.window, width=37, font=('Arial', 8))
        self.qualified_dependents_status_entry.place(x=610, y=250)
        self.employee_status_entry = ttk.Entry(self.window, width=60, font=('Arial', 8))
        self.employee_status_entry.place(x=75, y=300)
        self.pay_date_entry = ttk.Entry(self.window, width=25, font=('Arial', 8))
        self.pay_date_entry.place(x=448, y=300)
        self.employee_number_entry = ttk.Entry(self.window, width=37, font=('Arial', 8))
        self.employee_number_entry.place(x=610, y=300)

        # Labels and Textboxes in Frame 3
        self.contact_info = tk.Label(self.window, text="Contact Info:", fg='black', font=('Times New Roman', 12, 'bold'))
        self.contact_info.place(x=50, y=355)
        self.contact_no = tk.Label(self.window, text="Contact No.", bg='#f8f3f3', font=('Arial', 10))
        self.contact_no.place(x=75, y=390)
        self.email = tk.Label(self.window, text="Email", bg='#f8f3f3', font=('Arial', 10))
        self.email.place(x=390, y=390)
        self.other = tk.Label(self.window, text="Other(Social Media)", bg='#f8f3f3', font=('Arial', 10))
        self.other.place(x=75, y=435)
        self.soc_med_acc = tk.Label(self.window, text="Social Media Account ID/No.", bg='#f8f3f3', font=('Arial', 10))
        self.soc_med_acc.place(x=390, y=435)

        self.contact_no_entry = ttk.Entry(self.window, width=50, font=('Arial', 8))
        self.contact_no_entry.place(x=75, y=410)
        self.email_entry = ttk.Entry(self.window, width=73, font=('Arial', 8))
        self.email_entry.place(x=390, y=410)
        self.other_entry = ttk.Entry(self.window, width=50, font=('Arial', 8))
        self.other_entry.place(x=75, y=455)
        self.soc_med_acc_entry = ttk.Entry(self.window, width=73, font=('Arial', 8))
        self.soc_med_acc_entry.place(x=390, y=455)

        # Labels and Textboxes in Frame 4
        self.address = tk.Label(self.window, text="Address:", fg='black', font=('Times New Roman', 12, 'bold'))
        self.address.place(x=50, y=495)
        self.add_line1 = tk.Label(self.window, text="Address Line 1", bg='#f8f3f3', font=('Arial', 10))
        self.add_line1.place(x=75, y=525)
        self.add_line2 = tk.Label(self.window, text="Address Line 2", bg='#f8f3f3', font=('Arial', 10))
        self.add_line2.place(x=75, y=565)
        self.city_municipality = tk.Label(self.window, text="City/Municipality", bg='#f8f3f3', font=('Arial', 10))
        self.city_municipality.place(x=75, y=605)
        self.state_province = tk.Label(self.window, text="State/Province", bg='#f8f3f3', font=('Arial', 10))
        self.state_province.place(x=458, y=605)
        self.country = tk.Label(self.window, text="Country", bg='#f8f3f3', font=('Arial', 10))
        self.country.place(x=75, y=643)
        self.zip_code = tk.Label(self.window, text="Zip Code", bg='#f8f3f3', font=('Arial', 10))
        self.zip_code.place(x=458, y=643)
        self.pic_path = tk.Label(self.window, text="Picture Path", bg='#f8f3f3', font=('Arial', 10))
        self.pic_path.place(x=75, y=680)

        self.add_line1_entry = ttk.Entry(self.window, width=126, font=('Arial', 8))
        self.add_line1_entry.place(x=75, y=545)
        self.add_line2_entry = ttk.Entry(self.window, width=126, font=('Arial', 8))
        self.add_line2_entry.place(x=75, y=585)
        self.city_municipality_entry = ttk.Entry(self.window, width=62, font=('Arial', 8))
        self.city_municipality_entry.place(x=75, y=625)
        self.state_province_entry = ttk.Entry(self.window, width=62, font=('Arial', 8))
        self.state_province_entry.place(x=458, y=625)
        self.country_entry = ttk.Entry(self.window, width=62, font=('Arial', 8))
        self.country_entry.place(x=75, y=663)
        self.zip_code_entry = ttk.Entry(self.window, width=62, font=('Arial', 8))
        self.zip_code_entry.place(x=458, y=663)
        self.pic_path_entry = ttk.Entry(self.window, width=126, font=('Arial', 8))
        self.pic_path_entry.place(x=75, y=700)

        # Buttons
        self.upload_button = tk.Button(self.window, width=10, padx=10, text='Choose File',
                                       bg='white', fg='black', cursor='hand2', border=5)
        self.upload_button.place(x=63, y=150)
        self.save_button = tk.Button(self.window, width=10, padx=10, text='Save',
                                     bg='#007bff', fg='white', cursor='hand2', border=5)
        self.save_button.place(x=50, y=750)
        self.cancel_button = tk.Button(self.window, width=10, padx=10, text='Cancel',
                                       bg='white', fg='black', cursor='hand2', border=5)
        self.cancel_button.place(x=160, y=750)

        # Combo boxes
        # Date of Birth Combo boxes
        self.day_combo = ttk.Combobox(self.window, width=5)
        self.day_combo['values'] = [str(i) for i in range(1, 32)] # dropdown list of days from 1 to 31
        self.day_combo.place(x=200, y=160)
        self.day_combo.current()

        self.month_combo = ttk.Combobox(self.window, width=10)
        self.month_combo['values'] = ['January', 'February', 'March', 'April',
                                      'May', 'June', 'July', 'August', 'September',
                                      'October', 'November', 'December']
        self.month_combo.place(x=260, y=160)
        self.month_combo.current()

        self.year_combo = ttk.Combobox(self.window, width=7)
        self.year_combo['values'] = [str(i) for i in range(1900, 2026)]  # dropdown list of years from 1900 to 2025
        self.year_combo.place(x=350, y=160)
        self.year_combo.current()

        # Gender combo box
        self.gender_combo = ttk.Combobox(self.window, width=17)
        self.gender_combo['values'] = ('Male', 'Female')
        self.gender_combo.place(x=422, y=160)
        self.gender_combo.current()

        self.civil_status_combo = ttk.Combobox(self.window, width=22)
        self.civil_status_combo['values'] = ('Single', 'Married', 'Widow', 'Divorced', ' Annulled')
        self.civil_status_combo.place(x=680, y=160)
        self.civil_status_combo.current()

        self.nationality_combo = ttk.Combobox(self.window, width=17)
        self.nationality_combo['values'] = (
            'American', 'Argentinian', 'Australian', 'Bangladeshi', 'Brazilian', 'British', 'Canadian', 'Chilean',
            'Chinese', 'Colombian', 'Dutch', 'Egyptian', 'Filipino', 'French', 'German', 'Greek', 'Indian', 'Indonesian',
            'Iraqi', 'Italian', 'Japanese', 'Kenyan', 'Korean', 'Malaysian', 'Mexican', 'Nigerian','Pakistani',
            'Peruvian', 'Polish', 'Portuguese', 'Russian', 'Singaporean', 'South African', 'Spanish',
            'Sri Lankan', 'Swedish', 'Thai', 'Turkish', 'Ukrainian', 'Venezuelan', 'Vietnamese')
        self.nationality_combo.place(x=550, y=160)
        self.nationality_combo.current()

        self.social_media_combo = ttk.Combobox(self.window, width=47)
        self.social_media_combo['values'] = ('Facebook', 'Instagram', 'Twitter', 'Youtube', ' Tiktok', 'Snapchat',
                                             'Pinterest', 'Messenger', 'Telegram', 'Twitch')
        self.social_media_combo.place(x=75, y=455)
        self.social_media_combo.current()

        self.country_combo = ttk.Combobox(self.window, width=59)
        self.country_combo['values'] = ('Brazil', 'Cambodia', 'China', 'Indonesia', 'Japan', 'Russia', 'Philippines',
                                        'Poland', 'Portugal', 'South Korea', 'Thailand', 'United States', 'Vietnam')
        self.country_combo.place(x=75, y=663)
        self.country_combo.current()

if __name__ == "__main__":
    window = tk.Tk()
    _app = EmployeeRegistrationGUI(window)
    window.mainloop()