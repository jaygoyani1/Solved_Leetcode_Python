class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(i):

            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
                    
            
            
        visited = set()
        total = 0
        
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                total += 1
        
        return total