# initializaton of values
hdmf_contribution = 100
philhealth_contrib = 0

# inputs
employee_name = input("Enter name of employee: \n")
employee_code = input("Enter employee code: \n")
company_name = input("Enter name of company: \n")
department = input("Enter employee's department: \n")
salary_date_cutoff = input("Enter salary date cut off: \n")
rate_per_hour = float(input("Enter employee's rate per hour: \n"))
hours_per_payday = float(input("Enter employee's number of hours per payday: \n"))
hours_overtime = float(input("Enter number of overtime hours: \n"))
hours_absent = float(input("Enter number of hours absent: \n"))
hours_tardy = float(input("Enter number of hours tardy: \n"))
hours_work = float(input("Enter number of voluntary work hours: \n"))

# calculation
basic_pay = rate_per_hour * hours_per_payday
overtime_pay = rate_per_hour * hours_overtime
absences = rate_per_hour * hours_absent
tardiness = rate_per_hour * hours_tardy
honorarium = rate_per_hour * hours_work
gross_earnings = basic_pay + overtime_pay + honorarium

# SSS contribution
if gross_earnings < 4250:
    sss_contrib = 180
elif 4250 <= gross_earnings <= 4749.99:
    sss_contrib = 202.50
elif 4750 <= gross_earnings <= 5249.99:
    sss_contrib = 225
elif 5250 <= gross_earnings <= 5749.99:
    sss_contrib = 247.50
elif 5750 <= gross_earnings <= 6249.99:
    sss_contrib = 270
elif 6250 <= gross_earnings <= 6749.99:
    sss_contrib = 292.50
elif 6750 <= gross_earnings <= 7249.99:
    sss_contrib = 315
elif 7250 <= gross_earnings <= 7749.99:
    sss_contrib = 337.50
elif 7750 <= gross_earnings <= 8249.99:
    sss_contrib = 360
elif 8250 <= gross_earnings <= 8749.99:
    sss_contrib = 382.50
elif 8750 <= gross_earnings <= 9249.99:
    sss_contrib = 405
elif 9250 <= gross_earnings <= 9749.99:
    sss_contrib = 427.50
elif 9750 <= gross_earnings <= 10249.99:
    sss_contrib = 450
elif 10250 <= gross_earnings <= 10749.99:
    sss_contrib = 472.50
elif 10750 <= gross_earnings <= 11249.99:
    sss_contrib = 495
elif 11250 <= gross_earnings <= 11749.99:
    sss_contrib = 517.50
elif 11750 <= gross_earnings <= 12249.99:
    sss_contrib = 540
elif 12250 <= gross_earnings <= 12749.99:
    sss_contrib = 562.50
elif 12750 <= gross_earnings <= 13249.99:
    sss_contrib = 585
elif 13250 <= gross_earnings <= 13749.99:
    sss_contrib = 607.50
elif 13750 <= gross_earnings <= 14249.99:
    sss_contrib = 630
elif 14250 <= gross_earnings <= 14749.99:
    sss_contrib = 652.50
elif 14750 <= gross_earnings <= 15249.99:
    sss_contrib = 675
elif 15250 <= gross_earnings <= 15749.99:
    sss_contrib = 697.50
elif 15750 <= gross_earnings <= 16249.99:
    sss_contrib = 720
elif 16250 <= gross_earnings <= 16749.99:
    sss_contrib = 742.50
elif 16750 <= gross_earnings <= 17249.99:
    sss_contrib = 765
elif 17250 <= gross_earnings <= 17749.99:
    sss_contrib = 787.50
elif 17750 <= gross_earnings <= 18249.99:
    sss_contrib = 810
elif 18250 <= gross_earnings <= 18749.99:
    sss_contrib = 832.50
elif 18750 <= gross_earnings <= 19249.99:
    sss_contrib = 855
elif 19250 <= gross_earnings <= 19749.99:
    sss_contrib = 877.50
elif 19750 <= gross_earnings <= 20249.99:
    sss_contrib = 900
elif 20250 <= gross_earnings <= 20749.99:
    sss_contrib = 900
elif 20750 <= gross_earnings <= 21249.99:
    sss_contrib = 900
elif 21250 <= gross_earnings <= 21749.99:
    sss_contrib = 900
elif 21750 <= gross_earnings <= 22249.99:
    sss_contrib = 900
elif 22250 <= gross_earnings <= 22749.99:
    sss_contrib = 900
elif 22750 <= gross_earnings <= 23249.99:
    sss_contrib = 900
elif 23250 <= gross_earnings <= 23749.99:
    sss_contrib = 900
elif 23750 <= gross_earnings <= 24249.99:
    sss_contrib = 900
elif 24250 <= gross_earnings <= 24749.99:
    sss_contrib = 900
elif 24750 <= gross_earnings <= 25249.99:
    sss_contrib = 900
elif 25250 <= gross_earnings <= 25749.99:
    sss_contrib = 900
elif 25750 <= gross_earnings <= 26249.99:
    sss_contrib = 900
elif 26250 <= gross_earnings <= 26749.99:
    sss_contrib = 900
elif 26750 <= gross_earnings <= 27249.99:
    sss_contrib = 900
elif 27250 <= gross_earnings <= 27749.99:
    sss_contrib = 900
elif 27750 <= gross_earnings <= 28249.99:
    sss_contrib = 900
elif 28250 <= gross_earnings <= 28749.99:
    sss_contrib = 900
elif 28750 <= gross_earnings <= 29249.99:
    sss_contrib = 900
elif 29250 <= gross_earnings <= 29749.99:
    sss_contrib = 900

# philheath contribution
if gross_earnings < 10000:
    philhealth_contrib = 0
elif gross_earnings == 10000:
    philhealth_contrib = 500
elif 10001 <= gross_earnings <= 99999.99:
    philhealth_contrib = gross_earnings * 0.05
else:
    philhealth_contrib = 50000

# withholding tax
hey hye