# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(node, parent = None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        ans = []
        d = -1
        q = collections.deque([target])
        seen = {target}
        while q:
            n =len(q)
            d+=1
            for _ in range(n):
                node = q.popleft()
                if d == K:
                    ans.append(node.val)
                for child in [node.left,node.right,node.parent]:
                    if child:
                        if child in seen:
                            continue
                        seen.add(child)
                        q.append(child)
        return ans
                
            
        
        