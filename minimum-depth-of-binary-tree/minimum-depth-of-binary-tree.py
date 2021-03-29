# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        lvl = 0
        q = deque([root])
        while q:
            n = len(q)
            lvl+=1
            for _ in range(n):
                node = q.popleft()
                if not node.left and not node.right:
                    return lvl
                for child in [node.left,node.right]:
                    if child is not None:
                        q.append(child)
        return 0