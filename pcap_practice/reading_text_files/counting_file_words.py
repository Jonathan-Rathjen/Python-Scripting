def count_occurences(file_name, word):
    stream = open(file_name)
    file = stream.read()
    word_list = file.replace(".","").replace(",","").replace(":","").replace("?","").lower().split()
    count = 0
    for i in word_list:
        if i == word.lower():
            count += 1
    stream.close()
    return count

print(count_occurences('first_text_file.txt',"bit"))
print(count_occurences('second_text_file.txt',"The"))