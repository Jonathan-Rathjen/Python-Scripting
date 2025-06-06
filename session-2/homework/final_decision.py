try:
    bool1 = eval(input('Please input the first boolean ("True" or "False"): '))
    bool2 = eval(input('Please input the second boolean ("True" or "False"): '))
except:
    print("That is not a valid input, Try again")
    quit()
    pass


print(bool1,"and",bool2,"=",bool1 and bool2)
print(bool1,"or",bool2,"=",bool1 or bool2)
if bool1 == (not bool2):
    print("not",bool1,"=",not bool1)
    print("not",bool2,"=",not bool2)
else:
    print("not",bool1,"=",not bool1)
