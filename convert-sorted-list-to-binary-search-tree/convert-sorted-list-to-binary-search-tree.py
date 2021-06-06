# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        def map(head):
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            return arr
        
        arr = map(head)
        def convert(l,r):
            if (l>r):
                return None
            mid = (l+r)//2
            
            node = TreeNode(arr[mid])
            if l ==r:
                return node
            node.left = convert(l,mid-1)
            node.right = convert(mid+1,r)
            return node
        return convert(0,len(arr)-1)
            