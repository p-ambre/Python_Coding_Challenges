"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Input: "Hello World"
Output: 5

"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(string)-1
        count = 0
        if len(string) <= 1 or ' ' not in string:
            return 0
        else:
            while j > 0 and string[j] != " ":
                count += 1
                j -= 1
            return(count)
