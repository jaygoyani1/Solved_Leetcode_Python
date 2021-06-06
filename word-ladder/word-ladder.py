class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        dic = collections.defaultdict(list)
        
        
        for  i in wordList:
            for j in range(len(i)):
                dic[i[:j]+"*"+i[j+1:]].append(i)
        visited = set()
        q = [beginWord]
        total = 0
        while q:
            n = len(q)
            total +=1
            for i in range(n):
                wording = q.pop(0)
                if wording == endWord:
                    return total
                for i in range(len(wording)):
                    tofind = wording[:i]+"*"+wording[i+1:]
                    
                    for x in dic[tofind]:
                        if x not in visited:
                            if x == endWord:
                                return total+1
                            q.append(x)
                            visited.add(x)
                    dic[tofind] = []
        return 0
        
                
                