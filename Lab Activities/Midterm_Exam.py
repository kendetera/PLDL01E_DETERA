class ServiceInformation:  # Our Class for gathering Service Information such as account name and account number
    def __init__(self):  # Prompts the user to input their information
        self.contract_account_number = input("Enter Contract Account Number: ")
        self.account_name = input("Enter Account Name: ")
        self.service_address = input("Enter Service Address: ")
        self.tin = input("Enter TIN: ")
        self.rate_class = input("Enter Rate Class: ")
        self.business_area = input("Enter Business Area: ")


class MeteringInformation:  # Our 2nd class for gathering Metering Information
    def __init__(self):  # Prompts the user to input their metering information
        self.meter_number = input("Enter Meter No.: ")
        self.mru_number = input("Enter MRU No.: ")
        self.seq_number = input("Enter Seq No.: ")
        self.reading_date = input("Enter Reading Date: ")
        self.present_reading = input("Enter Present Reading: ")
        self.previous_reading = input("Enter Previous Reading: ")
        self.consumption = float(input("Enter Consumption (cu.m): "))


class BillAndPaymentHistory:  # Our 3rd class for displaying bill and payment history
    def __init__(self):
        self.description = "WB-Water Bill, GD-Guarantee Deposit, MISC-Reopening Fee, Connection Fee, Metering Charge"


class BillingSummary:  # Our 4th class that calculates the charges that are to be paid
    def __init__(self, consumption, reading_date):
        self.metering_consumption = consumption  # To take 'consumption' value from the MeteringInformation Class
        self.metering_reading_date = reading_date  # To take 'reading_date' value from the MeteringInformation Class
        self.billing_period_last_date = self.metering_reading_date.reading_date
        self.cubic_meter_rate = 23.52  # Fixed cubic meter rate
        self.basic_charge = 0
        self.environmental_charge = 0
        self.total_charges_before_taxes = 0
        self.government_taxes = 0
        self.total_amount_due = 0
        self.billing_period = input("Enter Billing Period: ")
        self.maintenance_service_charge = float(input("Enter Maintenance Service Charge (MSC): "))
        self.payment_due_date = input("Enter Payment Due Date: ")

    def get_basic_charge(self):  # method for calculating the basic charge
        self.basic_charge = (self.cubic_meter_rate * self.metering_consumption)
        return self.basic_charge

    def get_environmental_charge(self):  # method for calculating the environmental charge
        self.environmental_charge = (self.basic_charge * 0.20)
        return self.environmental_charge

    def get_total_charges_before_taxes(self):  # method for calculating the total charges before taxes
        self.total_charges_before_taxes = (self.basic_charge + self.environmental_charge
                                           + self.maintenance_service_charge)
        return self.total_charges_before_taxes

    def get_government_taxes(self):  # method for calculating government taxes
        self.government_taxes = (self.total_charges_before_taxes * 0.025)
        return self.government_taxes

    def get_total_amount_due(self):  # method to get the total amount due to be paid by the customer
        self.total_amount_due = (self.total_charges_before_taxes + self.government_taxes)
        return self.total_amount_due
