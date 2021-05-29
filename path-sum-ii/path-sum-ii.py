# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        result = []
        if not root:
            return []
        
        def dfs(node,currSum,comb):
            if not root:
                return
            if currSum == targetSum and not node.left and not node.right:
                result.append(comb[:])
            for child in [node.left,node.right]:
                if child:
                    comb.append(child.val)
                    dfs(child,currSum+child.val,comb)
                    comb.pop()

        dfs(root,root.val,[root.val])
        return result
                