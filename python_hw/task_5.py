"""
Task 5
File Handling and Exception handling

"""
#1. Write a program in Python to allow the error of syntax to be handled using exception handling.
#HINT: Use SyntaxError

def error_handling():
    try:
        eval('a===b')
    except SyntaxError:
        print("syntax error raised.")

error_handling()

#2. Write a program in Python to allow the user to open a file by using the argv module. If the
#entered name is incorrect throw an exception and ask them to enter the name again. Make sure
#to use read only mode.
import sys
def file_open(users):
    try:
        if sys.argv[0] == users:
            with open(users,'r') as f:
                f.read()
     

        raise FileExistsError ("enter your file name again. ")
    except FileExistsError:
        raise

file_open(input('user_input:  '))

# 3. Write a program to handle an error if the user entered a number more than four digits it should
#return “The length is too short/long !!! Please provide only four digits”

def four_digits(num):
    try:
        if num >= 10000:
            raise ValueError(f"{num} number is too long.")
        elif num < 999:
            raise ValueError(f"{num} number is too small.")
        print(num)
    except:
        print("Please provide only four digits number.")
        raise
        

four_digits(eval(input('enter number: ')))

#4. Create a login page backend to ask users to enter the username and password. Make sure to
#ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
#should not be more than 3 times.
def login_page():
    try:
        username = input("enter username: ")
        password = input("enter password: ")
        re_password = input("please re-enter your password: ")
        i = 1
        while i <= 2:
            if password == re_password:
                print('welcome: ',username)
                break
            elif password != re_password :
                print("your password is wrong. ")
                re_password = input("please re-enter your password: ")
            i +=1
            if i == 3:
                raise TypeError("session out.")
            
    except TypeError:
        raise

login_page()

#6. Read doc.txt file using Python File handling concept and return only the even length string from
#the file. Consider the content of doc.txt as given below:
#Hello I am a file
#Where you need to return the data string
#Which is of even length
#Make sure you return the content in The same link as it is present.

def file_handling():
    with open('doc.txt','w') as f :
        f.write("Hello I am a file\nWhere you need to return the data string\nwhich is of even length")
        f.write('\nMake sure you return the same link as it is present')
    with open("doc.txt") as f:
        a = ""
        for i in f:
            wordlist = i.split()
            #print(wordlist)
            for j in wordlist:
                if len(j) % 2 == 0:
                    a = a + " " + j
        with open('abc.txt','w') as wf:
            for line in f:
                wf.write(line)
        
        print(a)
file_handling()