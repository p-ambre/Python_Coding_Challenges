"""

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".

"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        letters = [c for c in s if c in vowels]
        rev_vowels = []
        for c in s:
            if c in vowels:
                rev_vowels.append(letters.pop())
            else:
                rev_vowels.append(c)
        return("".join(rev_vowels))
