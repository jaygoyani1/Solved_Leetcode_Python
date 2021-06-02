class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(s,left,right):
            while left>=0 and right <len(s):
                if not s[left] == s[right]:
                    break
                left-=1
                right+=1
            return right-left-1
        
        maximum = ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = helper(s,i,i)
            len2 = helper(s,i,i+1)
            
            max_len = max(len1,len2)
            
            if max_len > end-start:
                start = i-(max_len-1)//2
                end = i + max_len//2
        return s[start:end + 1]            
            
                
                