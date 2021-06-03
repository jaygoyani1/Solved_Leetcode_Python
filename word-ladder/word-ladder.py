class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        dic = collections.defaultdict(list)
        
        l = len(beginWord)
        for word in wordList:
            
            for i in range(l):
                dic[word[:i]+"*"+word[i+1:]].append(word)
        
        queue = [beginWord]
        visited = set()
        total = 0
        while queue:
            n = len(queue)
            total += 1
            for _ in range(n):
                x = queue.pop(0)
                
                for i in range(l):
                    wordfind = x[:i] + "*" + x[i+1:]

                    for allword in dic[wordfind]:
                        if allword == endWord:
                            return total + 1
                        if allword not in visited:
                            visited.add(allword)
                            queue.append(allword)
                    dic[wordfind] = []
                    
                
                
        return 0
        
                
                