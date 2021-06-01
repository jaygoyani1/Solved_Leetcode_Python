class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = []
        
        for num,unit in boxTypes:
            heapq.heappush(heap, (-unit,num))
        
        total = 0
        while truckSize >0 and len(heap) >=1:
            unit,num = heapq.heappop(heap)
            if truckSize >=num:
                total += num*(-unit)
                truckSize -= num
            else:
                total += truckSize*(-unit)
                break
        return total
                
        