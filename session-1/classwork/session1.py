# Numeric Data Types
# Both of the numeric data types can hold negative numbers

# Integer
# Whole Numbers
# Example: 1, 2, 10, 20, -10

# Float
# Decimal point NUmber:
# Example: 2.3, 4.5, 10.5, 4.0, -5.2

# integer_number = 10
# float_number = 5.6
# third_number = 86

# print(integer_number, float_number, third_number)

# addition
# subtraction
# multiplication
# division

# print(5 * 10.5)
# print(50 / 10.5)
# print(5 + 10.5)
# print(5 - 10.5)

# print(10 - 2 * 2) # PEMDAS
# print(10 ** 3) # power 10^2
# print(11 % 2) # remainder

# String
# String data is a text/word

# print("Hello World. 1")

# name = "Jonathan"
# name1 = 'Steve'
# sentence = "This is python session 1. This is sentence 2. This is sentence 3 ......"

# multiline_str = '''This is line 1
# This is line 2
# This is line 3'''

# print(type(name))

# String Indexing
# indexing always starts from 0 
# You can go from the back of the string with the index starting -1

# word = "Hello World"

# String Slicing
# start location : end location (non-inclusive) : characters to skip

# prints "World"
# print(word[6:11])

# every other letter
# print(word[::2])

# prints the word in reverse
# print(word[::-1])

# String Concatination
# Joining 2 or more strings together

# str1 = "aKumo"
# str2 = "Solutions"
# joined = str1 + str2

# # default values for end='\n' and sep=" "
# # print(str1,str2, end='\n', sep=' ')
# word = "This is line 1.\nThis is line 2.\nThis is line 3."
# print(word)

# # len(<string>) --> calculates length of the string
# print(len(word))

# input function always takes a string input
# int() converts data type to integer (if it's correct)
# float() same thing as int ^

# inp1 = float(input("Please provide a number 1: "))
# inp2 = float(input("Please provide a number 2: "))
# print(inp1 + inp2)

num1 = int(input("Please provide the first number: "))
num2 = int(input("Please provide the second number: "))

print(num1 * num2)
print(num1 / num2)
print(num1 % num2)

string = input("Please provide a word: ")
print("That word is",len(string),"letters long")

celcius = float(input("Please provide the tempurature in celcius: "))
farenheit = (celcius * (9/5) + 32)
print("That is",farenheit,"degrees in farenheit")
