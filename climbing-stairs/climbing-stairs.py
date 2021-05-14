class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        x = [0] * n
        x[0] = 1 
        x[1] = 2
        for i in range(2,n):
            x[i] = x[i-1] + x[i-2]
            
        return x[-1]
        