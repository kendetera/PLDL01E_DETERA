def __init__(self):
    self.tuition_fee_per_unit = 1551.00
    self.num_subjects = 0
    self.student_subjects = 0


def get_student_subjects(self):
    self.num_subjects = int(input("Enter number of subjects"))

    for i in range(self.num_subjects):
        subject = input(f'Enter subject {i + 1}: ')
        units = int(input(f'Enter units for {subject}: '))
        self.student_subjects.append((subject, units))

    return self.student_subjects


self.tuition_fee = self.total_units * self.tuition_fee_per_unit
        return self.tuition_fee