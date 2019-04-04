"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "" and needle != "":
            return -1
        elif needle == "":
            return 0
        else:
            if haystack.startswith(needle):
                return 0
            else:
                l = len(needle)
                for i in range(1, (len(haystack) - l + 1)):
                    if haystack[i:i+l] == needle:
                        return(i)
                    else:
                        continue
                return -1
