class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(path,res,used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in nums:
                if i in used:
                    continue
                used.add(i)
                path.append(i)
                backtrack(path,res,used)
                path.pop()
                used.remove(i)
        used = set()
        res = []
        backtrack([],res,used)
        return res
        