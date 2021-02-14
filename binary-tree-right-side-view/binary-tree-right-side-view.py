# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        q = [root]
        while q:
            n = len(q)
            ans.append(q[0].val)
            for _ in range(n):
                node = q.pop(0)
                for child in [node.right, node.left]:
                    if child:
                        q.append(child)
        return ans
                        
                        
        
        