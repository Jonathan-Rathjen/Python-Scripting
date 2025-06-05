## what we learned in last class

# -Python is a programming language
# -Python is an interpreted language
# -Easiest language to code
# -Python is not strict with spacing

# Variables: holds specific data type values (10, 10.9, "hello")

# Data Types:
# -Strings
# -Integers
# -Floats

# Numeric Data Types:
# -All sorts of mathematical equations(+,-,*,**,/,//,%)

# Strings:
# -Takes plain text 
# -Input function is by default string data type
# -int(),float()
# -String indexing --> Always starts from 0
# -len(),print(),type()
# -String Slicing (<start>:<end>:<jump>)
# -print(end='\n', sep=' ')



# Numeric Data Types

# Binary
# Binary are 0 and 1
# binary representation of a number in python is 0b:
# bin function translates from decimal to binary

# print(0b10101)
# print(bin(40))

# Hexidecimal
# hexidecimal = 16 0x (0-9) (a-f)
# hex function translates from decimal to hex

# print(0x123fd3)
# print(hex(534))

# Octal
# Octal 8 0-7
# 0o

# print(0o4361)
# print(oct(25))

# variable conventions (best practices)
# snake_casing, camelCasing

# last_name --> Snake Casing
# lastName --> Camel Casing

# snake_casing
# regular_variable = "Hello"
# _hidden_variable = "World"
# __super_hidden_variable = "teehee"


## Booleans
# What is a boolean?
# Boolean is a data type 
# Boolean only has two states: True or False

# Boolean Operators
# my_var = True
# my_var2 = False

# and, or, not

# and operator
# used to connect two booleans to form a single decision
# both must be True to pass True

# print(True and True) ## True and True --> True
# print(True and False) ## True and False --> False
# print(False and False) ## False and False --> False


# or operator
# used to connect two booleans to form a single decision
# only one has to be True to pass

# print(True or True) ## True or True --> True
# print(True or False) ## True or False --> True
# print(False or False) ## False or False --> False

# not operator
# used to return the opposite of the boolean 

# print(not True) ## --> False
# print(not False) ## --> True

# and always goes first

# if <condition1> and/or <condition2>

# Comparison Operators
# All return boolean values
# < less than
# > greater than
# <= less or equal
# >= greater or equal
# == equal

# if always takes boolean data types
# if condition always runs when the final decision is True
# if <condition1> and <condition2>:
    # indentation = tab
    # <code>
    # if <condition>:
        # indentation 
        # <code>
# elif <condition1> or <condition2>:
    # indentation = tab
    # <code>
# else:
    # indentation = tab
    # <code>

# Take 2 input of words 

# word1=input("Please input the first word: ")
# word2=input("Please input the second word: ")

# if len(word1) > len(word2):
#     print(word1,"is longer than",word2)
# elif len(word1) < len(word2):
#     print(word1,"is shorter than",word2)
# else:
#     print(word1,"and",word2,"are the same length")

# Check which word is longer

# score=int(input("Please input the student's score: "))

# if (score >= 90 and score <= 100):
#     print("The student earned an A")
# elif (score >= 80 and score <= 89):
#     print("The student earned a B")
# elif (score >= 70 and score <= 79):
#     print("The student earned a C")
# elif (score >= 60 and score <= 69):
#     print("The student earned a D")
# elif (score >= 0 and score <= 59):
#     print("The student earned an F")
# else:
#     print("That is not a valid score")

year=int(input("Please input any year: "))

if year%4 == 0 and not year%100 == 0 or year%400 == 0:
    print("Year",year,"is a leap year")
else:
    print("Year",year,"is not a leap year")




