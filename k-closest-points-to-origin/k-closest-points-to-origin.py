import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x in points:
            dis = x[0]**2 + x[1]**2
            heapq.heappush(heap,(dis,x))
        output = []
        for i in range(K):
            x,y = heapq.heappop(heap)
            output.append(y)
        return output