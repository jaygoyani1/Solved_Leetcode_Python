# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode()
        head = dummy
        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            
            val = n1 + n2 + carry
            
            num = val % 10
            
            carry = val // 10
            
            node = ListNode(num)
            head.next = node
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry >0:
            head.next = ListNode(carry)
        return dummy.next
    
        