class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def backtrack(comb,i):
            output.append(comb[:])
            for j in range(i,len(nums)):
                comb.append(nums[j])
                backtrack(comb,j+1)
                comb.pop()
            return
        
        backtrack([],0)
        return output
        