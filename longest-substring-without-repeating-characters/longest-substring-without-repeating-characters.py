class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        start = 0
        maxi = 0
        for i,char in enumerate(s):
            if char in dic:
                start = max(start, dic[char])
            
            maxi = max(maxi, i-start + 1)
            dic[char] = i + 1
        return maxi
                
                
            
                
        