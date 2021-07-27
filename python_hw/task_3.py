"""
task 3
Data structures

"""

# 1. Create a list of 10 elements of four different data types like int, string, complex and float.
my_list = [1,2,3,4,5,6,"ashish",1.2, 10+10j,"123"]

#2. Create a list of size 5 and execute the slicing structure
print(my_list[3:9])
print(my_list[-5:])
print(my_list[::-1])

#3. Write a program to get the sum and multiply of all the items in a given list.
sum = 0
multiply = 1
for i in range(1,len(eval(input("enter list items: ")))+1):
    sum = sum + i
    multiply = multiply * i

print(f"The total sum of list items: {sum}.\nThe total mutiply of list items: {multiply}")

#4. Find the largest and smallest number from a given list.
input_list = eval(input("enter list: "))
smallest = input_list[0]
largest = input_list[0]

for i in range(len(input_list)):
    if smallest  < input_list[i]:
        pass
    else:
        smallest = input_list[i]

    if largest < input_list[i]:
        largest = input_list[i]

print(f'the smallest number in the list: {smallest}.\nthe largest number in the list: {largest}.')

#5. Create a new list which contains the specified numbers after removing the even numbers from a
# predefined list.
user_input = eval(input("enter list: "))
odd_list = list(filter(lambda x:x % 2 !=0,user_input))
print(odd_list)

#6. Create a list of elements such that it contains the squares of the first and last 5 elements between
#1 and30 (both included).
square = []
for i in range(1,31):
    s = lambda n:n*n
    if i < 6 or i > 26:
        square.append(s(i))
print(square)
#7. Write a program to replace the last element in a list with another list.
#Sample input: [1,3,5,7,9,10], [2,4,6,8]
#Expected output: [1,3,5,7,9,2,4,6,8]

user_input = eval(input("enter list: "))
print(user_input)
user_input.pop()
print(user_input)
user_input.extend(eval(input("enter another list: ")))
print(user_input)

#Create a new dictionary by concatenating the following two dictionaries:
#Sample input: a={1:10,2:20} b={3:30,4:40}
#Expected output: {1:10,2:20,3:30,4:40}

dict_1 = eval(input("enter first dict: "))
dict_2 = eval(input("enter second dict: "))
dict_3=dict(dict_1)
dict_3.update(dict_2)
print(dict_3)

#9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
#and n(both 1 and n included).
#Sample input: n=5
#Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}

dictionary = {}
for i in range(1,6):
    dictionary[i]=i*i

print(dictionary)

#10. Write a program which accepts a sequence of comma-separated numbers from console and
#generates a list and a tuple which contains every number in the form of string.
#Sample input: 34,67,55,33,12,98
#Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)

def list_tuple_generate(values):
    list_generate = list(values)
    tupple_generate = tuple(values)
    yield list_generate
    yield tupple_generate
user_input = input("enter comma separate number: ").split(",")
g = list_tuple_generate(user_input)
print(next(g))
print(next(g))