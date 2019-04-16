"""

Given a non-empty string check if it can be constructed by taking a substring of
it and appending multiple copies ofthe substring together. You may assume the given
string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"  n = 4 pattern = "ab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba" n = 3 pattern = ""
Output: False

Example 3:
Input: "abcabcabcabc" n = 12 pattern = "abc" or "abcabc"
Output: True

Example 4:
Input: "abcabcabc" n = 9 pattern = "abc"
Output: True

Example 5:
Input: "abcd" n = 4 pattern = ""
Output: False

Example 6:
Input: "babbabbabbabbab" n = 13 pattern = "bab"
Output: True

Explanation:
n can be even or odd
i starts from 1 because in pattern we need to have at least one element

"""

class Solution:
    def repeatedSubstringPattern(self, s):
        n = len(s)
        else:
            for i in range(1, (n//2)+1):
                res = ""
                if (n % i) == 0:
                    count = n//i
                    pattern = s[0:i]
                    for j in range(count):
                        res += pattern
                    if res == s:
                        return True
                    else:
                        continue
                else:
                    continue
            return False

s = str(input())
p1 = Solution()
print(p1.repeatedSubstringPattern(s))
