# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def dfs(node,leftmax,rightmax):
            if not node:
                return True
            if not(leftmax < node.val < rightmax):
                return False
            return dfs(node.left,leftmax,node.val) and dfs(node.right,node.val,rightmax)
            
        
        
        return dfs(root,-float("inf"),float("inf"))
        