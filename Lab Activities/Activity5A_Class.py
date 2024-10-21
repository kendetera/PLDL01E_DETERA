class StudentInfo:
    def __init__(self, name, course, student_number, year):
        self.student_name = name
        self.student_course = course
        self.student_number = student_number
        self.academic_year = year

class Assessment:
    def __init__(self):
        self.sections = []
        self.assessment_fees = []
        self.total_units = 0
        self.downpayment = 0
        self.tuition_fee_per_unit = 1551.00

    def get_subject(self, section, subject, units):
        self.sections.append((section, subject, units))

    def get_total_units(self):
        self.total_units = sum(units for _, _, units in self.sections)
        return self.total_units

    def get_tuition_fee(self):
        return self.get_total_units() * self.tuition_fee_per_unit

    def get_total_due(self, downpayment):
        self.downpayment = downpayment
        return self.get_tuition_fee() - self.downpayment

    def get_assessment_amount(self):
        return self.get_tuition_fee()

    def get_payment_per_term(self):
        return self.get_total_due(self.downpayment) / 3

    def get_assessment_fees(self, fee_name, fee_amount):
        self.assessment_fees.append((fee_name, fee_amount))

    def get_all_assessment_fees(self):
        return self.assessment_fees

class SectionSubjectUnit:
    def __init__(self, assessment):
        self.assessment = assessment
        self.num_sections = 0
        self.num_subjects = 0
        self.total_units = 0

    def get_sections_subjects_units(self):
        self.num_sections = int(input("Enter number of sections: "))
        for _ in range(self.num_sections):
            section = input("Enter section: ")
            num_subjects = int(input(f'Enter number of subjects for section {section}: '))
            self.num_subjects += num_subjects
            for _ in range(num_subjects):
                subject = input("Enter subject: ")
                units = int(input(f'Enter number of units for {subject}: '))
                self.total_units += units
                self.assessment.get_subject(section, subject, units)

    def get_total_units(self):
        return self.total_units

    def get_subjects_info(self):
        return self.assessment.sections

class FeeInputs:
    # initialization or constructor method of our class
    def __init__(self, assessment):
        self.assessment = assessment

    def get_assessment_fees(self):
        # input of other assessment fees
        num_fees = int(input("Enter number of other assessment fees: "))
        for _ in range(num_fees):
            fee_name = input("Enter name of fee: ")
            fee_amount = float(input(f'Enter the amount to be paid for {fee_name}: '))
            self.assessment.get_assessment_fees(fee_name, fee_amount)

def main():
    # input student information
    name = input("Enter student name: ")
    course = input("Enter student's course: ")
    student_number = input("Enter student number: ")
    year = input("Enter academic year: ")
    current_date = input("Enter the current date: ")

    # create instances of the classes
    student = StudentInfo(name, course, student_number, year)
    student_assessment = Assessment()
    section_subject_unit = SectionSubjectUnit(student_assessment)
    fee_inputs = FeeInputs(student_assessment)

    # input sections, subjects, and units
    section_subject_unit.get_sections_subjects_units()

    # input assessment fees
    fee_inputs.get_assessment_fees()

    # input down payment amount
    downpayment = float(input("Enter downpayment amount: "))

    # calculate fees and payments
    tuition_fee = student_assessment.get_tuition_fee()
    total_due = student_assessment.get_total_due(downpayment)
    assessment_amount = student_assessment.get_assessment_amount()
    payment_term = student_assessment.get_payment_per_term()

    # get number of sections, subjects, and total units
    total_unit = section_subject_unit.get_total_units()
    subjects_info = section_subject_unit.get_subjects_info()
    assessment_fees = student_assessment.get_all_assessment_fees()

    # print the output
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

    print('\t\t***********************\n\n\t\tASSESSMENT FEES')
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