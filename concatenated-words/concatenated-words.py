class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        wordset = set(words)
        
        def dfs(word):
            for i in range(1,len(word)):
                pre = word[:i]
                post = word[i:]
                
                if pre in wordset and post in wordset:
                    return True
                if pre in wordset and dfs(post):
                    return True
            return False
            
            
        
        
        result = []
        
        for i in words:
            if dfs(i):
                result.append(i)
        return result