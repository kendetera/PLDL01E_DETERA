class CustomerInfo:
    def __init__(self):
        # initialize  inputs
        self.customer_name = input("Enter customer name: ")
        self.customer_street_address = input("Enter customer street address: ")
        self.customer_barangay_address = input("Enter customer barangay address: ")
        self.customer_municipality = input("Enter customer municipality: ")
        self.customer_city = input("Enter customer city: ")
        self.customer_account_number = input("Enter customer account number: ")


class ElectricBill:
    def __init__(self):
        # initialize values for electric bill status
        self.amount_due = int(input("Enter amount due: "))
        self.remaining_balance = int(input("Enter remaining balance: "))
        self.total_amount_due = 0
        self.previous_billing_info = ''

    def get_previous_billing_info(self):
        # this method determines if there is still a remaining balance of the customer
        if self.remaining_balance == 0:
            return "Thank You"  # if the remaining balance is only equal to 0
        else:
            return "Please pay your remaining balance"  # if remaining balance is greater than 0

    def get_total_amount_due(self):  # calculate for the total amount due
        self.total_amount_due = self.amount_due + self.remaining_balance
        return self.total_amount_due


class ServiceInfo:
    def __init__(self, customer):
        # initialize our values for service info status
        self.customer = customer
        self.service_id_number = self.customer.customer_account_number
        self.rate = input("Residential or Business: ")
        self.contact_in_the_name_of = self.customer.customer_name
        self.service_street_address = self.customer.customer_street_address
        self.service_barangay_address = self.customer.customer_barangay_address
        self.service_municipality = self.customer.customer_municipality
        self.service_city = self.customer.customer_city


class BillingInfo:
    def __init__(self, bill):
        # initialize our values for billing info status
        self.bill = bill
        self.amount_due = 0
        self.bill_date = input("Enter Bill Date: ")
        self.meter_reading_date = input("Enter meter reading date: ")
        self.bill_period = input("Enter bill period: ")
        self.due_date = input("Enter due date: ")
        self.rate_per_kwh = float(input("Enter rate per kwh: "))
        self.total_kwh = float(input("Enter Total KWH: "))
        self.total_current_amount = self.bill.total_amount_due
        self.next_meter_reading = input("Enter next meter reading date: ")

    def get_amount_due(self):
        self.amount_due = self.rate_per_kwh * self.total_kwh
        return self.amount_due


class BillComputationSummary:
    def __init__(self):
        # gather inputs or amounts for each charges
        self.generation = input("Enter Generation charge: ")
        self.transmission = input("Enter Transmission charge: ")
        self.system_loss = input("Enter System Loss charge: ")
        self.distribution = input("Enter Distribution (Meralco) charge: ")
        self.subsides = input("Enter Subsides charge: ")
        self.government_taxes = input("Enter Government Taxes charge: ")
        self.universal_charges = input("Enter Universal charges: ")
        self.fit_all = input("Enter FiT-All charge: ")
        self.applied_credits = input("Enter Applied Credits charge: ")
        self.other_charges = input("Enter Other charges: ")
        self.installment_due = input("Enter Installment Due charge: ")
