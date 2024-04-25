"""
This file contains various functions of a financial calculator.

Functions include 
1. Computing simple interest given the principal, interest rate and duration
2. Computing compound interest given the principal, interest rate and duration
3. Computing the future value given the present value, interest rate, duration and periodic deposit
4. Computing the present value given the future value, interest rate, duration and periodic deposit
5. Computing the periodic deposit given the future value, present value, interest rate and duration
6. Exiting the calculator

"""

import math

# function for the user to choose the operation 
def getInput():
    operation = input("""
    Type 1 for simple interest
    Type 2 for compound interest
    Type 3 for future value
    Type 4 for present value
    Type 5 for periodic deposit
    Type 6 to exit
    Type here: """)

    match operation:
        case "1":
            simple_interest()
        case "2":
            compound_interest()
        case "3":
            future_value()
        case"4":
            present_value()
        case"5":
            periodic_deposit()
        case "6":
            exit()

# Computes simple interest
# Interest = principal * (interest_rate/100) * duration
# Total balance = principal + Interest 
def simple_interest():
    principal = float(input("Enter the principal amount: "))
    interest_rate = float(input("Enter the interest rate: "))
    duration = float(input("Enter the duration in years: "))
    interest = round(float(principal * (interest_rate/100) * duration), 2)
    total_balance = round(float(principal + interest), 2)
    print("The interest is $",  interest)
    print("The total balance is $", total_balance)

# Computes compound interest
# Total balance = principal * (1 + interest_rate/100) ** duration
# Interest = Total balance - principal
def compound_interest():
    principal = float(input("Enter the principal amount: "))
    interest_rate = float(input("Enter the interest rate: "))
    duration = float(input("Enter the duration in years: "))
    total_balance = round(float(principal * (1 + interest_rate/100) ** duration), 2)
    interest = round(float(total_balance - principal), 2)
    print("The interest is $", interest)
    print("The total balance $", total_balance)

# Computes future value
# future_value = present_value * (1+ interest_rate/100) ** duration + (periodic_deposit * ((1+ interest_rate/100) ** duration -1)) / (interest_rate/100)
def future_value():
    present_value = float(input("Enter the present value : "))
    interest_rate = float(input("Enter the interest rate: "))
    duration = float(input("Enter the duration in years: "))
    periodic_deposit = float((input("Enter the periodic deposit: ")))
    future_value = round(float(present_value * (1 + interest_rate/100) ** duration + (periodic_deposit * ((1 + interest_rate/100) ** duration - 1))/(interest_rate/100)), 2)
    print("The future value is $", future_value)

# Computes present value
# present_value = (future_value - ((periodic_deposit * ((1 + interest_rate/100) ** duration - 1))/(interest_rate/100))) / (1 + interest_rate/100) ** duration
def present_value():
    future_value = float(input("Enter the future value: "))
    interest_rate = float(input("Enter the interest rate: "))
    duration = float(input("Enter the duration in years: "))
    periodic_deposit = float((input("Enter the periodic deposit: ")))
    present_value = round(float((future_value - ((periodic_deposit * ((1 + interest_rate/100) ** duration - 1))/(interest_rate/100))) / (1 + interest_rate/100) ** duration), 2)
    print("The present value is $", present_value)

# Computes periodic deposit
# periodic_deposit = (future_value - (present_value * (1 + interest_rate/100) ** duration)) * (interest_rate/100) / ((1 + interest_rate/100) ** duration -1)
def periodic_deposit():
    present_value = float(input("Enter the present value: "))
    future_value = float(input("Enter the future value: "))
    interest_rate = float(input("Enter the interest rate: "))
    duration = float(input("Enter the duration in years: "))
    periodic_deposit = round(float((future_value - (present_value * (1 + interest_rate/100) ** duration)) * (interest_rate/100) / ((1 + interest_rate/100) ** duration -1)), 2)
    print("The periodic deposit is $", periodic_deposit)


while True:
    getInput()