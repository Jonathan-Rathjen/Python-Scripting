words = input("Enter words: ")
word_list = words.split()
largest = ""
for i in word_list:
    if len(i) > len(largest):
        largest = i
print("Longest Word: ",largest)