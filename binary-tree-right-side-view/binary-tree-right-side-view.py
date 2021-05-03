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
        
        def dfs(node,index):
            if index == len(ans):
                ans.append(node.val)
            for child in [node.right,node.left]:
                if child:
                    dfs(child,index+1)
        dfs(root,0)
        return ans
                        
        
        