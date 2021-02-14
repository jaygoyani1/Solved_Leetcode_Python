class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        def helper(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        for i in range(len(s)):
            x = helper(i,i)
            y = helper(i,i+1)
            
            long = x if len(x) > len(y) else y
            res = long if len(long)>len(res) else res
        return res
                
                