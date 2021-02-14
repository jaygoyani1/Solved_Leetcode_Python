class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        def backtrack(comb,nums):
            output.append(comb[:])
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                comb.append(nums[i])
                backtrack(comb,nums[i+1:])
                comb.pop()
            return
        backtrack([],nums)
        return output
        
        