"""

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = [c for c in s if c.isalpha() or c.isdigit()]
        new = []
        for letter in letters:
            if letter.isupper():
                new.append(letter.lower())
            else:
                new.append(letter)
        val = "".join(new)
        i = 0
        j = len(val)-1
        while i < j:
            if val[i] != val[j]:
                return False
            i += 1
            j -= 1
        return True
