# List functions
# List comprehension
# Nested Loops
# Difference between mutable and immutable data types
# Tuples
# Dictionaries

# When to use del and whne to use methods?
# pop() remove()
# del
# methods can only be used with lists

# sort() 
# numbers are sorted from smallest to largest
# strings are sorted based on the ASCII table
# True = 1
# False = 0

# lst = [1,4,7,3,6,3,4,5,9,True]
# lst.sort()
# print(lst)

# index()
# gives index location of a given value

# lst = [2,5,1,-1,0,40.5]
# print(lst.index(0))

# split()
# split only works with strings 
# turns string into a list of elements divided by spaces

# strip()
# removes leading and trailing spaces from a string
# str1 = "   Hello. World. This. is a test.   "
# lst = str1.strip()
# lst = lst.split()

# for word in lst:
#     word = word.strip()
# print(lst)

# lst_numbers = []
# for num in range(0,11,2):
#     lst_numbers.append(num)
# print(lst_numbers)

# lst comprehension
# lst_num = [<vlaue_to_insert> for <iterator> in <sequence>]
# lst_num = [[i for i in range(1,6)] for j in range(5)]
# print(lst_num)

# Nested for loops

# for i in range(1,11):
#     print("Run",i)
#     for j in range(1,6):
#         print(" ",j,end = " ")
#         print('----------------',end = "")
#     print("\n")    

# Mutable data types are those whose contents can be changed
# Lists and Dictionaries are examples of mutable

# Immutable data types are those who cannont be changed
# examples are tuples and strings

# Tuples
# tuples are the same as lists but cannot be changed
# if list is inside tuple you can still change list
# tuples still supports functions but read only 

# tpl = (1,2,3,4)
# print(tpl[0:2])

# Dictionaries
# dictionaries are key and value pair stores

# keys must be unique
# dictionaries = {"key":"value","key2":"value2","key3":"value3"}
# print(dictionaries["key"])

dic = {1:{"name":"Elsu","last_name":"Loda","DoB":"March 13 2003"},
       2:{"name":"Jonathan","last_name":"Rathjen","DoB":"May 15 1999"},
       3:{"name":"Somon","last_name":"Smith","DoB":"November 24 1995"}}

for i,j in dic.items():
    print(f"Hello I'm {j['name']} {j['last_name']}. I was born in {j['DoB']}")
    print("I'm the student number",i)