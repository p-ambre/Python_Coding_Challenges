"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

"""
class Solution:
    def validPalindrome(self, string: str) -> bool:
        i = 0
        j = len(string)-1
        while i < j:
            if string[i] != string[j]:
                return self.isPalindrome(string, i+1, j) or self.isPalindrome(string, i, j-1)
            i += 1
            j -= 1
        return True

    def isPalindrome(self, string, l, r):
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True
