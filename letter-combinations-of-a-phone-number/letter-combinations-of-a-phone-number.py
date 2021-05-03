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
        
        ans = []
        def backtrack(comb,index):
            if len(comb) == len(digits):
                ans.append("".join(comb))
                return
            

            word = KEYBOARD[digits[index]]
            for i in word:
                comb.append(i)
                backtrack(comb,index+1)
                comb.pop()
                
        backtrack([],0)
        return ans
                
                