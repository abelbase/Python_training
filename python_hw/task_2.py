"""
Task Two
Operators and decision making statement

"""
#1. Write a program in Python to perform the following operation:
"""
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “Python Training” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
string."""
# user_input = eval(input("enter number: "))

# if user_input % 3 == 0 and user_input % 5 == 0:
#     print("Consultadd - python Training")

# if user_input % 3 == 0:
#     print("Consultadd")

# if user_input % 5 == 0:
#     print("python Training")

#2. Write a program in Python to perform the following operator based task:
"""Ask user to choose the following option first:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication
If User Enter 5 - Average
Ask user to enter two numbers and keep those numbers in variables num1 and num2
respectively for the first 4 options mentioned above.
Ask the user to enter two more numbers as first and second for calculating the average as
soon as the user chooses an option 5.
At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
NOTE: At a time a user can only perform one action."""

print("choose your option:\n1 - Addition\n2 - Subtraction\n3 - Dividion\n4 - Multiplication\n5 - Average ")

i = 1
while i > 0: 
    user_input = eval(input("select the option from 1 to 5: "))
    if user_input == 1:
        num1, num2 = input("enter two number: ").split()
        num1 , num2 = int(num1), int(num2)
        add = num1 + num2
        print(add)
        if add < 0:
            print("NEGATIVE")
    elif user_input == 2:
        num1, num2 = input("enter two number: ").split()
        num1 , num2 = int(num1), int(num2)
        sub = num1 - num2
        print(sub)
        if sub < 0:
            print("NEGATIVE")
    elif user_input == 3:
        num1, num2 = input("enter two number: ").split()
        num1 , num2 = int(num1), int(num2)
        div = num1 /num2
        print(div)
        if div < 0:
            print("NEGATIVE")
    elif user_input == 4:
        num1, num2 = input("enter two number: ").split()
        num1 , num2 = int(num1), int(num2)
        multiply = num1 * num2
        print(multiply)
        if multiply < 0:
            print("NEGATIVE")
    elif user_input == 5:
        first , second = input("enter two number :").split()
        average = int(first)+int(second)  /2
        print(average)
        if average < 0:
            print("NEGATIVE")
        
    else: 
        print("please select the valid option.")

    quit = input("press enter for continue or Q for quit: ")
    if quit.lower() == 'q':
        i = -1






