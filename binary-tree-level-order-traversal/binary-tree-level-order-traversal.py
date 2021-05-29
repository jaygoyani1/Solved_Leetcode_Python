# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        result = []
        
        queue = [root]
        
        while queue:
            n = len(queue)
            temp = []
            for _ in range(n):
                tempNode = queue.pop(0)
                temp.append(tempNode.val)
                
                if tempNode.left:
                    queue.append(tempNode.left)
                if tempNode.right:
                    queue.append(tempNode.right)
            result.append(temp)
        
        return result