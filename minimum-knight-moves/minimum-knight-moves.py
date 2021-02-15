class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        visited = set()
        dir = [(2,1),(1,2),(1,-2),(2,-1),(-2,1),(-1,2),(-2,-1),(-1,-2)]
        
        q = [(0,0)]
        ans = 0
        while q:
            n = len(q)
            for _ in range(n):
                step = q.pop(0)
                if step == (x,y):
                    return ans
                for d in dir:
                    x1 = d[0] + step[0]
                    y1 = d[1] + step[1]
                    
                    if (x1,y1) in visited:
                        continue
                    visited.add((x1,y1))
                    q.append((x1,y1))
            ans +=1
                
                
                
                
                
            
            