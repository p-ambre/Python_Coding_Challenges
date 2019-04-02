"""
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty word in str.

Example: Input: pattern = "abba", str = "dog cat cat dog"
         Output: true
"""
def wordPattern(pattern, string):

    new_string = string.split(' ')
    pattern_list = []
    string_list = []
    dict_string = {}
    dict_pattern = {}

    if len(pattern) != len(new_string):
        return(False)
    for i in range(len(pattern)):
        dict_pattern.setdefault(pattern[i], i)
        pattern_list.append(dict_pattern[pattern[i]])
        dict_string.setdefault(new_string[i], i)
        string_list.append(dict_string[new_string[i]])

    if pattern_list == string_list:
        return(True)
    else:
        return(False)

print("Enter a pattern:")
pattern = str(input())
print("Enter a string:")
string = str(input())
print(wordPattern(pattern, string))
