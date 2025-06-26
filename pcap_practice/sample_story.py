sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''
import re
def get_longest_word(inp):
    string_list = re.split(r'[,. \n]+', inp)
    largest = ''
    for i in string_list:
        if len(i) > len(largest):
            largest = i
    return largest