class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in dic:
                return [i,dic[t]]
            dic[nums[i]] = i
        
        