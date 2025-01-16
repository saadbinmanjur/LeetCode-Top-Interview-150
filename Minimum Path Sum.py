class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(0, n):
            for x in range(0, m): 
                if i > 0 and x > 0: 
                    grid[i][x] += min(grid[i-1][x], grid[i][x-1])
                elif i > 0:
                    grid[i][x] += grid[i-1][x]
                elif x > 0: 
                    grid[i][x] += grid[i][x-1]

        return grid[n-1][m-1]