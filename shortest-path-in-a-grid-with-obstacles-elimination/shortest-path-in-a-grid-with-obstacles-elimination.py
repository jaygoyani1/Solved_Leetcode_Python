class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        
        Queue = deque([(0,0,0,k)])
        visited = {}
        visited[(0,0)]=k
        while Queue:
            i,j,d,lifeline = Queue.popleft()
            
            if i==m-1 and j==n-1:
                return d
            
            for x,y in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if x>=0 and x<m and y>=0 and y<n:
                    if grid[x][y]==1:
                        if lifeline>0 and ((x,y) not in visited or visited[(x,y)]<lifeline-1):
                            visited[(x,y)] = lifeline-1
                            Queue.append((x,y,d+1,lifeline-1))
                    else:
                        if (x,y) not in visited or visited[(x,y)]<lifeline:
                            visited[(x,y)] = lifeline
                            Queue.append((x,y,d+1,lifeline))
        return -1
        