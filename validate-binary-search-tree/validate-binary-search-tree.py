# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def validate(node,mini,maxi):
            if not node:
                return True

            if not(mini<node.val<maxi):
                return False
            
            return validate(node.left,mini,node.val) and validate(node.right,node.val,maxi)
            
        return validate(root,-float("inf"),float("inf"))
                
        