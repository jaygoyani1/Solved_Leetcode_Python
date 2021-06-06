class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        result = []
        
        def backtrack(comb,visited):
            if len(comb) == len(nums):
                result.append(comb[:])
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    comb.append(nums[i])
                    backtrack(comb,visited)
                    visited[i] = False
                    comb.pop()
        backtrack([],[False]*len(nums))
        return result