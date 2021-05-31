class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = []
        
        for i in sticks:
            heapq.heappush(heap, i)
        count = 0
        while len(heap) >1:
            val1 = heapq.heappop(heap)
            val2 = heapq.heappop(heap)
            count += (val1+val2)
            heapq.heappush(heap,val1+val2)
        return count
        