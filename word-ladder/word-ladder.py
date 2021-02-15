from collections import defaultdict
from string import ascii_letters
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList:
            return 0
        q = [beginWord]
        ans = 0
        visited = set(wordList)
        while q:
            n = len(q)
            ans += 1
            for _ in range(n):
                word = q.pop(0)
                if word == endWord:
                    return ans
                for i in range(len(word)):
                    for j in ascii_letters:
                        w = word[:i] + j + word[i+1:]
                        if w in visited:
                            q.append(w)
                            visited.remove(w)
                        
          
        return 0
                        
        