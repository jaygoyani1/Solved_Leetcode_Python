import heapq
from collections import defaultdict
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        res = []
        students = defaultdict(list)
        
        for x,y in items:
            heapq.heappush(students[x],-y)
        
        for student in students:
            avg = sum(-heapq.heappop(students[student]) for x in range(0,5))//5
            res.append((student,avg))
        res.sort()
        return res
            