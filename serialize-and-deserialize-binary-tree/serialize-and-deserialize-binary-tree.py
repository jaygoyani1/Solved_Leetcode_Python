# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def dfs(node):
            if not node:
                ans.append("null")
                return
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data[0] == "null":
            del data[0]
            return None
        x = TreeNode(data[0])
        del data[0]
        x.left = self.deserialize(data)
        x.right = self.deserialize(data)
        return x
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))