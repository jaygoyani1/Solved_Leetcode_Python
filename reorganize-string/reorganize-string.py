class Solution:
    def reorganizeString(self, s: str) -> str:

        
        count = collections.Counter(s)
        
        heap = [(-val,i) for i,val in count.items()]
        
        heapq.heapify(heap)
        
        result = []
        
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            
            result.extend([x[1],y[1]])
            if x[0]<-1:
                heapq.heappush(heap,(x[0]+1,x[1]))
            if y[0] < -1:
                heapq.heappush(heap,(y[0]+1,y[1]))
        if heap:
            if heap[0][0] <-1:
                return ""
            result.append(heap[0][1])
        return "".join(result)
            
        
        