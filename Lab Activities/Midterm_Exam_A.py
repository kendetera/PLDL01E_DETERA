import Midterm_Exam  # import the Midterm_Exam file


def main():
    # calling of our classes from the Midterm_Exam file
    service_information = Midterm_Exam.ServiceInformation()
    metering_information = Midterm_Exam.MeteringInformation()
    bill_and_payment_history = Midterm_Exam.BillAndPaymentHistory()
    billing_summary = Midterm_Exam.BillingSummary(metering_information.consumption, metering_information)

    # calling the methods in BillingSummary Class for computations
    billing_summary.get_basic_charge()
    billing_summary.get_environmental_charge()
    billing_summary.get_total_charges_before_taxes()
    billing_summary.get_government_taxes()
    billing_summary.get_total_amount_due()

    # calling our display functions
    display_service_info(service_information)
    display_metering_information(metering_information)
    display_bill_and_payment_history(bill_and_payment_history)
    display_billing_summary(billing_summary)


def display_service_info(service_information):  # function for displaying our service_info function
    print(f'''
                                                    Maynilad Water Services Inc.
                                                    8390 DR A SANTOS AVE BF HOMES
                                                    PARANAQUE CITY
                                                    VAT Reg TIN 005-393-442-0000
                                                    SPM NO:
                                                    MACHINE SN:
                        
                        SERVICE INFORMATION
            
    Contract Account No.:   {service_information.contract_account_number}
    Account Name:           {service_information.account_name}
    Service Address:        {service_information.service_address}
    TIN:                    {service_information.tin}
    Rate Class:             {service_information.rate_class}
    Business Area:          {service_information.business_area}
    
    ---------------------------------------------------------------------
    ''')


def display_metering_information(metering_information):  # function for displaying our metering_information function
    print(f'''
                        METERING INFORMATION
    
    Meter No.               MRU No.         Seq No.            
    {metering_information.meter_number}         {metering_information.mru_number}      {metering_information.seq_number}   
    Reading Date:           {metering_information.reading_date}
    Present Reading:        {metering_information.present_reading}
    Previous Reading:       {metering_information.previous_reading}
    Consumption (cu.m):     {metering_information.consumption}
    
    Previous 3 Months
       Consumption
       
    ---------------------------------------------------------------------
    ''')


def display_bill_and_payment_history(bill_and_payment_history):
    # function for displaying our bill_and_payment_history function
    print(f'''
                        BILL & PAYMENT HISTORY
    
    Desc                Total Amount            OR#         Date
    Description: {bill_and_payment_history.description}
    
    ---------------------------------------------------------------------
    ''')


def display_billing_summary(billing_summary):  # function for displaying our billing_summary function
    print(f'''
                        BILLING SUMMARY
                
    Billing Period: {billing_summary.billing_period} TO {billing_summary.billing_period_last_date}
    
    Current Charges:                                {billing_summary.total_amount_due:.2f}
    Basic Charge:                                   {billing_summary.basic_charge:.2f}
    Environmental Charges (20% of Basic Charge):    {billing_summary.environmental_charge:.2f}
    Maintenance Service Charge (MSC):               {billing_summary.maintenance_service_charge:.2f}
    Total Current Charges Before Taxes:             {billing_summary.total_charges_before_taxes:.2f}
    Government Taxes:                               {billing_summary.government_taxes:.2f}
    
    ---------------------------------------------------------------------
    
    TOTAL AMOUNT DUE                {billing_summary.total_amount_due:.2f}
    PAYMENT DUE DATE                {billing_summary.payment_due_date}
    ''')


# calling the main function
if __name__ == '__main__':
    main()
