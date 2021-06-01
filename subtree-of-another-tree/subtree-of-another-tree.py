# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def same (node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and same(node1.left,node2.left) and same(node1.right,node2.right)
        
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return same(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
    
    
    
    
    
#         def isSame(A,B):
#             if A==None and B==None:
#                 return True
#             if A==None or B==None:
#                 return False
#             return A.val==B.val and isSame(A.left,B.left) and isSame(A.right,B.right)
    
        
#         if r==None and sr==None:
#             return True
#         if r==None or sr==None:
#             return False

#         return isSame(r,sr) or self.isSubtree(r.left,sr) or self.isSubtree(r.right,sr)
        