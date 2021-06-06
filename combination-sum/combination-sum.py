class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(comb,summ,i):
            if summ > target:
                return
            if summ == target:
                result.append(comb[:])
                return
            
            for j in range(i,len(candidates)):
                comb.append(candidates[j])
                backtrack(comb,summ+candidates[j],j)
                comb.pop()
        backtrack([],0,0)
        return result
        