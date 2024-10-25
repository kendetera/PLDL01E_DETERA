class StudentInfo: # Class for student information
    def __init__(self): # initialize the student information
        self.student_name = input("Enter student name: ")
        self.student_course = input("Enter student's course: ")
        self.student_number = input("Enter student number: ")
        self.academic_year = input("Enter academic year: ")
        self.date_printed = input("Enter the current date: ")
        self.num_sections = 0
        self.get_subject = []

    def get_subjects(self): # method to get the subjects
        self.num_sections = int(input("Enter number of sections: "))
        for _ in range(self.num_sections):
            section = input("Enter section: ")
            num_subjects = int(input(f'Enter number of subjects for section {section}: '))
            for _ in range(num_subjects):
                subject = input("Enter subject: ")
                units = int(input(f'Enter number of units for {subject}: '))
                self.get_subject.append((section, subject, units))

    def get_subjects_info(self): # method to get the subject information
        return self.get_subject

    def total_units(self): # method to get the total units
        return sum(units for _, _, units in self.get_subject)

class Assessment: # Class for assessment
    def __init__(self, student): # initialize the assessment values
        self.student = student
        self.downpayment = 0
        self.tuition_fee = 0
        self.total_due = 0
        self.total_units = self.student.total_units()
        self.tuition_fee_per_unit = 1551.00
        self.adu_chronicle = float(input("Enter ADU Chronicle fee: "))
        self.athletic = float(input("Enter Athletic fee: "))
        self.audio_visual = float(input("Enter Audio Visual Library fee: "))
        self.ausg = float(input("Enter AUSG fee: "))
        self.cultural_fee = float(input("Enter Cultural fee: "))
        self.energy_cost_aircon_classroom = float(input("Enter Energy Cost, AirCon Classroom fee: "))
        self.guidance = float(input("Enter Guidance fee: "))
        self.insurance = float(input("Enter Insurance fee: "))
        self.learning_management_system = float(input("Enter Learning Management System fee: "))
        self.library_fee = float(input("Enter Library fee: "))
        self.medical_and_dental = float(input("Enter Medical and Dental fee: "))
        self.registration = float(input("Enter Registration fee: "))
        self.rso = float(input("Enter RSO fee: "))
        self.student_activities_fee = float(input("Enter Student Activities fee: "))
        self.student_nurturance_fee = float(input("Enter Student Nurturance fee: "))
        self.technology_fee = float(input("Enter Technology fee: "))
        self.test_papers = float(input("Enter Test Papers fee: "))
        self.downpayment = float(input("Enter Downpayment amount: "))

    def get_tuition_fee(self): # method to get the tuition fee
        self.tuition_fee = self.total_units * self.tuition_fee_per_unit
        return self.tuition_fee

    def get_total_due(self): # method to get the total due
        self.total_due = self.get_total_assessment_amount() - self.downpayment
        return self.total_due

    def get_total_assessment_amount(self): # method to get the total assessment amount
        return (self.tuition_fee + self.adu_chronicle + self.athletic + self.audio_visual + self.ausg +
                self.cultural_fee + self.energy_cost_aircon_classroom + self.guidance + self.insurance +
                self.learning_management_system + self.library_fee + self.medical_and_dental + self.registration +
                self.rso + self.student_activities_fee + self.student_nurturance_fee + self.technology_fee +
                self.test_papers)
