import payroll_oop2

# instantiate payroll.oop2.py and place it inside the employee payroll.
employee_payroll = payroll_oop2.Employee_Salary()
emp_rate_per_hour = float(input("Enter Employee Rate per Hour: "))
emp_num_absences = int(input("Enter Value for Number of Absences: "))
tardiness_hours = int(input("Enter Number of Tardiness: "))

# accessing the codes under attribute get_absences_deduction inside the Employee_Salary class
absences_deduction = employee_payroll.get_absences_deduction(emp_rate_per_hour, emp_num_absences)
tardiness_deduction = employee_payroll.get_tardiness_deduction(emp_rate_per_hour, tardiness_hours)

# formula to compute partial deduction of an employee
partial_deduction = absences_deduction + tardiness_deduction
print("Employee Partial Deduction is: %.2f" % partial_deduction)
