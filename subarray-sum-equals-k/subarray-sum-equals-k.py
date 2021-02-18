class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        curr = 0
        count = 0
        for i in range(len(nums)):
            curr += nums[i]
            diff = curr - k 
            if diff in dic:
                count += dic[diff] 
                
            if curr in dic :
                dic[curr]  += 1
            else:
                dic[curr] = 1
            
        return count
            
        