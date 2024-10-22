class StudentInfo: # Class for student information
    def __init__(self): #
        self.student_name = input("Enter student name: ")
        self.student_course = input("Enter student's course: ")
        self.student_number = input("Enter student number: ")
        self.academic_year = input("Enter academic year: ")
        self.date_printed = input("Enter the current date: ")

class Assessment: # Class for assessment
    def __init__(self): # initialize the attributes
        self.assessment_fees = []
        self.total_units = 0
        self.downpayment = 0
        self.tuition_fee_per_unit = 1551.00

    def get_tuition_fee(self): # method to get the tuition fee
        return self.total_units * self.tuition_fee_per_unit

    def get_downpayment(self): # method to get the down payment
        self.downpayment = float(input("Enter downpayment amount: "))
        return self.downpayment

    def get_total_due(self, downpayment): # method to get the total due
        self.downpayment = downpayment
        return self.get_total_assessment() - self.downpayment

    def get_payment_per_term(self): # method to get the payment per term
        return self.get_total_due(self.downpayment) / 3

    def add_assessment_fee(self, fee_name, fee_amount): # method to add assessment fees
        self.assessment_fees.append((fee_name, fee_amount))

    def get_all_assessment_fees(self): # method to get all assessment fee amounts
        return self.assessment_fees

    def add_units(self, units): # method to add units to calculate the tuition fee
        self.total_units += units

    def get_total_assessment(self): # method to get the total assessment amount
        total_fees = sum(fee_amount for _, fee_amount in self.assessment_fees)
        return self.get_tuition_fee() + total_fees

class SectionSubjectManager: # class for sections, subjects, and units
    def __init__(self, assessment): # initialize the attributes
        self.assessment = assessment
        self.sections = []
        self.num_sections = 0
        self.total_units = 0

    def get_sections_subjects_units(self): # method to get the sections, subjects, and units
        self.num_sections = int(input("Enter number of sections: "))
        for _ in range(self.num_sections):
            section = input("Enter section: ")
            num_subjects = int(input(f'Enter number of subjects for section {section}: '))
            for _ in range(num_subjects):
                subject = input("Enter subject: ")
                units = int(input(f'Enter number of units for {subject}: '))
                self.get_subject(section, subject, units)

    def get_subject(self, section, subject, units): # method to get the subject
        self.sections.append((section, subject, units))
        self.assessment.add_units(units)  # Sync units with Assessment

    def get_subjects_info(self): # method to get the subjects information
        return self.sections

class FeeInputs: # class for assessment fees
    def __init__(self, assessment): # initialize the attributes
        self.assessment = assessment

    def get_assessment_fees(self): # method to get the assessment fees
        num_fees = int(input("Enter number of other assessment fees: "))
        for _ in range(num_fees):
            fee_name = input("Enter name of fee: ")
            fee_amount = float(input(f'Enter the amount to be paid for {fee_name}: '))
            self.assessment.add_assessment_fee(fee_name, fee_amount)
