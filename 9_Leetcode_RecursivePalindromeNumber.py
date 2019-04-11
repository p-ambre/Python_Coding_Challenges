"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

def isPalindrome(x, start, end, n):
    #if the string is empty
    if n == 0:
        return True
    #if there is only one character
    if start == end:
        return True
    #if the first and last character of the string don't match
    if x[start] != x[end]:
        return False
    #if the first and last character are same then we check the characters in between
    if (start < end):
        return(isPalindrome(x, start+1, end-1, n))
    return True

x = int(input())
x = str(x)
n = len(x)
print(isPalindrome(x, 0, n-1, n))
