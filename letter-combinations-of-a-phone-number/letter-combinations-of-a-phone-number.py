class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: 
            return []
        KEYBOARD = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        def backtrack(path,res,i):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            x = digits[i]
            for l in KEYBOARD[x]:
                path.append(l)
                backtrack(path,res,i+1)
                path.pop()
        res = []
        backtrack([],res,0)
        return res