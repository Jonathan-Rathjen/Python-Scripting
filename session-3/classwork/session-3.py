# for loop until 5
#   print

# iterator = variable used within loop the value of which changes based on the sequence
# sequence data type = data type that has start point and end point

# string indexing. through indexing we can get the start of the string and end of the string

# for <iterator> in <sequence_data type>:
#     <code that needs to be repeated>

# inp = input("Please give me and input: ")
# for i in inp:
#     print(i)

# inp = input("Input a word: ")
# inp2 = input("Input a character: ")
# count = 0
# for i in inp:
#     if i == inp2:
#         count += 1

# if count > 1 or count == 0:
#     print(f"There are {count} {inp2}'s in {inp}")
# else:
#     print(f"There is {count} {inp2} in {inp}")

# for i in range(1,11):
#     print(i,"squared is",(i**2))

# import math
# for i in range(2,101):
#     for j in range(2,int(math.sqrt(i))+1):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# inp = int(input("Input: "))
# num = 0

# while num < inp:
#     num += 1
#     print(num)

# for i in range(1,10):
#     if i == 5:
#         break
#     else:
#         print(i)

# inp1 = int(input("Until what number to print: "))
# inp2 = int(input("Where we need to break: "))

# if inp2 > inp1:
#     print("Input two is out of range")
# else:
#     for i in range(1,inp1+1):
#         if i == inp2:
#             break
#         else:
#             print(i)

# Lists | Tuple | Dectionaries | Sets --> Data types that can hold more than one value

# all other data types can only hold a single value
# int = 10
# float = 40.5
# boolean = True | False
# string = "Hello"

# List is a data type that can hold 0 or more values
# List starts with []

# lst = ["Hello","World",10,10.5,True,['Hello',"Test"]]
# print(lst[1][2])

lst_fruits = ["pineapple","pear","kiwi","apricot","peach","pear", "cherry", "melon"]

# append()
# append function adds element at the end of the list
# append can only take one argument at a time

# lst_fruits.append('apple')
# lst_fruits.append('grape')

# insert()
# insert allows you to insert an element into any location within the list
# can only take one argument

# lst_fruits.insert(0,"apple")

# pop()
# pop removes the last element in a list
# you can also specify a location to remove a certin index location

# lst_fruits.pop()
# lst_fruits.pop(2)

# remove()
# remove finds any element matching the input and removes them from the list
# wil remove any instance of the input argument

# lst_fruits.remove("pear")

# indexing lists is the same as strings
# print(lst_fruits[0::2])

# lst_fruits[0] , lst_fruits[-1] = lst_fruits[-1], lst_fruits[0]
# print(lst_fruits)

inp = input("Please give me a character: ")
count = 0
for i in lst_fruits:
    if inp in i:
        print(i)
    else:
        count += 1

if count == len(lst_fruits):
    print("No fruits in our list contain that character")

