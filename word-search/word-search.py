class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lenx, leny = len(board), len(board[0])
        def dfs(r,c,wordi):
            if wordi == len(word):
                return True
            if r<0 or r>=lenx or c<0 or c>=leny or board[r][c] != word[wordi]:
                return False
            temp = board[r][c]
            board[r][c] = "*"
            x = dfs(r+1,c,wordi+1) or dfs(r-1,c,wordi+1) or dfs(r,c+1,wordi+1) or dfs(r,c-1,wordi+1)
            board[r][c] = temp
            return x
        
        for i in range(lenx):
            for j in range(leny):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False
        