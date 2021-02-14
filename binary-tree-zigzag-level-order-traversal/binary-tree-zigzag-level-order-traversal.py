# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([root])
        output = []
        ok = False
        while q:
            n = len(q)
            lvl = []
            
            for _ in range(n):
                node = q.popleft()
                lvl.append(node.val)
                for child in [node.left,node.right]:
                    if child:
                        q.append(child)
            if not ok:
                output.append(lvl)
            else:
                output.append(lvl[::-1])
            ok = not ok
        return output
        