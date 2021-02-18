class Solution:
    def subarraysDivByK(self, nums: List[int], K: int) -> int:
        dic = defaultdict(int)
        curr = 0
        count = 0
        dic[0] = 1
        for i in range(len(nums)):
            curr += nums[i]
            remind = curr% K
            compliment = (K-remind)% K
            if compliment in dic:
                count += dic[compliment] 
                
            dic[compliment] += 1
            
        return count
        