class StudentInfo:
    # initialization or constructor method of our class
    def __init__(self, name, course, student_number, year):
        self.student_name = name
        self.student_course = course
        self.student_number = student_number
        self.academic_year = year


class Assessment:
    # initialization or constructor method of our class
    def __init__(self, sections):
        self.sections = sections
        self.total_units = 0
        self.tuition_fee = 0
        self.tuition_fee_per_unit = 1551.00
        self.assessment_fees = {}

    def add_subjects(self, section, subject, units):
        # giving our Assessment class a method of adding subjects and units
        if section not in self.sections:
            self.sections = []
        self.sections[section].append({'subject': subject, 'units': units})

    def get_total_units(self):
        # giving our Assessment class a method for getting total units
        self.total_units = 0
        for section_data in self.sections.values():
            for subject_data in section_data:
                self.total_units += subject_data['units']

    def get_tuition_fee(self):
        # giving our class a method for computing the tuition fee
        total_units = sum(subject['units'] for section in self.sections.values() for subject in section)
        return total_units * self.tuition_fee_per_unit

    def get_assessment_amount(self):
        # giving our class a method for calculating the amount of total assessment
        tuition_fee = self.get_tuition_fee()
        other_fees = sum(self.assessment_fees.values())
        return tuition_fee + other_fees

    def get_total_due(self, downpayment):
        assessment_amount = self.get_assessment_amount()
        return assessment_amount + downpayment

    def get_payment_per_term(self, total_due):
        return total_due / 3


def main():
    # input of student details
    name = input("Enter student name: ")
    course = input("Enter student's course: ")
    student_number = input("Enter student number: ")
    year = input("Enter academic year: ")

    student = StudentInfo(name, course, student_number, year)

    # input of current date
    current_date = input("Enter the current date: ")
    print(f'Date Printed: {current_date}')

    # input of sections, subjects, and units
    sections = {}
    num_sections = int(input("Enter number of sections: "))
    for i in range(num_sections):
        section = input("Enter section: ")
        num_subjects = int(input(f'Enter number of subjects for section {section}: '))
        for j in range(num_subjects):
            subject = input("Enter subject: ")
            units = int(input(f'Enter number of units for {subject}: '))
            if section not in sections:
                sections[section] = []
            sections[section].append({'subject': subject, 'units': units})

    assessment = Assessment(sections)

    # input of assessment fees except tuition fee lecture
    num_fees = int(input("Enter number of other assessment fees: "))
    for k in range(num_fees):
        fee_name = input("Enter name of fee: ")
        fee_amount = float(input(f'Enter the amount to be paid for {fee_name}: '))
        assessment.assessment_fees[fee_name] = fee_amount

    # compute of tuition fee lecture
    tuition_fee = assessment.get_tuition_fee()
    print(f'\nTuition Fee Lecture: P {tuition_fee:.2f}\n')

    # input downpayment
    downpayment = float(input("Enter downpayment amount: "))

    # compute of assessment amount
    assessment_amount = assessment.get_total_due(downpayment)
    print(f'\nTotal Due: P {assessment_amount:.2f}\n')

    # compute payment per term
    payment_term = assessment.get_payment_per_term(assessment_amount)
    print(f'Prelims: P {payment_term: .2f}')
    print(f'Midterm: P {payment_term: .2f}')
    print(f'Finals: P {payment_term: .2f}')


if __name__ == "__main__":
    main()
