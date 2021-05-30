class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = collections.defaultdict(int)
        count = 0
        for t in time:
            curr = t % 60
            currmod = (60-curr)%60
            if currmod in dic:
                count += dic[currmod]
            dic[curr] += 1
        
        return count
            
        