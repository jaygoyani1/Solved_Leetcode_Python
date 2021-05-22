from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        
        for x,y in prerequisites:
            dic[x].append(y)
        
        
        def dfs(i):
            state[i] = 1
            for nexti in dic[i]:
                if state[nexti] == 2:
                    continue
                if state[nexti] == 1:
                    return False
                if not dfs(nexti):
                    return False
            state[i] = 2
            return True
            
        state = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
        
            
            
        
        
        