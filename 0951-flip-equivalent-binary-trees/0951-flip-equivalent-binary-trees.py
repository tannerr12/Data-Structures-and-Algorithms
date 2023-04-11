# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        #just flip the tree ahead of time which makes it much easier than trying to flow through naturally
        def dfs(r1,r2):
            
            if r1 == r2:
                return True
            
            if r1 is None or r2 is None:
                return False
            
            if r1.val != r2.val:
                return False
            
            res = dfs(r1.left,r2.left) and dfs(r1.right,r2.right) or dfs(r1.left,r2.right) and dfs(r1.right,r2.left)
            
            return res
    
        
        return dfs(root1,root2)
            
                
            
            