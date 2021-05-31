class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = collections.defaultdict(int)
        
        for i in arr:
            dic[i] += 1
        heap = []
        
        for i in dic:
            heapq.heappush(heap,(dic[i],i))
        
        while k>0:
            val, i = heapq.heappop(heap)
            if val <= k:
                k-=val
            else:
                heapq.heappush(heap,(val,i))
                break
        return len(heap)