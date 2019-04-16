"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

class Solution:
    def commonPrefix(self, result, rest_elem):
        if rest_elem == []:
            return result
        else:
            res = ""
            curr_elem = rest_elem[0]
            if len(result) > len(curr_elem):
                min_len = len(curr_elem)
            else:
                min_len = len(result)
            for i in range(min_len):
                if result[i] == curr_elem[i]:
                    res += result[i]
                else:
                    break
            return(self.commonPrefix(res, rest_elem[1:]))

    def longestCommonPrefix(self, strs):
        n = len(strs)
        if strs == []:
            return ""
        else:
            return(self.commonPrefix(strs[0], strs[1:]))

strs = list(input().split())
p1 = Solution()
print(p1.longestCommonPrefix(strs))
