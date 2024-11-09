import MidtermQ1  # import the MidtermQ1 module


def main():
    # calling of our classes and their methods
    customer_info = MidtermQ1.CustomerInfo()

    electric_bill = MidtermQ1.ElectricBill()
    electric_bill.get_previous_billing_info()
    electric_bill.get_total_amount_due()

    service_info = MidtermQ1.ServiceInfo(customer_info)

    billing_info = MidtermQ1.BillingInfo(electric_bill)

    bill_computation_summary = MidtermQ1.BillComputationSummary()

    # call the display functions
    display_customer_info(customer_info)
    display_electric_bill(electric_bill)
    display_service_info(service_info)
    display_billing_info(billing_info)
    display_bill_computation_summary(bill_computation_summary)


def display_customer_info(customer_info):  # display the customer infos
    print(f'''
    {customer_info.customer_name}
    {customer_info.customer_street_address}
    {customer_info.customer_barangay_address}
    {customer_info.customer_municipality}
    {customer_info.customer_city}

    ************************** 
    ''')


def display_electric_bill(electric_bill):  # display the electric bill info status box
    print(f'''
    Balance From Previous Billing 
    {electric_bill.remaining_balance} \t||\t {electric_bill.get_previous_billing_info()}

    Current Charges
    {electric_bill.amount_due} \t||\t {electric_bill.total_amount_due}

    **************************
    ''')


def display_service_info(service_info):  # display the service info status box
    print(f'''
    Service ID Number: {service_info.service_id_number}
    Rate: {service_info.rate}
    Contact in the name of {service_info.contact_in_the_name_of}
    Service Address: {service_info.service_street_address} {service_info.service_barangay_address} 
                     {service_info.service_municipality} {service_info.service_city}

    **************************
    ''')


def display_billing_info(billing_info):  # display the billing info status box
    print(f''''
    Bill Date: {billing_info.bill_date}
    Meter Reading Date: {billing_info.meter_reading_date}
    Bill Period: {billing_info.bill_period}
    Due Date: {billing_info.due_date}
    Total KWH: {billing_info.total_kwh}    
    Total Current Amount: {billing_info.total_current_amount}
    Next Meter Reading: {billing_info.next_meter_reading}
    
    **************************
    ''')


def display_bill_computation_summary(bill_computation_summary):  # display the bill computation summary box
    print(f'''
    Generation: {bill_computation_summary.generation}
    Transmission: {bill_computation_summary.transmission}
    System Loss: {bill_computation_summary.system_loss}
    Distribution (Meralco): {bill_computation_summary.distribution}
    Subsides: {bill_computation_summary.subsides}
    Government Taxes: {bill_computation_summary.government_taxes}
    Universal Charges: {bill_computation_summary.universal_charges}
    FiT-All (Renewable): {bill_computation_summary.fit_all}
    Applied Credits: {bill_computation_summary.applied_credits}
    Other Charges: {bill_computation_summary.other_charges}
    Installment Due: {bill_computation_summary.installment_due}

    ''')


# calling the main function
if __name__ == '__main__':
    main()
