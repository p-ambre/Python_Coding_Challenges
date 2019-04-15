"""

Given a non-empty string check if it can be constructed by taking a substring of
it and appending multiple copies ofthe substring together. You may assume the given
string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, (n//2)+1):
            if (n % i) == 0:
                count = n//i
                pattern = s[0:i]
                if count*pattern == s:
                    return True
                else:
                    continue
            else:
                continue
        return False

s = str(input())
p1 = Solution()
print(p1.repeatedSubstringPattern(s))
