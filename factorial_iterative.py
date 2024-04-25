"""
This file contains a function to compute the factorial of a given number
"""
import math

#Computes the factorial of a given number
def factorial(number) :
    index = 1
    factorial_value = 1
    while index <= number:
        factorial_value = factorial_value * index
        index += 1
    return factorial_value

my_num = input("Enter a number to find its factorial: ")

print("The factorial is ", factorial(int(my_num)))