class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        lm = len(grid)
        ln = len(grid[0])
        dir = [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
        
        queue = [(0,0)]
        visited = set()
        visited.add((0,0))
        level = 0
        while queue:
            n = len(queue)
            level += 1
            for _ in range(n):
                (i,j) = queue.pop(0)
                if (i,j) == (lm-1,ln-1):
                    return level
                for x,y in dir:
                    a = x + i
                    b = y + j
                    if a<0 or a >= lm or b<0 or b>=ln or grid[a][b] == 1 or (a,b) in visited:
                        continue

                    visited.add((a,b))
                    queue.append((a,b))
        return -1