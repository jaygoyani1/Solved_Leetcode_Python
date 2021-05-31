class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        def bfs(i,j):
            dir = [(0,1),(-1,0),(0,-1),(1,0)]
            queue = [(i,j)]
            visited = set()
            visited.add((i,j))
            count = -1
            while queue:
                n = len(queue)
                count+=1
                for _ in range(n):
                    a,b = queue.pop(0)
                    if grid[a][b] == "#":
                        return count
                    for p,q in dir:
                        x = a + p
                        y = b + q
                        if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y] == "X" or (x,y) in visited:
                            continue
                        queue.append((x,y))
                        visited.add((x,y))
            return -1
            
            
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "*":
                    return bfs(i,j)
        