import tkinter as tk
from PIL import Image, ImageTk  # import the Image and ImageTk classes from the PIL module
from assessment_form_gui import AssessmentFormGUI  # import the AssessmentFormGUI class

def main():
    window = tk.Tk()  # create the main window
    window.title("Assessment Form")  # set the window title
    window.geometry('1920x1080')  # set the window size
    window.configure(bg='#807F7D')  # set the window background color

    image = Image.open('LPU_Banner.png')  # open the image file
    bck_pic = ImageTk.PhotoImage(image.resize((1200, 140)))  # resize the image and convert it to a PhotoImage object
    lbl = tk.Label(window, image=bck_pic, bg='#807F7D')  # create a Label widget to display the image
    lbl.place(x=1, y=1)  # place the label at the specified coordinates

    gui = AssessmentFormGUI(window)  # initialize the AssessmentFormGUI class

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

    # Create labels in the third frame
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

    window.mainloop()  # start the Tkinter event loop

if __name__ == '__main__':
    main()  # call the main function