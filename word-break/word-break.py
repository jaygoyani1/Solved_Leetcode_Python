class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        memo = {}
        def backtrack(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            for w in words:
                if s[i:].startswith(w):
                    if backtrack(i+len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return backtrack(0)
        