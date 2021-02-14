# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([root])
        output = []
        while q:
            n = len(q)
            lvl = []
            for _ in range(n):
                node = q.popleft()
                lvl.append(node.val)
                for child in [node.left,node.right]:
                    if child:
                        q.append(child)
            output.append(lvl)
        return output
            
        
        