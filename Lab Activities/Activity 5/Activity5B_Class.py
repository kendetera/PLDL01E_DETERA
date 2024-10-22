import Activity5_Class # import the Activity5_Class module

def main():
    # call the classes from the Activity5_Class module
    student = Activity5_Class.StudentInfo()
    assessment_amount = Activity5_Class.Assessment()
    section_subject_unit = Activity5_Class.SectionSubjectManager(assessment_amount)

    # call the methods from the classes
    section_subject_unit.get_sections_subjects_units()
    assessment_amount.get_all_assessment_fees()

    # call the display function
    display_student_info(student)
    display_sections_subjects_units(section_subject_unit)

def display_student_info(student): # display the student information
    print(f'''
    Student Name: {student.student_name}
    Course: {student.student_course}
    Student Number: {student.student_number}
    Academic Year: {student.academic_year}
    Date Printed: {student.date_printed}
    **************************
    ''')

def display_sections_subjects_units(section_subject_unit): # display the sections, subjects, and units
    for section, subject, units in section_subject_unit.get_subjects_info():
        print(f'\tSection: {section}, Subject: {subject}, Units: {units}')

# call the main function
if __name__ == "__main__":
    main()