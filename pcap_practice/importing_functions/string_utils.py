import math 
def halve_string(input_string):     
    first = input_string[0:math.ceil(len(input_string)/2)]    
    second = input_string[math.ceil(len(input_string)/2):]     
    return (first,second) 
print(halve_string("supercalifragilisticexpialidocious"))