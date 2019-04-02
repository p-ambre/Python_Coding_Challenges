"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows
like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

ALGORITHM-
1) Create an array of n strings, arr[n]
2) Initialize direction as "down" and row as 0. The
   direction indicates whether we need to move up or
   down in rows.
3) Traverse the input string, do following for every
   character.
   a) Append current character to string of current row.
   b) If row number is n-1, then change direction to 'up'
   c) If row number is 0, then change direction to 'down'
   d) If direction is 'down', do row++.  Else do row--.
4) One by one print all strings of arr[].
"""

class Solution:
    def convert(self, word: str, numRows: int) -> str:
        if numRows == 1:
            return(word)
        len_word = len(word)
        arr = ["" for x in range(len_word)]
        row = 0
        for i in range(len_word):
            arr[row] += word[i]
            if row == 0:
                down = True
            elif row == numRows - 1:
                down = False
            if down:
                row += 1
            else:
                row -= 1

        return(''.join([arr[i] for i in range(len_word)]))

"""
Time complexity: O(len of the string)
"""
