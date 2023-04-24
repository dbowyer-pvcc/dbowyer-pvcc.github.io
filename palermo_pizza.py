#Name: Dustin Bowyer
#program purpose: To calculate gross and net pay for employees at a grocery store

import datetime
############ define global variables #############

s = ("small", 9.99)
m = ("medium", 12.99)
l = ("large", 14.99)
x = ("extra large", 17.99)


sales_tax = 0.055


########### define program functions ############

def main():
   
    calculate_again = True

    while calculate_again:
        
        get_user_data() 

        
        perform_calculations() 

        
        display_to_user() 

        
        keep_going = input("\nWould you like to place another order? (Y/N): ")
        if keep_going.upper() != "Y":
            calculate_again = False
        

def get_user_data():
    global pizza_size, num_pizzas
    pizza_size = str(input("Enter pizza size code (s, m, l, or x):  ")).lower()
    num_pizzas = int(input("Enter number of pizzas you want to order:  "))

def perform_calculations():
    global single_pizza_cost, cost_of_pizzas, sales_tax, total, sales_tax_amt
    if pizza_size == 's': 
        single_pizza_cost = s[1]  
    if pizza_size == 'm':
        single_pizza_cost = m[1]
    if pizza_size == 'l':
        single_pizza_cost = l[1]
    if pizza_size == 'x':
        single_pizza_cost = x[1]

    cost_of_pizzas = num_pizzas * single_pizza_cost
    sales_tax_amt = cost_of_pizzas * sales_tax
    total = cost_of_pizzas + sales_tax_amt


def display_to_user():
    
    
     

    print('\n\n')
    print('-----------------------------------------')
    print('--> Palermo Pizza <--')
    print('-----------------------------------------')
    print('Number of pizzas ordered :        ' + format(num_pizzas,'10,.2f'))
    print('Pizza cost :                    $ ' + format(cost_of_pizzas,'10,.2f'))
    print('Sales tax                       $ ' + format(sales_tax,'10,.2f'))  
    print('Total                           $ ' + format(total,'10,.2f'))
    print('------------------------------------------------------')

    print(str(datetime.datetime.now()))


######### call on main program to execute #######
main()


