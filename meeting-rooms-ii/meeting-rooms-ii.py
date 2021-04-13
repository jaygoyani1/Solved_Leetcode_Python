import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        if not intervals:
            return 0
        intervals.sort()
        heapq.heapify(heap)
        heapq.heappush(heap,intervals[0][1])
        
        for i in range(1,len(intervals)):
            
            if heap[0] > intervals[i][0]:
                heapq.heappush(heap,intervals[i][1])
            else:
                heapq.heappushpop(heap,intervals[i][1])
        return len(heap)