class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        dic  = {}
        i = 0
        for j in range(n):
            if s[j] in dic:
                i = max(i,dic[s[j]])
            ans = max(ans , j-i+1)
            dic[s[j]] = j+1
        return ans
    
                
                
                
                
            
        