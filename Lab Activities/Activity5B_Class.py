from Activity5A_Class import StudentInfo, SectionSubjectUnit, Assessment

def main():
    name = input("Enter student name: ")
    course = input("Enter student's course: ")
    student_number = input("Enter student number: ")
    year = input("Enter academic year: ")
    current_date = input("Enter the current date: ")

    student = StudentInfo(name, course, student_number, year)
    student_assessment = Assessment()
    sections_subjects_unit = SectionSubjectUnit(student_assessment)


    sections_subjects_unit.get_sections_subjects_units()
    subjects_info = sections_subjects_unit.get_subjects_info()
    total_unit = sections_subjects_unit.get_total_units()

    print(f'''
    ***********************

    Date Printed: {current_date}
    Student name: {student.student_name}
    Course: {student.student_course}
    Student Number: {student.student_number}
    Academic Year: {student.academic_year}

    ***********************
    ''')

    for section, subject, units in subjects_info:
        print(f'\tSection: {section}, Subject: {subject}, Units: {units}')
    print(f'\tTotal Units: {total_unit}\n')



if __name__ == '__main__':
    main()