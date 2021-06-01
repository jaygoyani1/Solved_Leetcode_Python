class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(i,j):
            return (i)**2 + (j)**2
        heap = []
        
        for x,y in points:
            val = distance(x,y)
            heapq.heappush(heap,(val,[x,y]))
        
        result = []
        
        for i in range(k):
            _ ,curr = heapq.heappop(heap)
            result.append(curr)
        return result
            
        