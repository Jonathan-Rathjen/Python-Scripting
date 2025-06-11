num_string = input("Enter numbers: ")
num_list = num_string.split()
try:
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
except:
    print("One of your values is not an integer, try again")
    pass
largest = 0
second = 0
for i in num_list:
    if i > largest:
        largest,second = i,largest
print("Second largest number:",second)
