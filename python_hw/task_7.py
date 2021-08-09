"""
task 7

classes and objects

"""

#1. Write a program that calculates and prints the value according to the given formula:
###Q= Square root of [(2*C*D)/H]
#Following are the fixed values of C and H:
#C is 50.
##H is 30.
#D is a variable whose values should be input to your program in a comma-separated sequence.##
import math
class square:
    c = 50 # class variable for every object created from  this class. 
    h = 30
    def __init__(self,d):
        self.d = [i for i in d.split(",") ] # spliting the d value into list 

    def square_root(self):
        value = []
        for i in self.d:
            value.append([round(math.sqrt((2*self.c* int(i))/self.h))])
        print(value)
        for i in value:
            for j in i :
                print(j,end="\t")
        print()

S = square(input("enter number with comma-separated squences: "))
S.square_root()

#2. Define a class named Shape and its subclass Square. The Square class has an init function which
##takes length as argument. Both classes have an area function which can print the area of the shape
#where Shape’s area is 0 by default.

class Shape:
    def __init__(self,length):
        self.length = self.Square(length)

    def area_shape(self):
        return 0
    
    class Square:
        def __init__(self,length):
            self.length = length

        def area(self):
            return 0

a = Shape(10)
print(a.area_shape())
print(Shape.Square(10).area())




#3. Create a class to find three elements that sum to zero from a set of n real numbers.

class find_zero:
    def __init__(self,num):
        self.num = num
        print(self.num)

    def zero(self):
        values =[]
        positive = [x for x in self.num if x > 0]
        negative = [x for x in self.num if x < 0]
        positive.sort()
        negative.sort()
        for index,value in enumerate(positive):
            for j in positive[index+1:]:
                total = value + j
                #print(total)
                for k in negative:
                    if total + k == 0:
                        values.append([value,j,k])
        for index,value in enumerate(negative):
            for j in negative[index+1:]:
                total = value + j
                #print(total)
                for k in positive:
                    if total + k == 0:
                        values.append([value,j,k])
        print(values)

E = find_zero([-25,-10,-7,-3,2,4,8,10])
E.zero()


#4 4. Create a Time class and initialize it with hours and minutes.
#Create a method addTime which should take two Time objects and add them.
#E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
#Create another method displayTime which should print the time.
#Also create a method displayMinute which should display the total minutes in the Time.
#E.g.- (1 hr 2 min) should display 62 minute.

#from types import new_class


class Time:
    def __init__(self,hours, minutes):
        self.hours = hours
        self.minutes = minutes


    def __str__(self): # display the Time input
        return (f'{self.hours} hours and {self.minutes} minutes')


    def __add__(self,other): # add hour and minutes
        self.hour = self.hours + other.hours
        self.minute = self.minutes + other.minutes

        while self.minute >= 60:
            self.minute -= 60
            self.hour +=1

        # convert hour into minutes
        self.sum_hr = self.hours + other.hours
        self.sum_min = self.minutes + other.minutes

        self.sum_min = (self.sum_hr * 60) + self.sum_min
    
        #print(f'the time is {self.hour} hr and {self.minute} min.')


    def display_time(self): # display total hour and minutes
        print(f'the total time is {self.hour} hours and {self.minute} minutes.')

    def display_minutes(self): # display total minutes 
        print(f'the total time  of ({self.hour} hr  and {self.minute} min) in minutes is  : {self.sum_min} minutes.')



a = Time(eval(input("enter hour: ")),eval(input("enter minutes: ")))
print(a)
b = Time(eval(input("enter hour: ")),eval(input("enter minutes: ")))
print(b)
c = a + b
a.display_time()
a.display_minutes()


# 5.Write a Person class with an instance variable “age” and a constructor that takes an integer as a
#parameter. The constructor must assign the integer value to the age variable after confirming the
#argument passed is not negative; if a negative argument is passed then the constructor should set
#age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
#methods:
#yearPasses() should increase age by the integer value that you are passing inside the function.
#amIOld() should perform the following conditional actions:I
#if age is between 0 and <13, print “You are young”.
#If age is >=13 and <=19 , print “You are a teenager”.
#Otherwise, print “You are old”.

class Person:
    def __init__(self,age=0):
        if age < 0:
            print(f'Age is not valid,setting age to 0.')
            self.age = age
        self.age = age

    def year_passes(self,increasement):
        self.age = self.age + increasement
        return self.age
    
    def am_i_old(self):
        if 0 <= self.age < 13:
            print('You are young.')

        elif 13 <= self.age <=19:
            print('You are a teenager.')
        
        else:
            print('You are old.')

    
age = Person(eval(input("enter your age: ")))
age.year_passes(eval(input("enter your year passes increament: ")))
age.am_i_old()


