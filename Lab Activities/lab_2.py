# initialization
pagibig = 100.00

# inputs
employee_name = input("Enter name of employee: ")
department = input("Enter employee's department: ")
rate = float(input("Enter employee's rate per hour: "))
hours_per_day = float(input("Enter employee's number of working hours per day: "))
days_per_week = float(input("Enter employee's number of days per week: "))
weeks_per_month = float(input("Enter employee's number of weeks per month: "))

# formula
gross = hours_per_day * days_per_week * weeks_per_month * rate

# calculations
if 0 <= gross <= 20000:
    sss_contrib = 125.75
    philhealth_contrib = 100.00
elif 20001 <= gross <= 50000:
    sss_contrib = 2200.50
    philhealth_contrib = 1200.00
elif 50001 <= gross <= 75000:
    sss_contrib = 4800.00
    philhealth_contrib = 6800.00
else:
    sss_contrib = 5800.00
    philhealth_contrib = 8800.00

# formula
deduction = sss_contrib + pagibig + philhealth_contrib
net_income = gross - deduction

# display
print("Employee name: ", employee_name)
print("Employee department: ", department)
print("Gross income: ", gross)
print("Total deduction", deduction)
print("Net income:", net_income)
