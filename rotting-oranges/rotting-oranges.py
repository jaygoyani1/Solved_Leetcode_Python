class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lenx, leny = len(grid), len(grid[0])
        q = []
        fresh= 0
        for i in range(lenx):
            for j in range(leny):
                if grid[i][j] == 2:
                    q.append([i,j])
                if grid[i][j]  == 1:
                    fresh +=1
        if fresh ==0 and len(q) == 0:
            return 0
        time = -1
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            n = len(q)
            time +=1
            for _ in  range(n):
                row,col = q.pop(0)
                for x in dir:
                    x1 = x[0] + row
                    y1 = x[1] + col
                    if x1 < 0 or x1>=lenx or y1<0 or y1>=leny:
                        continue
                    if grid[x1][y1] == 1:
                        grid[x1][y1] = 2
                        fresh -= 1
                        q.append([x1,y1])
        return time if fresh==0 else -1 
                
                    
                    