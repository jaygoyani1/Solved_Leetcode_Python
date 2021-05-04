class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def backtrack(comb,total,j):
            if total == target:
                ans.append(comb[:])
                return
            if total> target:
                return
            for i in range(j,len(candidates)):
                comb.append(candidates[i])
                total += candidates[i]
                backtrack(comb,total,i)
                total -= candidates[i]
                comb.pop()
        backtrack([],0,0)
        return ans