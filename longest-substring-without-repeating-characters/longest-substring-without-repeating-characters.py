class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        set1 = set()
        maxx = 0
        maximum = 0
        i = 0
        while i < len(s):
            if s[i] not in set1:
                set1.add(s[i])
                maxx+=1
            else:
                while s[j] != s[i]:
                    set1.remove(s[j])
                    j+=1
                    maxx-=1
                j+=1
            maximum = max(maximum,maxx)
            i+=1
        return maximum
                
                
                
                
            
        