class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        row_len=len(board[0])
        col_len=len(board)
        ans = [[-1 for x in range(row_len)] for y in range(col_len)]

        def inBound(i,j):
            return (0<=i<col_len) and (0<=j<row_len)

        for i in range(col_len):
            for j in range(row_len):
                count=0
                for ii,jj in [(i,j+1),(i,j-1),(i-1,j),(i+1,j),(i-1,j+1),(i+1,j-1),(i+1,j+1),(i-1,j-1)]:
                    if inBound(ii,jj):
                        count+=board[ii][jj]
                if count<2:
                    ans[i][j]=0
                elif board[i][j]==1 and (count==2 or count==3):
                    ans[i][j]=1
                elif board[i][j]==1 and count>3:
                    ans[i][j]=0
                elif board[i][j]==0 and count==3:
                    ans[i][j]=1
                else:
                    ans[i][j]=board[i][j]
        board[:]=ans
        return board