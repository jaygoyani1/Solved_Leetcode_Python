# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = [root.val]
        
        queue = [root]
        
        while queue:
            n = len(queue)
            temp = []
            for _ in range(n):
                node = queue.pop(0)
                
                for child in [node.right,node.left]:
                    if child:
                        queue.append(child)
                        temp.append(child.val)
            if temp:
                result.append(temp[0])
        return result