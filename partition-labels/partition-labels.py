class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = collections.defaultdict(int)
        
        for i,char in enumerate(s):
            dic[char] = i
        
        start = 0
        end = 0
        maxi = 0
        result = []
        while end < len(s):
            
            maxi = max(dic[s[end]],maxi)
            if maxi == end:
                result.append(end-start+1)
                start = end + 1
            end += 1
        return result
                