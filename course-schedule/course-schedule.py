class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = collections.defaultdict(list)
        
        for pre in prerequisites:
            dic[pre[0]].append(pre[1])

        
        def dfs(i):
            if i in visiting:
                return False
            visiting.add(i)

            for nei in dic[i]:
                if nei in visiting:
                    return False
                if nei in visited:
                    continue
                if not dfs(nei):
                    return False
            visiting.remove(i)
            visited.add(i)
            return True

            
            
        visiting = set()
        visited = set()     
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False     
        return True