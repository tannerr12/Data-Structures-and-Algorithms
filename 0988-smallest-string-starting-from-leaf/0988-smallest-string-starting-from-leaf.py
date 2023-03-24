# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        res = []
        def dfs(root,par):
            
            if root is None:
                return ''
            left = '{'
            right = '{'
            if root.left:
                left = dfs(root.left,root.val)
            
            if root.right:
                right = dfs(root.right,root.val)
            
            
            ch = chr(root.val + ord('a'))
            chpar = chr(par + ord('a'))
            
            left = left + ch 
            right = right + ch
            if left + chpar <= right + chpar:
                new = left
            else:
                new = right
            
            if '{' in new:
                new = ch
            return new
         
        
        return dfs(root,0)
            