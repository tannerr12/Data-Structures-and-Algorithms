# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        @cache
        def dfs(root,take):
            
            if root is None:
                return 0
            
            left,right = 0,0
            res = 0
            if take:
                left = max(left,dfs(root.left,False))
                right = max(right,dfs(root.right,False))
                res = max(res, left + right + root.val)
            left = max(left, dfs(root.left,True))
            right = max(right,dfs(root.right,True))
            res = max(res, left + right)
            
            
            return res
        
        
        return dfs(root,True)
