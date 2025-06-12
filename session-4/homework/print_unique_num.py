word = input("Input: ")
dic = dict.fromkeys(list(word),0)

for i in list(word):
    dic[i] += 1
for i,j in dic.items():
    if j == 1:
        print(i,end = " ")
print("\n")