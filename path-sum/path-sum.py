# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        def inorder(node,curr_sum):
            if not node:
                return None
            curr_sum += node.val
            if curr_sum == targetSum and not node.left and not node.right:
                return True
            if node.left:
                if inorder(node.left,curr_sum):
                    return True
            if node.right:
                if inorder(node.right,curr_sum):
                    return True
        
        return inorder(root,0)
            
        
        
        
        
        
        