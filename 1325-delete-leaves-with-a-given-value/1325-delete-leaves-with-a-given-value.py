# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(root):
            
            if root is None:
                return root

            dfs(root.left)
            dfs(root.right)
            
            if root.left and root.left.val == -1:
                root.left = None
            if root.right and root.right.val == -1:
                root.right = None
            
            if root.right is None and root.left is None and root.val == target:
                root.val = -1
        
        
        dfs(root)
        
        return root if root.val != -1 else None
            