class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        x = collections.Counter(s)
        
        count = 0
        for i in x:
            if x[i]%2 != 0:
                count+=1
            if count == 2:
                return False
        return True
            
        