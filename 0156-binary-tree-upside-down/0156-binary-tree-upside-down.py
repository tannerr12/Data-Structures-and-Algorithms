# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pointer = None
        def dfs(root,par):
            nonlocal pointer
            if root is None:
                return None
            if root.left is None and root.right is None:
                pointer = root
            
            dfs(root.left, root)
            #dfs(root.right, root)
            
            if par:
                right = par.right
                par.left = None
                par.right = None
                root.right = par
                root.left = right
            
            
            return root
        
        dfs(root, None)
        return pointer
            