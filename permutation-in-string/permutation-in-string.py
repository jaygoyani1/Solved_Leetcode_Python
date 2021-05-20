class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        x =collections.Counter(s1)
        l = len(s1)
        for i in range(len(s2)):
            if collections.Counter(s2[i:i+l]) == x:
                return True
        return False
            
        