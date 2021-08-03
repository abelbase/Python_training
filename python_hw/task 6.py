"""
task 6 
generators, list comprehension and decorators

"""

#1. Write a program in Python to find out the character in a string which is uppercase using list
#comprehension.
strings = 'AshiHihs'
upper_case = [x for x in strings  if x.isupper()]
print(upper_case)

# 2. Write a program to construct a dictionary from the two lists containing the names of students and
#their corresponding subjects. The dictionary should map the students with their respective subjects.
#Let’s see how to do this using for loops and dictionary comprehension.
def student_class(name, classes):
    my_dict = {key:values for key,values in zip(name,classes)}
    return my_dict

print(student_class(eval(input("enter name list: ")),eval(input("enter classes list: "))))

#4. Write a program in Python using generators to reverse the string.
#Input String = “Consultadd Training”

def reverse_string(str):
    str = str.split(" ")
    for i in str:
        yield i[::-1]

string = 'Consultadd Training'
g = reverse_string(string)
for i in g:
    print(i,end=" ")

#5. Write an example on decorators.
