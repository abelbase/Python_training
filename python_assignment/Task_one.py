"""
Task One 
Number and Varibales

"""
# Q1.Create three variables in a single line and assign values to them in such a manner that each one of
# them belongs to a different data type.
 a, b, c = 1, True, "Ashish"

# # 2. Create a variable of type complex and swap it with another variable of type integer.
a = 10 + 20j
b = 20
a , b = b , a 

# #3.Swap two numbers using a third variable and do the same task without using any third variable.
a, b = 1, 2
c = a+b
b,a = c-b,c-a
print(a,b)
# without tird variable
a, b = 5, 6
a = a + b
b = a - b
a = a - b
print(a,b)



# #4.Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.
python_2x = raw_input()
print(python_2x)

python_3x = input()
print(python_3x)

#5. Write a program to complete the task given below:
#Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
#another variable called z. Add 30 to z and store the output in variable result and print result as the
#final output.

users_input_1, users_input_2= input("enter two number between 1-10 separate by space: ").split()
z = int(users_input_1) + int(users_input_2)
result = z + 30
print(result)

#6. Write a program to check the data type of the entered values.
#HINT: Printed output should say - The data type of the input value is : int/float/string/etc
a, b, c = 10, 1.1, "hello"
print(f"The data type of the input value is: {a.__class__.__name__}/{b.__class__.__name__}/{c.__class__.__name__}/etc")


# 7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
# UPPERCASE.
# (Refer: https://capitalizemytitle.com/camel-case/)

CamelCase = "upper camel case variable"
Camelcase = "lower camel case variable"
snake_case = 'snake case varibale'

#8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
#again. Will it change the value? If Yes then Why?
"""it change the value because in first case , a is referencing to certain  object and then changing 
the value of a again , a is now referencing to another object. python print out the latest value of a."""