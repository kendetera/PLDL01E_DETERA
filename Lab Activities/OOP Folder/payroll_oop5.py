# calling of payroll_oop2.py
# test push
import payroll_oop2

# Create an instance of the Employee_Salary class:
payroll1 = payroll_oop2.Employee_Salary()
emp_rate_per_hour = float(input("Enter Employee Rate per Hour: "))
emp_hour_overtime = float(input("Enter Employee's Number of Overtime Hours: "))
emp_tardiness = float(input("Enter the Number of Tardiness in Hours: "))

# calculate tardiness deduction and overtime pay
tardiness_deduction = payroll1.get_tardiness_deduction(emp_rate_per_hour, emp_tardiness)
overtime_pay = payroll1.get_overtime_pay(emp_rate_per_hour, emp_hour_overtime)

# display of results
print("Employee Tardiness Deduction is: %.2f" % tardiness_deduction)
print("Employee Overtime Pay is: %.2f" % overtime_pay)
