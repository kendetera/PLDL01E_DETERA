import Activity5_Class

sections = {}

enrolment = Activity5_Class.Assessment(sections)
subject_units = enrolment.get_total_units()


print("Subjects and Units: ", subject_units)
