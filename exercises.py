'''

01a Exercises
These exercises should help you get the flavor of how to perform arithmetic and string operations in Python. 
You will also get to play with (pseudo-)random generators and the range operator.
These skills will all be used in assignment 2.

To answer these exercises, open the IDLE program that came with your Python installation. IDLE is a line-by-line Python interpreter.
You can copy lines from this file into IDLE to interpret them and produce a result. Then copy the result back to the following line in this file (after the #).
You will also need to answer several questions to show you understand what is happening. 


'''
# Math in Python is what you would expect. Add comments with the answers the IDLE returns. I'll do the first one for you.
10 + 15 
#25
8 - 1 
#7
10 * 2 
#20
35 / 5
#6

35 / 4
#8.75
35 // 4 
#8
# What is the difference between the / operator and the // operator?
# / returns the exact amount but // returns the amount rounded down to the nearest whole number

2 ** 5 
#32
# What does the ** operator do?
#it acts like the ^ operator
5 % 3 
#2
5 % 2
#1
5 % 4
#1
# What does the % operator do?
#it returns the remainder after dividing the first number by the second

(1 + 3) * 2
#8
# What effect do the parenthesis have on this statement?
#it makes python add before multiplying

# Data in python is of different flavors or "types," each with its own characteristics
type(3)
#int
type(3.0)
#float
type("word")
#str
type(True)
#bool
type(False)
#bool
type(None)
#Nonetype
# None is a special object in python. We will talk more about it later


# It is possible to convert from one type to another. 
int(3.0)
#3
float(7)
#7.0
str(55)
#'55'
bool(1)
#True
# How can you tell the difference between these four different types?
#int don't have decimals, floats always have decimals, strings are surounded by '' or "", booleans are either True or False.

# Strings are created with single or double-quotes
"This is a string."
'This is also a string.'

"Hello " + "world!"
# What does the + operator do here?
#adds the strings together

"This is a string"[0]
#'T'
"This is a string"[5]
#'i'
"This is a string"[8]
#'t'
# What is happening as you change the number?
#you take the string that is located at that index

"This is a string"[-1]
#g
# What happens when you use a negative number?
#you go to the end of the string and left instead of starting from the beginning

"%s can be %s" % ("strings", "interpolated")
# What is happening here? 
#the %s are being replaced by the strings after the %

# A more robust (and modern) way to put things into strings is using the format method
"{0} can be {1}".format("strings", "formatted")
#"strings can be formatted"

# You can use names instead of numbers to make it easier to keep things straight
"{name} wants to eat {food}".format(name="Bob", food="lasagna")
#"Bob wants to eat lasagna

# You have already met the print method
print("I'm Python. Nice to meet you!")
# Here is its sibling, the input method
n = input("What is your name? ")
print("Hello, " + n)
#"Hello, matt"
# What just happened?
# python requests input by asking what is your name and then that input is saved to n and it gets printed out

# For your next assignment, you will need to use random numbers 
# first we need to get a few methods from the library called random
from random import random,randint,shuffle,sample
random()
# Run this line a few times. What is happening here?
# it gives a random number less than 1

randint(1,100)
# How is this different?
#it gives a random int ranging from 1 to 100

# The next few use a list of numbers from 0 to 9
items = [0, 1,2,3,4,5,6,7,8,9]
shuffle(items)
print(items)
# What just happened?
# shuffle put the numbers in the list in a random order and then prints it

print(sample(items, 1))
# What does this do?
# prints a random number from the list

print(sample(items, 5))
# What does the second parameter control?
# the amount of items that are printed

for i in range(0,5):
	print(i)
# 0 1 2 3 4
# What is happening here? What happens if you change the two range parameters?
#it prints from the first number to one less the second number
