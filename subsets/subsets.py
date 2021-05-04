class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        
        def backtrack(comb,j):
            if len(comb) == len(nums):
                ans.append(comb[:])
                return
            ans.append(comb[:])
            
            for i in range(j,len(nums)):
                comb.append(nums[i])
                backtrack(comb,i+1)
                comb.pop()
        backtrack([],0)
        return ans