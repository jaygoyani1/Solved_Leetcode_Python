class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i,j,index):
            if board[i][j] != word[index]:
                return False
            if index == len(word)-1:
                return True
            x = board[i][j]
            board[i][j] = "*"
            for r,c in [(-1,0),(1,0),(0,-1),(0,1)]:
                rx = r + i
                cx = c + j
                if 0<=rx< len(board) and 0<=cx<len(board[0]):
                    if backtrack(rx,cx,index+1):
                        return True
            board[i][j] = x
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
        return False
        