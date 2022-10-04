# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        

        def dfs(root,s):
 
            if root is None:
                return False 
            
            s -= root.val
            if not root.left and not root.right:
                return s == 0
            
            l = dfs(root.left,s)
            r = dfs(root.right,s)
            
            
            return (l or r)
        
        
        return dfs(root,targetSum)


    
    