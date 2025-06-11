bad_list = input("Enter numbers separated by space: ")
num_list = bad_list.split()

rev_list = []
for i in range(len(num_list)):
    rev_list.insert(-i,num_list[i])
print("Reversed List:",rev_list)