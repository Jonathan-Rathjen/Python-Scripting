# return
# return is essential part of using functions
# functions that don't have return are pretty much useless(not always)

# def greet(name):
#   return "Hello, "+name+"!"
# print(greet("Alice"))

# if you do not return a value in a function it will return None

# def greet(name):
#     print("Hello, "+name+"!")
# print(greet("Alice"))

# parameters are the variables that we use within a function
# arguments are the values that we input when we call a function
# you can have multiple parameters and arguments used in a function
# arguments can be assigned in the order the are given or by assigning them to the parameters

# def greet(name, age):
#     return{
#         "name": name,
#         "age": age
#     }

# print(greet('Abdul',25))
# print(greet(age=26, name='Kris'))

# def give_age():
#     age = input("How old are you? ")
#     return age
# def give_name():
#     name = input("What is your name? ")
#     return name
# age = give_age()
# name = give_name()
# def dic(age,name):
#     return {'age':age,'name':name}
# print(dic(age,name))

# recursive functions call themselves

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))  

# def fibonacci(stop,first=0,second=1):
#     print(first)
#     if second >= stop:
#         return first
#     first,second = second,(first + second)
#     return first + fibonacci(stop,first,second)
# fibonacci(10000)

# try except blocks
# used when you beilieve a block of code could give you an error
# except will only run when an error is raised between try and except
# you can also specify what is done based on what error is raised

# try:
#     number = int(input("Enter a number: "))
#     print(10 / number)
# except ZeroDivisionError:
#     print("You can't divide by zero.")
# except ValueError:
#     print("Please enter a valid integer.")

# students = {'Jonathan': 98, 'Somon': 95, 'Elsu': 90, 'Shah':80, 'Yunus':60}

# def check_student(students):
#     try:
#         inp = input("Which student are you looking for? ")
#         return (inp+" has a score of "+ str(students[inp]))
#     except KeyError:
#         return ("That student is not in this class.")

# print(check_student(students))

# you can import functions from other files in the same directory
# from <file name> import <function name>