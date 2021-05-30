# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        
        head = dummy
        if not l1:
            return l2
        if not l2:
            return l1
        
        while l1 and l2:
            v1 = l1.val 
            v2 = l2.val 
            

            if v1<v2:
                mini = v1
                l1 = l1.next
            else:
                mini = v2
                l2 = l2.next

            
            head.next = ListNode(mini)
            head = head.next
        
        if l1:
            head.next = l1
        else:
            head.next = l2
        
        return dummy.next