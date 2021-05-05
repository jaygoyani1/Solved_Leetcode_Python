class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        lenx, leny = len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[lenx-1][leny-1] != 0:
            return -1
        visited = {(0,0)}
        q = collections.deque([(0,0)])
        dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1) ]
        ans = 1
        while q:
            n = len(q)
            for _ in range(n):
                r,c = q.popleft()
                if (r,c) == (lenx-1,leny-1):
                    return ans
                for x in dir:
                    x1 = x[0] + r
                    y1 = x[1] + c
                    if x1 <0 or x1>=lenx or y1<0 or y1>=leny or grid[x1][y1] == 1:
                        continue
                    if (x1,y1) in visited:
                        continue
                    visited.add((x1,y1))
                    q.append((x1,y1))
            ans+=1
        return -1
                    