class Solution:
    def permute(self, l: List[int]) -> List[List[int]]:
        
        ans = []
        
        def backtrack(comb,used):
            if len(comb) == len(l):
                ans.append(comb[:])
                return
            
            for i in range(len(l)):
                if not used[i]:
                    used[i] = True
                    comb.append(l[i])
                    backtrack(comb,used)
                    used[i] = False
                    comb.pop()
        backtrack([],[False]*len(l))
        return ans