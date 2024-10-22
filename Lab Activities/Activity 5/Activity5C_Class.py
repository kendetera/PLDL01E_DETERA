import Activity5_Class

def main():
    student = Activity5_Class.StudentInfo()
    assessment_amount = Activity5_Class.Assessment()
    fee_inputs = Activity5_Class.FeeInputs(assessment_amount)

    # call the methods from the classes
    assessment_amount.get_all_assessment_fees()
    fee_inputs.get_assessment_fees()

    # get the values from the methods
    tuition_fee = assessment_amount.get_tuition_fee()
    total_assessment = assessment_amount.get_total_assessment()
    downpayment = assessment_amount.get_downpayment()
    total_due = assessment_amount.get_total_due(downpayment)
    payment_term = assessment_amount.get_payment_per_term()

    # call the display function
    display_student_info(student)
    display_assessment_of_fees(tuition_fee, assessment_amount, total_assessment, downpayment, total_due, payment_term)

def display_student_info(student):
    # display the student information
    print(f'''
    Student Name: {student.student_name}
    Course: {student.student_course}
    Student Number: {student.student_number}
    Academic Year: {student.academic_year}
    Date Printed: {student.date_printed}
    ''')

def display_assessment_of_fees(tuition_fee, assessment_amount, total_assessment, downpayment, total_due, payment_term):
    # display the assessment of fees
    print(f'''
    ***************************\n
        ASSESSMENT OF FEES
    Tuition Fee Lecture: P {tuition_fee:.2f}
    ''')
    for fee_name, fee_amount in assessment_amount.get_all_assessment_fees():
        print(f'\t{fee_name}: P {fee_amount:.2f}')

    print(f'''
    **************************
    
    Assessment Amount: P {total_assessment:.2f}
    Downpayment: P {downpayment:.2f}
    
    **************************
    
    Total Due: P {total_due:.2f}
    
    **************************
    Prelims: P {payment_term:.2f}
    Midterms: P {payment_term:.2f}
    Finals: P {payment_term:.2f}
    ''')

# call the main function
if __name__ == "__main__":
    main()