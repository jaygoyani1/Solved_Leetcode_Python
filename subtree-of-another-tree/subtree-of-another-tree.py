# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, r: TreeNode, sr: TreeNode) -> bool:
        def isSame(A,B):
            if A==None and B==None:
                return True
            if A==None or B==None:
                return False
            return A.val==B.val and isSame(A.left,B.left) and isSame(A.right,B.right)
    
        
        if r==None and sr==None:
            return True
        if r==None or sr==None:
            return False

        return isSame(r,sr) or self.isSubtree(r.left,sr) or self.isSubtree(r.right,sr)