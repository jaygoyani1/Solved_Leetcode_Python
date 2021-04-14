class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0]*len(matrix[0]) for i in range(len(matrix))]
        ans = 0
         
        for i in range(len(matrix)):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] == 1:
                ans = 1
        
        for j in range(1,len(matrix[0])):
            dp[0][j] = int(matrix[0][j])
            if dp[0][j] == 1:
                ans = 1
        
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])
                ans = max(ans, dp[i][j])
        return ans*ans
                    