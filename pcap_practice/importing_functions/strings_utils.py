from string_utils import halve_string

def halve_strings(string_list):
    halve_list = []
    for i in string_list:
        halve_list.append(halve_string(i))
    return halve_list