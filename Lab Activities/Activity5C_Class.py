from Activity5A_Class import StudentInfo, Assessment, FeeInputs, SectionSubjectUnit

def main():
    name = input("Enter student name: ")
    course = input("Enter student's course: ")
    student_number = input("Enter student number: ")
    year = input("Enter academic year: ")
    current_date = input("Enter the current date: ")

    student = StudentInfo(name, course, student_number, year)
    student_assessment = Assessment()

    section_subject_unit = SectionSubjectUnit(student_assessment)
    section_subject_unit.get_sections_subjects_units()
    fee_inputs = FeeInputs(student_assessment)
    fee_inputs.get_assessment_fees()

    downpayment = float(input("Enter downpayment amount: "))

    tuition_fee = student_assessment.get_tuition_fee()
    total_due = student_assessment.get_total_due(downpayment)
    assessment_amount = student_assessment.get_assessment_amount()
    payment_term = student_assessment.get_payment_per_term()
    assessment_fees = student_assessment.get_all_assessment_fees()



    print(f'''
    ***********************

    Date Printed: {current_date}
    Student name: {student.student_name}
    Course: {student.student_course}
    Student Number: {student.student_number}
    Academic Year: {student.academic_year}

    ***********************
    ''')

    print('\t\tASSESSMENT FEES')
    print(f'\tTuition Fee Lecture: P {tuition_fee:.2f}')

    for fee_name, fee_amount in assessment_fees:
        print(f'\t{fee_name}: P {fee_amount:.2f}')

    print(f'''
    ***********************

    Assessment Amount: P {assessment_amount:.2f}
    Downpayment: P {downpayment:.2f}

    ***********************

    Total Due: P {total_due:.2f}

    ***********************

    Prelims: P {payment_term:.2f}
    Midterm: P {payment_term:.2f}
    Finals: P {payment_term:.2f}
    ''')


if __name__ == '__main__':
    main()