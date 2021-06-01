class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lm = len(grid)
        ln = len(grid[0])
        
        fresh = 0
        queue = []
        visited = set()
        for i in range(lm):
            for j in range(ln):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    queue.append((i,j))

        time = -1
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        
        if fresh == 0:
            return 0
        while queue:
            n= len(queue)
            time+=1
            if fresh == 0:
                return time
            for _ in range(n):
                
                a,b = queue.pop(0)
                for x,y in dir:
                    p = a + x
                    q = b + y
                    if p<0 or p>=lm or q<0 or q>=ln or grid[p][q] !=1:
                        continue
                    grid[p][q] = 2
                    queue.append((p,q))
                    fresh-=1 
        return time if fresh == 0 else -1

            
        