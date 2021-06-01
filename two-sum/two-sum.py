class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,j in enumerate(nums):
            remain = target - j
            if remain in dic:
                return [i,dic[remain]]
            dic[j] = i
        
        