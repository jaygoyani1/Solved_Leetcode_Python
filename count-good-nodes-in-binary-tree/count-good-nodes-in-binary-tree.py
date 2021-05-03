# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 
        
        
        def dfs(node,maxsofar):
            if not node:
                return 0
            count = 0
            if node.val>=maxsofar:
                count+=1
            count+= dfs(node.left,max(maxsofar,node.val))
            count+= dfs(node.right,max(maxsofar,node.val))
            return count 
        
        return dfs(root,-float("inf"))