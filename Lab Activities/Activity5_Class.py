class StudentInfo:
    # initialization or constructor method of our class
    def __init__(self, name, course, student_number, year):
        self.student_name = name
        self.student_course = course
        self.student_number = student_number
        self.academic_year = year


class Assessment:
    def __init__(self):
        self.sections = []
        self.total_units = 0
        self.downpayment = 0
        self.tuition_fee_per_unit = 1551.00
        self.assessment_fees = []

    def add_subject(self, section, subject, units):
        self.sections.append((section, subject, units))

    def get_total_units(self):
        self.total_units = sum(units for _, _, units in self.sections)
        return self.total_units

    def get_tuition_fee(self):
        return self.get_total_units() * self.tuition_fee_per_unit

    def add_assessment_fee(self, fee_name, fee_amount):
        self.assessment_fees.append((fee_name, fee_amount))

    def get_assessment_amount(self):
        tuition_fee = self.get_tuition_fee()
        other_fees = sum(fee_amount for _, fee_amount in self.assessment_fees)
        return tuition_fee + other_fees

    def get_total_due(self, downpayment):
        self.downpayment = downpayment
        return self.get_assessment_amount() - downpayment

    def get_payment_per_term(self):
        return self.get_total_due(self.downpayment) / 3

def main():
    name = input("Enter student name: ")
    course = input("Enter student's course: ")
    student_number = input("Enter student number: ")
    year = input("Enter academic year: ")
    current_date = input("Enter the current date: ")

    student_info = StudentInfo(name, course, student_number, year)
    assessment = Assessment()

    num_sections = int(input("Enter number of sections: "))
    for _ in range(num_sections):
        section = input("Enter section: ")
        num_subjects = int(input(f'Enter number of subjects for section {section}: '))
        for _ in range(num_subjects):
            subject = input("Enter subject: ")
            units = int(input(f'Enter number of units for {subject}: '))
            assessment.add_subject(section, subject, units)

    num_fees = int(input("Enter number of other assessment fees: "))
    for _ in range(num_fees):
        fee_name = input("Enter name of fee: ")
        fee_amount = float(input(f'Enter the amount to be paid for {fee_name}: '))
        assessment.add_assessment_fee(fee_name, fee_amount)

    downpayment = float(input("Enter downpayment amount: "))

    tuition_fee = assessment.get_tuition_fee()
    total_due = assessment.get_total_due(downpayment)
    assessment_amount = assessment.get_assessment_amount()
    payment_term = assessment.get_payment_per_term()

    print(f'''
    Date Printed: {current_date}
    Student name: {student_info.student_name}
    Course: {student_info.student_course}
    Student Number: {student_info.student_number}
    Academic Year: {student_info.academic_year}

    ***********************

    Tuition Fee Lecture: P {tuition_fee:.2f}
    Assessment Amount: P {assessment_amount:.2f}
    Total Due: P {total_due:.2f}

    ***********************

    Prelims: P {payment_term:.2f}
    Midterm: P {payment_term:.2f}
    Finals: P {payment_term:.2f}
    ''')


if __name__ == "__main__":
    main()
