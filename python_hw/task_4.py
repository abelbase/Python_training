"""
task 4
Traditional functions , Anonymous functions & Higher order functions
"""
#1. Write a program to reverse a string.
def reverse_order(strings):
    return strings[::-1]
print(reverse_order(input("enter strings: ")))

# 2.Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.
def upper_lower(strings):
    count_upper = 0
    count_lower = 0
    for i in range(len(strings)):
        if strings[i].isupper():
            count_upper +=1
        elif strings[i].islower():
            count_lower +=1
    print(f"No.of uppercase char : {count_upper}.\nNo.of Lower case char: {count_lower}.")

upper_lower(input("enter string: "))

#3. Create a function that takes a list and returns a new list with unique elements of the first list.
def unique_list(args):
    return list(set(args))

print(unique_list(eval(input("enter list item: "))))

# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.
def sort_alpha(args):
    print(args)
    args = sorted(args)
    return ("-").join(args)

print(sort_alpha(input("enter hypen separated words: ").split("-")))

#5. Write a program that accepts a sequence of lines as input and prints the lines after making all
#characters in the sentence capitalized.
def make_uppercase(args):
    return args.upper()
print(make_uppercase(input("enter strings: ")))

#6. Define a function that can receive two integral numbers in string form and compute their sum and
#print it in the console.
a , b = input("enter two number number: ").split(" ")
a , b = int(a) , int(b)
sum = lambda a,b : a + b
print(sum(a,b))

#7. Define a function that can accept two strings as input and print the string with the maximum length
#in the console. If two strings have the same length, then the function should print both the strings line
#by line.
def str_length(str1,str2):
    if len(str1) == len(str2):
        print(str1,end="\t")
        print(str2)
    elif len(str1) < len(str2):
        print(str2)
    else:
        print(str1, end="\t")
        print(str2)

str_length(input("enter strings: "),input("enter another string: "))

#8..Define a function which can generate and print a tuple where the values are square of numbers
#between 1 and 20 (both 1 and 20 included).
def square():
    my_list= list()
    for i in range(1,21):
        square = i * i
        my_list.append(square)

    print(tuple(my_list))
square()

# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.
def showNumbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            print(f'{i} EVEN')
        elif i % 2 != 0:
            print(f'{i} ODD')

showNumbers(int(input("enter number: ")))

# 10 Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)
def even():
    my_list = list(range(1,21))
    print(list(filter(lambda x: x % 2 ==0,my_list)))

even()

#11. Write a program which uses map() and filter() to make a list whose elements are squares of even
#numbers in [1,2,3,4,5,6,7,8,9,10].
#Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
#numbers in the filtered list. Use lambda() to define anonymous functions.

def square_even():
    my_list = list(range(1,11))
    filter_even = list(filter(lambda x: x % 2 ==0,my_list))
    print(list(map(lambda x: x*x , filter_even)))

square_even()

# 12. Write a function to compute 5/0 and use try/except to catch the exceptions
def try_except(num1,num2):
    try:
        print(num1/num2)
    except:
        print("don't divide number with 0")
try_except(int(input("enter number: ")),int(input("enter number again: ")))

# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
import functools
delim  =""
reduce_num = functools.reduce(lambda x, y: str(x) + delim + str(y),list(range(1,8)))
print(reduce_num)

# 14. 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.
print(list(filter(lambda x: x % 3 !=0 and x % 7 ==0, eval(input("enter list: ")))))

# 15 Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.
def multiply(my_list):
    return my_list*my_list

print(list(map(multiply,eval(input("enter a list: ")))))

#16. What is the output of the following codes:
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
# ans: 2

def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')

a()
# ans: finally run but after that throw a NameError.