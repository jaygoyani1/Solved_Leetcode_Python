class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def backtrack(path,target,index):
            if target == 0:
                output.append(path[:])
                return
            if target < 0 :
                return
            for i in range(index,len(candidates)):
                path.append(candidates[i])
                backtrack(path,target-candidates[i],i)
                path.pop()
            return

        backtrack([],target,0)
        return output
        