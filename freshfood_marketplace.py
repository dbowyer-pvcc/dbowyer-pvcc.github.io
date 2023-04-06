#Name: Dustin Bowyer
#program purpose: To calculate gross and net pay for employees at a grocery store

import datetime
############ define global variables #############

c = ("cashier", 16.50)
s = ("stocker", 15.75)
j = ("janitor", 15.75)
m = ("maintenance", 19.50)


federal_income_tax = 0.12
state_income_tax = 0.03
social_security_tax = 0.062
medicare_tax = 0.0145

########### define program functions ############

def main():
   
    calculate_again = True

    while calculate_again:
        
        get_user_data() 

        
        perform_calculations() 

        
        display_to_user() 

        
        keep_going = input("\nWould you like to calculate for another employee? (Y/N): ")
        if keep_going.upper() != "Y":
            calculate_again = False
        

def get_user_data():
    global job_category, num_hours_worked
    job_category = str(input("Enter job category code (C, S, J, or M):  ")).upper()
    num_hours_worked = int(input("Enter number of hours worked:  "))

def perform_calculations():
    global hourly_rate, federal_income_deduction, state_income_deduction, social_security_deduction, medicare_deduction, total_deductions, net_pay, gross_pay
    if job_category == 'C': 
        hourly_rate = c[1]  
    if job_category == 'S':
        hourly_rate = s[1]
    if job_category == 'J':
        hourly_rate = j[1]
    if job_category == 'M':
        hourly_rate = m[1]

    gross_pay = num_hours_worked * hourly_rate
    federal_income_deduction = gross_pay * federal_income_tax
    state_income_deduction = gross_pay * state_income_tax
    social_security_deduction = gross_pay * social_security_tax
    medicare_deduction = gross_pay * medicare_tax

    total_deductions = federal_income_deduction + state_income_deduction + social_security_deduction + medicare_deduction
    net_pay = gross_pay - total_deductions

def display_to_user():
    
    
     

    print('\n\n')
    print('-----------------------------------------')
    print('--> Fresh Foods Market Payroll System <--')
    print('-----------------------------------------')
    print('Number of hours worked :         ' + format(num_hours_worked,'10,.2f'))
    print('Gross Pay :                    $ ' + format(gross_pay,'10,.2f'))
    print('Federal Tax Deducted           $ ' + format(federal_income_deduction,'10,.2f'))
    print('State Tax Deducted             $ ' + format(state_income_deduction,'10,.2f'))
    print('Social Security Tax Deducted   $ ' + format(social_security_deduction,'10,.2f'))
    print('Medicare Tax Deducted          $ ' + format(medicare_deduction,'10,.2f'))
    print('------------------------------------------------------')
    print('Net Pay                        $ ' + format(net_pay, '10,.2f'))
    print(str(datetime.datetime.now()))


######### call on main program to execute #######
main()

