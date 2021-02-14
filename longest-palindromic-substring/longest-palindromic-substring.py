class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans3 = ""
        
        def helper(left,right):
            d = ""
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                if right-left >= len(d):
                    d = s[left: right+1]
                    
                left -= 1
                right += 1
            return d

        for i in range(len(s)):
            ans1 =  helper(i,i)
            ans2 =  helper(i, i+1)
            if len(ans1) > len(ans2) and len(ans1) >= len(ans3):
                ans3 = ans1
            if len(ans2) > len(ans1) and len(ans2) >= len(ans3):
                ans3 = ans2
                
        return ans3