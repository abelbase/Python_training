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
user_input = eval(input("enter number: "))

if user_input % 3 == 0 and user_input % 5 == 0:
    print("Consultadd - python Training")

if user_input % 3 == 0:
    print("Consultadd")

if user_input % 5 == 0:
    print("python Training")

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

#3. Write a program in Python to implement the given flowchart:

a, b, c = 10, 20, 30

avg = (a + b + c)/ 3
print(f"avg = {avg}")

if avg > a and avg > b and avg > c :
    print("avg is higher than a, b, c.")
else:
    if avg > a and avg > b:
        print("avg is higher than a, b")
    else:
        if avg > a and avg > c:
            print("avg is higher than a, c.")
        else:
            if avg > b and avg > c :
                print("avg is higher than b, c")
            else:
                if avg > a :
                    print("avg is just higher than a.")
                else:
                    if avg > b:
                        print("avg is just higher than b.")
                    else:
                        if avg > c:
                            print("avg is just higher than c.")

# 4. Write a program in Python to break and continue if the following cases occurs
#If user enters a negative number just break the loop and print “It’s Over”
#If user enters a positive number just continue in the loop and print “Good Going”
while True :
    user_input = eval(input("enter a number: "))
    if user_input < 0:
        print("it's Over.")
        break
    if user_input > 0 :
        print("Good Going.")
        continue

#5.. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200.

for i in range (2000,3201):
    if i % 7 == 0 and  (i % 5 !=0):
        print(i)

#6. What is the output of the following code examples?
x=123 
for i in x: 
    print(i)
# ans: typeerror int object not iterable

i = 0
while i < 5: 
    print(i) 
    i += 1 
    if i == 3: 
        break
    else: 
        print('error')
# ans: 0, error , 1, error, 2
count = 0
while True: 
    print(count) 
    count += 1 
    if count >= 5: 
        break
# ans : 0,1,2,3,4

# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6. 
# Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i)

#8. Write a program that accepts a string as an input from the user and calculate the number of digits
# and letters. 
# Sample input: consul72 
# Expected output: Letters 6 Digits 2

user_input = input("enter string: ")
count_str = 0
count_num = 0
for i in user_input:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        count_str = count_str + 1
    elif i in '0123456789':
        count_num = count_num + 1

print(f"letters: {count_str}\tDigits: {count_num}")

# 9. Read the two parts of the question below: 
#Write a program such that it asks users to “guess the lucky number”. If the correct number is
# guessed the program stops, otherwise it continues forever.
#Modify the program so that it asks users whether they want to guess again each time. Use two
#variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
#to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
#The program continues as long as a user has not answered “no” and has not guessed the correct
#number)
import random
while True:
    answer = random.randint(1,100)
    print(f"the lucky number is: {answer}")
    user_input = eval(input("Guess the lucky number from 1 to 100: "))
    if user_input == answer:
        print("you guessed it correctly.")
        break
    option = input("press enter for continue or 'NO' for quit: ")
    if option.lower() == 'no':
        break

# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
#such as
#While counter <= 5:
#print(“Type in the”, counter, “number”
#counter=counter+1
#The program asks for five guesses (no matter whether the correct number was guessed or not). If the
#correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
#After the fifth guess it stops and prints “Game over!”

import random
counter = 1
while counter <=5:
    answer = random.randint(1,100)
    print(f"the lucky number is: {answer}")
    user_input = eval(input("Guess the lucky number from 1 to 100: "))
    if user_input == answer:
        print("Good guess.")
    else:
        print("Try again!")
    if counter == 5:
        print("Game over.")
    counter +=1

# 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
#the while loop so that users do not have to continue guessing after they found the number. If the user
#does not guess the number at all, print “Sorry but that was not very successful”

import random
counter = 1
while counter <=5:
    answer = random.randint(1,100)
    print(f"the lucky number is: {answer}")
    user_input = eval(input("Guess the lucky number from 1 to 100: "))
    if user_input == answer:
        print("Good guess.")
        break
    else:
        print("Sorry but that was not very successful.")
    if counter == 5:
        print("Game over.")
    counter +=1





