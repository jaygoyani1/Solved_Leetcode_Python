import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        heapq.heapify(ans)
        res = []
        for i in points:
            heapq.heappush(ans,(i[0]**2 + i[1]**2,i[0],i[1]))
        
        for i in range(k):
            x,a,b  = heapq.heappop(ans)
            res.append([a,b])
        return res