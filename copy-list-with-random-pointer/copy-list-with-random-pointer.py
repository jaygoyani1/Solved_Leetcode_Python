"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return head
        
        curr = head
        while curr:
            new = Node(curr.val,None,None)
            
            new.next = curr.next
            curr.next = new
            curr = new.next
        
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
            
        old_list  = head
        new_list = head.next
        
        new_head = head.next
        
        while old_list:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None
            old_list = old_list.next
            new_list = new_list.next
        return new_head
            
        
            
        