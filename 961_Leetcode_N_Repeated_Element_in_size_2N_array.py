"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these
elements is repeated N times. Return the element repeated N times.
Input: [1,2,3,3]
Output: 3
Input: [2,1,2,5,3,2]
Output: 2
Input: [5,1,5,2,5,3,5,4]
Output: 5
"""

def repeatedNTimes(array):
    i = 0
    j = i+1
    n = len(array)
    for i in range(n):
        for j in range(j, n):
            if array[i] == array[j]:
                return(array[i])

array = [int(x) for x in input().split()]
if len(array) % 2 == 0:
    result = repeatedNTimes(array)
    print(result)
else:
    print("Please enter a even number.")
