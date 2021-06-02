# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        result = []
        if not root:
            return result
        queue = [root]
        direction = 1
        while queue:
            n = len(queue)
            temp =[]
            for _ in range(n):
                node = queue.pop(0)
                temp.append(node.val)
                for child in [node.left,node.right]:
                    if child:
                        queue.append(child)
            result.append(temp[::direction])
            direction =-direction
        return result
        