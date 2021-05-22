# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        arr = []
        
        
        def dfs(node,targetSum,curr_list):
            if not node:
                return
            curr_list.append(node.val)
            targetSum -= node.val

            if not node.left and not node.right and targetSum == 0:

                arr.append(curr_list[:])
            dfs(node.left,targetSum,curr_list)
            dfs(node.right,targetSum,curr_list)
            curr_list.pop()
            return
            
        dfs(root,targetSum,[])
        return arr