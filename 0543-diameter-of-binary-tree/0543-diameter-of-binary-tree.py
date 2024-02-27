# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter =0
        def dfs(root):
            
            if root is None:
                return 0
            
            
            
            l = dfs(root.left) 
            r = dfs(root.right)
            
            self.diameter = max(self.diameter, l+r)
            
            
            return max(l,r) +1
        
        dfs(root)
        return self.diameter
    
        
            