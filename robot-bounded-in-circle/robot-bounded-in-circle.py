class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        x = 0
        y = 0
        id = 0
        
        for i in instructions:
            if i == "L":
                id = (id+3)%4
            elif i == "R":
                id = (id + 1)%4
            else:
                x += dir[id][0]
                y += dir[id][1]
        return (x==0 and y==0) or id!=0
        
        
        