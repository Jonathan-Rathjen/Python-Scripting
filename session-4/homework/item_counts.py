dict1 = {"apple": 3, "banana": 5, "orange": 2}
dict2 = {"banana": 2, "orange": 4, "grape": 6}
newdict = dict(dict1)
newdict.update(dict2)

for i,j in dict1.items():
    for k,l in dict2.items():
        if i == k:
            newdict[i] = j + l
print(newdict)