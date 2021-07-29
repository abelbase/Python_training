#1. Create a list of given structure and get the Access list as provided below:
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][:4])
print(x[-3:])
print(x[::2])
print(x[::-1])
print([x[5][5][0]])
print(list())

#2. Create a list of thousand numbers using range and xrange and see the difference between each other.
print(list(range(1001)))
print(list(xrange(1001)))

#3. How Tuple is beneficial as compared to the list?
# ans: tuple is immutable as compared to list.
 
# 4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
#the number which is divisible by 3 and is a multiple of 2.

print(list(filter(lambda x: x % 3 ==0 and x % 2 == 0, list(range(1,101)))))

#5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
#string with their index.
def vowels(str):
    str = str[::-1]
    print(f"reverse string: {str}")
    for i,vowels in enumerate(str):
        if vowels.lower() in 'aeiou':
            print(f"reverse string index is: {i} and vowel in the string is: {vowels}")
            

vowels(input("enter your string: "))

# 6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
#string which is having an even length. 
def even_length_string(str):
    str = str.split(" ")
    for i in str:
        if len(i) % 2 == 0:
            print(f"string: {i}\tlenght of string is: {len(i)}")

strings = "hello my name is abcede"
even_length_string(strings)

#7. Write a program in python to print the pair of numbers whose sum is equal to the result
#number that is let's say 8.
x=[1,2,3,4,5,6,7,8,9,-1]
def pair_sum(my_list):
    for results in my_list:
        a = results
        for i in my_list:
            for j in my_list:
                if a == i + j:
                    print(f"results: {a}\t sum of pair equal to results: {i,j}")

pair_sum(x)

#8. Write a program in Python to complete the following task:
#Create two lists such as even_list and odd_list
#Ask user to enter a number in the range of 1,50 and make sure if the entered number is
#even, append it to the even_list and if the entered number is odd append it to the odd_list.
#Keep that in mind you can only add 5 items in each list
#Make sure once you enter all the 5 elements, calculate the sum of the list and return the
#maximum of the list.

def ask_user(ask):
    even_list = []
    odd_list =[]
    for i in ask:
        if i % 2 == 0:
            if len(even_list) <= 5:
                even_list.append(i)
            else:
                continue
        elif i % 2 != 0:
            if len(odd_list) <=5 :
                odd_list.append(i)
            else:
                continue

    even_sum = sum(even_list)
    odd_sum = sum(odd_list)
    if even_sum > odd_sum:
        return f"maximum of the list is even_list and the total sum of even_list is : {even_sum}"
    else:
        return f"maximum of the list is odd_list and the total sum of odd_list is : {odd_sum}"


max_sum_list = ask_user(eval(input("enter list of number in range of 1 to 50: ")))
print(max_sum_list)

#9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
def char_occurence(str):
    frequency = {}
    for char in str:
        if char in "abcdefghijklmnopqrstuvwxyz":
            frequency[char] = str.count(char)
    
    for key, values in frequency.items():
        print(f"{key}={values}")

char_occurence(str(input("enter strings: ")))

# 10. 10. Generate and print another tuple whose values are even numbers in the given tuple
# (1,2,3,4,5,6,7,8,9,10).

def even_tuple(num):
    return tuple(filter(lambda x: x % 2 == 0,num))

print(even_tuple(range(1,11)))