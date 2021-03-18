class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        used = [False]*len(nums)
        def backtrack(res,used):
            if len(res) == len(nums):
                output.append(res[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                res.append(nums[i])
                backtrack(res,used)
                res.pop()
                used[i] = False
        backtrack([],used)
        return output