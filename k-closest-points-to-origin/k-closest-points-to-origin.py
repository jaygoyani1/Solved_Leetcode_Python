import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        h =[]
        for p in points:
            heapq.heappush(h,(p[0]**2+p[1]**2,p))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(h)[1])
        return res