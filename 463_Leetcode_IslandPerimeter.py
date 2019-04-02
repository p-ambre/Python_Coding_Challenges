"""
You are given a map in form of a two-dimensional integer grid where 1 represents
land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is
completely surrounded by water, and there is exactly one island (i.e., one or
more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water
around the island). One cell is a square with side length 1. The grid is rectangular,
width and height don't exceed 100. Determine the perimeter of the island.

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
"""
class Solution:
    def Count(self, grid: List[List[int]],i, j) -> int:
        count = 0
        row = len(grid[0])
        col = len(grid)
        if (i > 0 and grid[i-1][j]): #UP
            count += 1
        if (j > 0 and grid[i][j-1]): #LEFT
            count += 1
        if (i < row - 1 and grid[i+1][j]): #DOWN
            count += 1
        if (j < col - 1 and grid[i][j+1]): #RIGHT
            count += 1
        return(count)

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid[0])
        col = len(grid)
        perimeter = 0
        for i in range(0,row):
            for j in range(0,col):
                if(grid[i][j] == 1):
                    perimeter += (4 - self.Count(grid, i, j))
        return(perimeter)

row = int(input())
col = int(input())
grid = [ [1,1,0,0],
 [0,1,1,0],
 [1,1,1,0],
 [0,0,1,1] ]
result = islandPerimeter(grid, row, col)
print(result)
