class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        lenm = len(rooms)
        lenn = len(rooms[0])
        
        queue = []
        visited = set()
        
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        
        for i in range(lenm):
            for j in range(lenn):
                if rooms[i][j] == 0:
                    queue.append(((i,j),0))
                    visited.add((i,j))
        while queue:
            n = len(queue)
            for _ in range(n):
                (a,b),val = queue.pop(0)
                if rooms[a][b] != -1:
                    rooms[a][b] = val
                for x,y in direction:
                    i = a+x
                    j = b+y
                    if i <0 or i>=lenm or j<0 or j>=lenn or rooms[i][j] == -1:
                        continue
                    if (i,j) not in visited:
                        visited.add((i,j))
                        queue.append(((i,j),val+1))
        
        
        
        
        return rooms