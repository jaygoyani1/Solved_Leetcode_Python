# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        ans = []
        q = [(root,0,0)]
        while q:
            n = len(q)
            for _ in range(n):
                node,i,j = q.pop(0)
                ans.append([j,i,node.val])
                
                if node.left:
                    q.append([node.left,i+1,j-1])
                if node.right:
                    q.append([node.right,i+1, j+1])
        ans.sort()   
        dic = {}
        for x,y,z in ans:
            if x in dic:
                dic[x].append(z)
            else:
                dic[x] = [z]
        return dic.values()
            
            
        