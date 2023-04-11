# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        def dfs(r1,r2):
            
            if not r1 and r2 or r1 and not r2:
                return False
            
            if not r1 and not r2:
                return True
            
            res = True
            
            if r1.val != r2.val:
                return False
            
            if (r1.left and r2.right and r1.left.val == r2.right.val) or r1.left == r2.right:
                r2.left,r2.right = r2.right, r2.left
            
            res = res and dfs(r1.left,r2.left)
            res = res and dfs(r1.right,r2.right)
            
            
            return res
    
        
        return dfs(root1,root2)
            
                
            
            