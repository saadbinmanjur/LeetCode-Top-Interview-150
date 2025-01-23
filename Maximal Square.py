class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        maxLen = 0
        # each cell means the number of squares it can form starting from that position.
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        for i in range(rows+1):
            dp[i][cols] = 0
        for j in range(cols+1):  
            dp[rows][j] = 0
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
                    if dp[i][j] > maxLen:
                        maxLen = dp[i][j]    
        return (maxLen*maxLen)              