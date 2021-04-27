class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        dp = [["."] * n for _ in range(n)]
        res = []
        diag = set()
        antidaig = set()
        col = set()
        
        def backtrack(i):
            if i == n:
                temp = ["".join(x) for x in dp]
                res.append(temp)
                return
            
            for j in range(n):
                if j in col or i+j in diag or i-j in antidaig:
                    continue
                dp[i][j] = "Q"
                col.add(j)
                diag.add(i+j)
                antidaig.add(i-j)
            
                backtrack(i+1)
                
                dp[i][j] = "."
                col.remove(j)
                diag.remove(i+j)
                antidaig.remove(i-j)
                    
        backtrack(0)
        return res
                
        