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
        ans = []
        q = deque([root])
        while q:
            n = len(q)
            lvl = []
            for _ in range(n):
                x = q.popleft()
                lvl.append(x.val)
                for child in [x.left,x.right]:
                    if child is not None:
                        q.append(child)
            ans.append(lvl)
        return ans