# Mike's comprehensive review of python programming up until this point

# Variable declaration and different data types
numbers = 1
characters = 'c'
boolean = True
string = "String"
lists = [1, "string", 'c']
smallExampleofDictionary = {'Navin': 'Samsung'}

# text manipulation
example = "My string"
example.lower()
example.upper()
example.find('c')
example.replace(example, "Apples")

# list manipulation
lists.append(45)
lists.insert(0,12)
lists.remove('c')
lists.pop(0)
del lists[2:]
print(numbers)

# Tuples and sets
tuples = {1,2,3,5,6} # does not support indexing

# to import a module
import math

# to use that same module
m = 25
math.sqrt(m)

# to only take in a character from the user
# myChar = input("Take it in")[0]

# Different ways to use if syntax
if (True):
    print("This is how an if statement works")
elif(False):
    print("elif is the keyword youd use for middle section")
else:
    print("This is how you end the whole if statement tree thing")

# while loop syntax
j = 5
while(j <= 10):
    j = j + 1

# for loop syntax
for i in range(10):  # i will take on the value of every different part of the list/array/whatever
    print(i)

# Dictionaries (essentially hash maps)
student = {'name': 'John'}
print(student)  # print entire map
print(student['name'])  # accesses a value associated with a name
student.get('name')  # does the same thing but will print "none" if it doesn't find it
student.get('name', 'Not Found')  # will print Not Found if map isnt found


# Tuples are immutable lists
tup = (1, 2, 3, 4, 5)

# Sets cannot maintain any order
sets = {1, 2, 3, 4, 5}
z = 0
while(z < 3):
    print(sets)
    z = z + 1

# Extra thing on dictionaries
listofkeys = ['Navin', 'Kiran', 'Harsh']
listofvalues = ['Pyth', 'Java', 'JS']
combinedlist = dict(zip(listofkeys, listofvalues))

# IF tree keywords


# Arrays
from array import *
vals = array('i', [5, 6, 7, 8, 9]) # different typecodes: b, 0, i, I, f, d
print(vals.buffer_info())
print(vals.reverse())
print(vals[0])
print(len(vals))

# functions
def greet():
    print("Hello!")

def add(a, b):
    print(a+b)

def functionWithSeveralInputs(a, *b):
    c = a
    for i in b:
        c = c + i

# Global keywords
v = 99
def globalStuff():
    v = 100  # This is a locally created variable
    print(v)

print(v)
bepis = globals()['v']  # will take on global variable v

# Just remember to set a max recurison limit
# import sys
# sys.setrecursionlimit(10)


# Beginning of more advanced topics

#Filtering, mapping, and reducing functions
f = lambda var1,var2: var1 + var2  # allows you to quickly throw together a function, use this: result = f()
randomList = [range(10)]
# evens = list( lambda n: n%2 == 0, randomList) # filter example
# evens = list(map(lambda n: n*2, evens)) # map example

# Importing modules
from math import *
print(math.sqrt(25))

# Notes on OOP in Python
class mikesClass:
    apples = 0 # field declaration
    def __init__(self, bruh):  #  constructor method that can be manually created
        self.bruh = bruh
    def regularMethod(self):
        print("Do your thing")

# Beginning of Polymorphism

# Beginning of Duck Typing, as long as an object has a certain method it doesn't matter what else it's class has
# it can still be used for
class Orchard:
    def add(self):
        print("Its in the orchard")

class Apple:
    def putitIn(self, Orchard):
        Orchard.add()


mikesOrchard = Orchard()
anApple = Apple()
anApple.putitIn(mikesOrchard)

# Beginning of COmplex topics: Method overloading and overriding, Abstraction and Interfaces
from abc import ABC, abstractmethod
class Artist():
    def createArt(self):
        print("Making art")

    @abstractmethod
    def getMoney(self):  #example of abstraction in Python
        pass
    def computerStuffIguess(self, x, *b): # example of method overloading in Python
        c = x
        for i in b:
            c = c + i


    def genericClass(self):
        print("Generic class method")

class WebDesigner(Artist):
    def getMoney(self):
        print("Ok, Im gonna get money rn")

    def genericClass(self):
        print("Generic class method but for the sub class")

pepis = WebDesigner()
print(pepis.genericClass()) # this will print the genericClass from the subclass WebDesigner not Artist

# Iterators
nums = [1,2,3,4]
it = iter(nums)

#alternatively
class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        self.num =+ 1

# Generators, basically iterators but with pre-determined functions
def topten():
  n = 1
  while n<= 10:
      sq = n*n
      yield sq
      n += 1

values = topten()
for i in values:
    print(i)

# Practical purpose: fetching 1ks records from database and you
# wanna process them, allows you to work with one at a time

# Exception/error Handling
# Snytatical errors: compile time error
# Run time errors: Wrong input from user
# Normal statements don't give error, critical statements do
a = 5
b = 0
try:
    print("Resource open")
    print(a/b)
except Exception as e:  # Only executed when there is an error
    print("Whoops", e)
except ZeroDivisionError as e:
    print("Specifically", e)
except ValueError as e:
    print("Invalid Input")
finally:  # Always executes
    print("Resouce closed")

# Multithreading

from threading import *
from time import sleep # time manipulation module
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello!")
            sleep(1) #forces method to halt for one second

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)
t1 = Hello()
t2 = Hi()

# inside the threading class we have a method called run
t1.start()  # A thread is crated here
sleep(.2)  # Prevents a collision, preventing threads from running in cpu at the same time and create a gap
t2.start()  # A seperate thread is created here

t1.join()  # This part will wait for the
t2.join()
print("End of threading example")  # Because this goes in the main thread it is executed before thread 1 and 2
