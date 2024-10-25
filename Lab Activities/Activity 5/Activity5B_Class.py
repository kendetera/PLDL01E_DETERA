import Activity5_Class # import the Activity5_Class module

def main():
    # call the classes from the Activity5_Class module
    student = Activity5_Class.StudentInfo()

    # call the method from the class
    student.get_subjects()

    # call the display function
    display_student_info(student)
    display_sections_subjects_units(student)

def display_student_info(student): # display the student information
    print(f'''
    Student Name: {student.student_name}
    Course: {student.student_course}
    Student Number: {student.student_number}
    Academic Year: {student.academic_year}
    Date Printed: {student.date_printed}
    
    **************************
    ''')

def display_sections_subjects_units(student): # display the sections, subjects, and corresponding units
    for section, subject, units in student.get_subjects_info():
        print(f'\tSection: {section}, Subject: {subject}, Units: {units}')
    print(f'\tTotal Units: {student.total_units()}') # display the total units

# call the main function
if __name__ == "__main__":
    main()