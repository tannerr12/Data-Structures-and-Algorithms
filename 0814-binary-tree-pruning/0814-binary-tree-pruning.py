# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def dfs(node):
            
            if node is None:
                return 0
            
            left = 0
            right = 0
            left = dfs(node.left)
            if left == 0:
                node.left = None
            
            right = dfs(node.right)
            if right == 0:
                node.right = None
            
            return left + right + node.val
        
        
        dfs(root)
        
        if root.left is None and root.right is None and root.val == 0:
            return None
        return root