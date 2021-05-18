class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dp = [[0]*len(board[0]) for _ in range(len(board))]
        
        dir = [(-1,-1),(-1,0),(0,-1),(1,0),(0,1),(1,1),(1,-1),(-1,1)]                    
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                x = 0
            
                for a,b in dir:
                    newx,newy = i+a,j+b
                    if newx <0 or newx>=len(board) or newy < 0 or newy >= len(board[0]):
                        continue
                    if board[newx][newy] == 1:
                        x+=1
                if board[i][j] == 1:
                    if x<2 or x>3:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1
                else:
                    if x ==3:
                        dp[i][j] = 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = dp[i][j]
        