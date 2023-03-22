# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        
        def dfs(root, lim):
            
            if root.right == root.left:
                return None if root.val < lim else root
        
            
            if root.left:
                root.left = dfs(root.left,lim - root.val)
               
            if root.right:
                root.right = dfs(root.right, lim - root.val)
       
            
            return root if root.left or root.right else None
        
        return dfs(root,limit)