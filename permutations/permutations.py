class Solution:
    def permute(self, l: List[int]) -> List[List[int]]:
        
        def backtrack(path,res,used):
            if len(path) == len(l):
                res.append(path[:])
                return
            for letter in l:
                if letter in used:
                    continue
                used.add(letter)
                path.append(letter)
                backtrack(path,res,used)
                path.pop()
                used.remove(letter)
        res = []
        used = set()
        backtrack([],res,used)
        return res