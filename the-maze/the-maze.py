class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        
        queue = [(start[0],start[1])]
        visited = set()
        visited.add((start[0],start[1]))
        
        dir  = [(0,1),(1,0),(0,-1),(-1,0)]
        while queue:
            a,b = queue.pop(0)
            if [a,b] == destination:
                return True
            for x,y in dir:
                i = a + x
                j = b + y
                while i>=0 and i < m and j>=0 and j< n and maze[i][j] == 0:
                    i += x
                    j += y
                if (i-x,j-y) not in visited:
                    queue.append((i-x,j-y))
                    visited.add((i-x,j-y))
        return False
