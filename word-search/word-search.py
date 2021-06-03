class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lenm = len(board)
        lenn = len(board[0])
        
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        def bfs(i,j,index):
            if index == len(word)-1:
                return True
            
            temp = board[i][j]
            board[i][j] = "#"
            
            for d in direction:
                newi = d[0] + i
                newj = d[1] + j
                if newi<0 or newi>=lenm or newj<0 or newj>=lenn or board[newi][newj] != word[index+1]:
                    continue
                if bfs(newi,newj,index+1):
                    return True
            board[i][j] = temp
            return False
            
        
        
        for i in range(lenm):
            for j in range(lenn):
                if board[i][j] == word[0]:
                    if bfs(i,j,0):
                        return True
        return False
                    
                    
        