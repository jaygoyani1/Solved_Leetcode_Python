# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        smallhead = ListNode(0)
        bighead = ListNode(0)
        
        small, big = smallhead, bighead
        curr = head
        
        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                big.next = curr
                big = big.next
            curr = curr.next
            
        big.next = None
        small.next = bighead.next
        
        return smallhead.next
        