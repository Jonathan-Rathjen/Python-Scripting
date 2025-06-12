word = input("Input: ")
dic = dict.fromkeys(list(word),0)

for i in list(word):
    dic[i] += 1
print(dic)