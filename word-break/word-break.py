class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        memo = {}

        def backtrack(index):
            if index in memo:
                return memo[index]
            if index == len(s):
                return True
            
            for w in words:
                if s[index:].startswith(w):
                    if backtrack(index+len(w)):
                        memo[index] = True
                        return True
            memo[index] = False
            return False
                    
            
        
        return backtrack(0)
            