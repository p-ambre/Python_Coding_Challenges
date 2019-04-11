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

#------------------------*** METHOD 1 (REVERSING THE NUMBER LOGIC) ***----------------------------------

def isPalindrome(x):
    if x < 0:
        return False
    rev_x = 0
    temp = x
    while temp>0:
        rev_x = rev_x*10 +temp%10
        temp = temp//10
    return rev_x == x

x = int(input())
print(isPalindrome(x))

#------------------------*** METHOD 2 (WITHOUT REVERSING THE NUMBER) ***----------------------------------

def isPalindrome(x):
    if x < 0:
        return False
    x = str(x)
    i = 0
    j = len(x) - 1
    while i < j:
        if x[i] != x[j]:
            return False
        i += 1
        j -= 1
    return True

x = int(input())
print(isPalindrome(x))
