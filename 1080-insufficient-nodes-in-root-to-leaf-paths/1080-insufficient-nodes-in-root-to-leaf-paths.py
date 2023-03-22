# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        #we dfs all the way to the bottom of the tree subtracting the roots value from our current limit
        #if any of our leaf nodes are less than limit after this pass subtraction we remove it and return None else we return that node
        #if we do encounter an non leaf where both the left and right were removed inclusive of the current node value we return None stating 
        #that this entire tree is safe to remove. Eventually at the end we return the source root
        def dfs(root, lim):
            
            if root.right == root.left:
                return None if root.val < lim else root
        
            
            if root.left:
                root.left = dfs(root.left,lim - root.val)
               
            if root.right:
                root.right = dfs(root.right, lim - root.val)
       
            
            return root if root.left or root.right else None
        
        return dfs(root,limit)