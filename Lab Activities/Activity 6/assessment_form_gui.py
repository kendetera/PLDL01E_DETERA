from tkinter import Label, Frame, Text  # import the necessary classes from the tkinter module

class AssessmentFormGUI:  # create a class named AssessmentFormGUI
    def __init__(self, window):
        self.window = window  # initialize the window attribute

    # Method to create the first frame
    def create_frame1(self, x, y, width=1100, height=160, border=10, bg='#a2262f', relief='raised'):
        frame = Frame(self.window, width=width, height=height, border=border, bg=bg, relief=relief)  # create a Frame widget
        frame.place(x=x, y=y)  # place the frame at the specified coordinates
        return frame  # return the created frame

    # Method to create the second frame
    def create_frame2(self, x, y, width=1100, height=100, border=10, bg='#a2262f', relief='raised'):
        frame = Frame(self.window, width=width, height=height, border=border, bg=bg, relief=relief)  # create a Frame widget
        frame.place(x=x, y=y)  # place the frame at the specified coordinates
        return  # no return value

    # Method to create the third frame
    def create_frame3(self, x, y, width=1100, height=350, border=10, bg='#a2262f', relief='raised'):
        frame = Frame(self.window, width=width, height=height, border=border, bg=bg, relief=relief)  # create a Frame widget
        frame.place(x=x, y=y)  # place the frame at the specified coordinates
        return frame  # return the created frame

    # Method to create the first type of textbox
    def create_textbox1(self, x, y, width=25, height=1, fg='black', bg='white', font=('Arial', 11)):
        textbox = Text(self.window, width=width, height=height, fg=fg, bg=bg, font=font)  # create a Text widget
        textbox.place(x=x, y=y)  # place the textbox at the specified coordinates
        return textbox  # return the created textbox

    # Method to create the second type of textbox
    def create_textbox2(self, x, y, width=22, height=1, fg='black', bg='white', font=('Arial', 11)):
        textbox = Text(self.window, width=width, height=height, fg=fg, bg=bg, font=font)  # create a Text widget
        textbox.place(x=x, y=y)  # place the textbox at the specified coordinates
        return textbox  # return the created textbox

    # Method to create a label
    def create_label(self, x, y, text, fg='white', bg='#a2262f', font=('Times New Roman', 12, 'bold')):
        label = Label(self.window, text=text, fg=fg, bg=bg, font=font)  # create a Label widget
        label.place(x=x, y=y)  # place the label at the specified coordinates
        return label  # return the created label