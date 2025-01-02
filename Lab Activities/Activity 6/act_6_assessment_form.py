import tkinter as tk
from tkinter import Label, Frame, Text
from PIL import Image, ImageTk

class GuiDesign:
    def __init__(self, window):
        self.window = window

    def create_frame1(self, x, y, width=1100, height=160, border=10, bg='#a2262f', relief='raised'):
        frame = Frame(self.window, width=width, height=height, border=border, bg=bg, relief='raised')
        frame.place(x=x, y=y)
        return frame

    def create_frame2(self, x, y, width=1100, height=100, border=10, bg='#a2262f', relief='raised'):
        frame = Frame(self.window, width=width, height=height, border=border, bg=bg, relief='raised')
        frame.place(x=x, y=y)
        return

    def create_frame3(self, x, y, width=1100, height=350, border=10, bg='#a2262f', relief='raised'):
        frame = Frame(self.window, width=width, height=height, border=border, bg=bg, relief='raised')
        frame.place(x=x, y=y)
        return frame

    def create_textbox1(self, x, y, width=25, height=1, fg='black', bg='white', font=('Arial', 11)):
        textbox = Text(self.window, width=width, height=height, fg=fg, bg=bg, font=font)
        textbox.place(x=x, y=y)
        return textbox

    def create_textbox2(self, x, y, width=22, height=1, fg='black', bg='white', font=('Arial', 11)):
        textbox = Text(self.window, width=width, height=height, fg=fg, bg=bg, font=font)
        textbox.place(x=x, y=y)
        return textbox

    def create_label(self, x, y, text, fg='white', bg='#a2262f', font=('Times New Roman', 12, 'bold')):
        label = Label(self.window, text=text, fg=fg, bg=bg, font=font)
        label.place(x=x, y=y)
        return label

def main():
    window = tk.Tk()
    window.title("Assessment Form")
    window.geometry('1920x1080')
    window.configure(bg='#807F7D')

    # Open the image file
    image = Image.open('LPU_Banner.png')
    # Resize the image
    bck_pic = ImageTk.PhotoImage(image.resize((1200, 140)))
    # Create a label to display the image
    lbl = tk.Label(window, image=bck_pic, bg='#807F7D')
    lbl.place(x=1, y=1)

    gui = GuiDesign(window)

    # Create frames
    gui.create_frame1(220, 220)
    gui.create_frame2(220, 400)
    gui.create_frame3(220, 520)

    # Create textboxes in the first frame
    gui.create_textbox1(300, 262)
    gui.create_textbox1(630, 262)
    gui.create_textbox1(950, 262)
    gui.create_textbox1(300, 330)
    gui.create_textbox1(630, 330)

    # Create textboxes in the second frame
    gui.create_textbox1(300, 447)
    gui.create_textbox1(630, 447)
    gui.create_textbox1(950, 447)

    # Create textboxes in the third frame
    gui.create_textbox2(300, 580)
    gui.create_textbox2(550, 580)
    gui.create_textbox2(800, 580)
    gui.create_textbox2(1050, 580)
    gui.create_textbox2(300, 650)
    gui.create_textbox2(550, 650)
    gui.create_textbox2(800, 650)
    gui.create_textbox2(1050, 650)
    gui.create_textbox2(300, 720)
    gui.create_textbox2(550, 720)
    gui.create_textbox2(800, 720)
    gui.create_textbox2(1050, 720)
    gui.create_textbox2(300, 790)
    gui.create_textbox2(550, 790)
    gui.create_textbox2(800, 790)
    gui.create_textbox2(1050, 790)


    # Create labels in the first frame
    gui.create_label(300, 235, 'Student Name')
    gui.create_label(630, 235, 'Student Number')
    gui.create_label(950, 235, 'Student Course')
    gui.create_label(300, 305, 'Academic Year')
    gui.create_label(630, 305, 'Current Date')

    # Create labels in the second frame
    gui.create_label(300, 420, 'Section')
    gui.create_label(630, 420, 'Subjects')
    gui.create_label(950, 420, 'Units')

    # crate labels in the third frame
    gui.create_label(300, 550, 'ADU Chronicle Fee')
    gui.create_label(550, 550, 'Athletic Fee')
    gui.create_label(800, 550, 'Audio Visual Library Fee')
    gui.create_label(1050, 550, 'AUSG Fee')
    gui.create_label(300, 620, 'Cultural Fee')
    gui.create_label(550, 620, 'Energy Cost, AirCon Classroom Fee')
    gui.create_label(800, 620, 'Guidance Fee')
    gui.create_label(1050, 620, 'Insurance Fee')
    gui.create_label(300, 690, 'Learning Management System Fee')
    gui.create_label(550, 690, 'Library Fee')
    gui.create_label(800, 690, 'Medical and Dental Fee')
    gui.create_label(1050, 690, 'Registration Fee')
    gui.create_label(300, 760, 'RSO Fee')
    gui.create_label(550, 760, 'Student Activities Fee')
    gui.create_label(800, 760, 'Student Nurturance Fee')
    gui.create_label(1050, 760, 'Technology Fee')

    window.mainloop()

if __name__ == '__main__':
    main()