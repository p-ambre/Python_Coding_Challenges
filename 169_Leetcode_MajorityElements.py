"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

"""

class Solution:
    def majorityElement(self, num: List[int]) -> int:
        num_dict = {}
        for i in range(len(num)):
            num_dict.setdefault(num[i], i)
        num_dict = dict.fromkeys(num_dict,0)

        for elem in num:
            if elem in num_dict:
                num_dict[elem] += 1
        return(max(num_dict, key=num_dict.get))
