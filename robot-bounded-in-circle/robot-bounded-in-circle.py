class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir = [(0,1),(1,1),(0,-1),(-1,-1)]
        x = y = 0
        index = 0
        for i in instructions:
            if i == "L":
                index = (index+3)%4
            elif i == "R":
                index = (index+1)%4
            else:
                x += dir[index][0]
                y += dir[index][1]
        return index!= 0 or (x==0 and y==0)  
            