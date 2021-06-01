# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        head = dummy
        
        heap = [] 
        
        for i,val in enumerate(lists):
            if val:
                heapq.heappush(heap,(val.val,i))
        
        while heap:
            val,ind = heapq.heappop(heap)
            head.next = ListNode(val)
            head = head.next
            if lists[ind].next:
                lists[ind] = lists[ind].next
                heapq.heappush(heap,(lists[ind].val,ind))
        return dummy.next
        