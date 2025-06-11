word_string = input("Enter words: ")
word_list = word_string.split()
no_dup = []
for i in word_list:
    if i in no_dup:
        continue
    else:
        no_dup.append(i)
print("Filtered List:",no_dup)
