class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0]*len(matrix[0]) for _ in matrix]
        maxi = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                    maxi = max(maxi,dp[i][j])
        return maxi*maxi
                    
                    
        
                
        
                    
        
                
        