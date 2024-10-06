#initialization value
net_income = 0
gross_income = 0
total_deduction = 0
pagibig_contribution = 100
name_of_employee = " "

#inputting of values
name_of_employee = input("Enter name of employee:")
rate_per_hour = float(input("Enter employee's rate per hour:"))
number_hours_per_day = float(input("Enter employee's working number of hours per day:"))
number_days_per_week = int(input("Enter employee's working number of days per week:"))
number_weeks_per_month = int(input("Enter employee's working number of weeks per month:"))
SSS_contribution = (float(input("Enter employee's SSS contribution:")))
philheath_contribution = float(input("Enter employee's philhealth contribution:"))
tax_contribution = float(input("Enter employee's tax contribution:"))

#calculation for gross income, total deduction, net income
gross_income = rate_per_hour * number_hours_per_day * number_days_per_week * number_weeks_per_month
total_deduction = SSS_contribution + philheath_contribution + tax_contribution + pagibig_contribution
net_income = gross_income - total_deduction

#displaying of name of employee, net income, gross income, total deduction
print("Employee name:", name_of_employee)
print("Net income:", net_income)
print("Gross income:", gross_income)
print("Total deduction:", total_deduction)


