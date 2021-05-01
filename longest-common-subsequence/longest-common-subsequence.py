class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        x = len(text1)
        y = len(text2)
        
        dp = [[0]*(y+1) for _ in range(x+1)]
        
        for i in reversed(range(x)):
            for j in reversed(range(y)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]