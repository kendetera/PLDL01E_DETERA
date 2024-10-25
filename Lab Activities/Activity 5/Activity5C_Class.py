import Activity5_Class # call the Activity5_Class module

def main():
    # call the classes from the Activity5_Class module
    student = Activity5_Class.StudentInfo()
    assessment = Activity5_Class.Assessment(student)

    # get the values from the methods
    tuition_fee = assessment.get_tuition_fee()
    total_due = assessment.total_due()
    total_assessment_amount = assessment.total_assessment_amount()

    # call the display function
    display_student_info(student)
    display_assessment_fees(assessment, tuition_fee, total_due, total_assessment_amount)

def display_student_info(student):
    # display the student information
    print(f'''
    Student Name: {student.student_name}
    Course: {student.student_course}
    Student Number: {student.student_number}
    Academic Year: {student.academic_year}
    Date Printed: {student.date_printed}

    **************************
    ''')

def display_assessment_fees(assessment, tuition_fee, total_due, total_assessment_amount):
    # display the assessment of fees
    print(f'''
         ASSESSMENT OF FEES
    Tuition Fee Lecture: P {tuition_fee:.2f}
    ADU Chronicle: P {assessment.adu_chronicle:.2f}
    Athletic: P {assessment.athletic:.2f}
    Audio Visual Library: P {assessment.audio_visual:.2f}
    AUSG: P {assessment.ausg:.2f}
    Cultural: P {assessment.cultural_fee:.2f}
    Energy Cost, AirCon Classroom: P {assessment.energy_cost_aircon_classroom:.2f}
    Guidance: P {assessment.guidance:.2f}
    Insurance: P {assessment.insurance:.2f}
    Learning Management System: P {assessment.learning_management_system:.2f}
    Library: P {assessment.library_fee:.2f}
    Medical and Dental: P {assessment.medical_and_dental:.2f}
    Registration: P {assessment.registration:.2f}
    RSO: P {assessment.rso:.2f}
    Student Activities Fee: P {assessment.student_activities_fee:.2f}
    Student Nurturance Fee: P {assessment.student_nurturance_fee:.2f}
    Technology: P {assessment.technology_fee:.2f}
    Test Papers: P {assessment.test_papers:.2f}
    **************************

    Total Assessment: P {total_assessment_amount:.2f}
    Downpayment: P {assessment.downpayment:.2f}

    **************************

    Total Due: P {total_due:.2f}

    **************************

    Prelims: P {total_due / 3:.2f}
    Midterms: P {total_due / 3:.2f}
    Finals: P {total_due / 3:.2f}
    ''')

if __name__ == '__main__': # call the main function
    main()
