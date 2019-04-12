"""
Given a string S, return the "reversed" string where all characters that are not a letter
stay in the same place, and all letters reverse their positions.

Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        rev_s = []
        for c in s:
            if c.isalpha():
                rev_s.append(letters.pop())
            else:
                rev_s.append(c)
        return("".join(rev_s))
