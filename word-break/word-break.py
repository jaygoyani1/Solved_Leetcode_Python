class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordset = set(wordDict)
        memo = {}
        def backtrack(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                memo[i] = True
                return True
            
            for word in wordset:
                if s[i:].startswith(word):
                    if backtrack(i+len(word)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
            
            
        
        return backtrack(0)