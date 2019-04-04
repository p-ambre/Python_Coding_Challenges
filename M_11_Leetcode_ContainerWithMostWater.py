"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms
a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

ALGORITHM:
Note 1 : When you consider a1 and aN, then the area is (N-1) * min(a1, aN).
Note 2 : The base (N-1) is the maximum possible.

1)This implies that if there was a better solution possible, it will definitely have the Height greater than min(a1, aN).
 Base * Height > (N-1) * min(a_1, a_N)
2) We know that, Base min(a1, aN)
This means that we can discard min(a1, aN) from our set and look to solve this problem again from the start.
3) If a1 < aN, then the problem reduces to solving the same thing for a2, aN.
4) Else, it reduces to solving the same thing for a1, aN-1
"""

def maxarea(array):
    n = len(array)
    l = 0
    r = n - 1
    area = []
    while l < r:
        area.append(min(array[l], array[r]) * (r - l))
        if array[l] < array[r]:
            l += 1
        else:
            r -= 1
        print(area)
    return(max(area))



array = [int(x) for x in input().split()]
result = maxarea(array)
print(result)
