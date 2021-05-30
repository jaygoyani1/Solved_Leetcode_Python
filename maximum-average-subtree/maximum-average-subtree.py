# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        maximum = [0]
        def helper(node):
            if not node:
                return (0,0)
            curr = node.val
            
            left_sum,left_count = helper(node.left)
            right_sum,right_count = helper(node.right)
            
            curr_sum = curr + left_sum + right_sum
            curr_count = 1+left_count+right_count
            
            average = curr_sum/curr_count
            maximum[0] = max(maximum[0],average)

            return (curr_sum,curr_count)
        
        helper(root)
        return maximum[0]