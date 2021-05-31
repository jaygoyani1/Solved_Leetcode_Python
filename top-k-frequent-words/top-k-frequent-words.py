class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        dic = collections.defaultdict(int)
        
        for i in words:
            dic[i] += 1
        
        heap = []
        
        for i in dic:
            heapq.heappush(heap, (-dic[i],i))
        
        result = []
        
        for i in range(k):
            _,word = heapq.heappop(heap)
            result.append(word)
        return result
        
        
        