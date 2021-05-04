class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        
        def find(start,end):
            count = 0
            while 0<=start and end <len(s):
                if s[start] != s[end]:
                    break
                start-=1
                end+=1
                count+=1
            return count
        
        for i in range(len(s)):
            ans += find(i,i)
            ans += find(i,i+1)
        return ans
            
                
        
        
            
        