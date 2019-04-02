"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Input: "()"
Output: true
Input: "()[]{}"
Output: true
Input: "(]"
Output: false
Input: "([)]"
Output: false
Input: "{[]}"
Output: true

"""

def isValid(string):
    bracket_dict = {")":"(", "]":"[", "}":"{"}
    stack = []
    for character in string:
        if character == "(" or character == "[" or character == "{":
            stack.append(character)
        elif character == ")" or character == "]" or character == "}":
            if not stack:
                return(False)
            popped_char = stack.pop()
            if bracket_dict[character] != popped_char:
                return(False)
    return not stack

string = str(input())
print(isValid(string))
