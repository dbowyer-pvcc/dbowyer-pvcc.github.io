#Name: Dustin Bowyer
#Prog Purpose: compute tuition, fees, and balance for pvcc student based on inputs listed in handout
#   PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees
#   NOTE: All fees are PER CREDIT
#       In-state tuition: $155, Out-of-state tuition: $331.60
#       Capital fee: $23.50 (out-of-state students only)
#       Institution fee: $1.75
#       Activity fee: $2.90


import datetime

############ define global variables #############
# define tuition & fee rates
RATE_TUITION_IN = 155
RATE_TUITION_OUT = 331.60
RATE_CAPITAL = 23.5
RATE_INSTITUTION = 1.75
RATE_ACTIVITY = 2.90



#define global variables
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0
tuitionfee = 0
capitalfee = 0
institutionfee = 0
activityfee = 0
totalowed = 0
balance = 0





########### define program functions ############

def main():
    another_student = True
    while another_student:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno.upper() != "Y":
            another_student = False



def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("\nNumber of credits registered for: "))
    scholarshipamt = float(input("\nScholorship amout received; If none enter Number zero: "))


def perform_calculations():
    global tuitionfee, capitalfee, institutionfee, activityfee, totalowed, balance 
    if inout == 1:
        tuitionfee = numcredits * RATE_TUITION_IN
        capitalfee = 0
    else:
        tuitionfee = numcredits * RATE_TUITION_OUT
        capitalfee = numcredits * RATE_CAPITAL


    institutionfee = numcredits * RATE_INSTITUTION
    activityfee = numcredits * RATE_ACTIVITY
    totalalowed = tuitionfee + capitalfee + institutionfee + activityfee
    balance = totalowed - scholarshipamt


def display_results():
    print('\n\n--------------------------------')
    print('Number of credits : ' + str(numcredits))
    print('Tuitions          $ ' + format(tuitionfee,'10,.2f'))
    print('Capital fee       $ ' + str(capitalfee))
    print('Institution Fee   $ ' + str(institutionfee))
    print('Activity Fee      $ ' + str(activityfee))
    print('Total             $ ' + str(totalowed))
    print('Scholarship       $ ' + str(scholarshipamt))
    print('--------------------------------')
    print('Balance Owed      $ ' + str(balance))
    print(str(datetime.datetime.now()))
    print("NOTE: PVCC Fee Rates: https:www.pvcc.edu/tuition-and-fees")



######### call on main program to execute ########

main()

