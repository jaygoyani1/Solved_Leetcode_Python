class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        i = 0
        j = 0
        ans =0
        
        while j < len(s):
            curr = s[j]
            if curr in dic and i<=dic[curr]:
                i = dic[curr] + 1
            else:
                ans = max(ans, j-i+1)
            dic[curr] = j
            j+=1
        return ans
            
        