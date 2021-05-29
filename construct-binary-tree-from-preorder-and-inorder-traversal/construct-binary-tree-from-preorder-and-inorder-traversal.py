# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        hashMap = {}
        
        for i in range(len(inorder)):
            hashMap[inorder[i]] = i
        
        def helper(left,right):
            if left>right:
                return None
            
            val = preorder.pop(0)
            root = TreeNode(val)
            
            index = hashMap[val]
            
            root.left = helper(left,index-1)
            root.right = helper(index+1,right)
            return root
        return helper(0,len(inorder)-1)
        