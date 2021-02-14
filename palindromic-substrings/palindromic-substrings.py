class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        
        def helper(left,right):
            d = 0
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
                d += 1
            return d

        for i in range(len(s)):
            ans += helper(i,i)
            ans += helper(i, i+1)
        
        return ans
            
                
        
        
            
        