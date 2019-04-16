"""
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""

class Solution:

    def combinations(self, combination, rest_digits):
        result = []
        if rest_digits == "":
            return(combination)
        else:
            list_1 = self.phone.get(rest_digits[0])
            for i in range(len(combination)):
                for j in range(len(list_1)):
                    result.append(combination[i] + list_1[j])
            return(self.combinations(result, rest_digits[1:]))

    def letterCombinations(self, digits):
        if digits == "" or digits == "0" or digits == "1":
            return []
        else:
            self.phone = {
                     '2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']
                    }
            return(self.combinations(self.phone.get(digits[0]), digits[1:]))

p1 = Solution()
digits = str(input())
print(p1.letterCombinations(digits))
