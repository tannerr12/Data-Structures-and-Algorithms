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
            
            rob,donot = 0,0
            
            if take:
                rob = root.val + dfs(root.left,False) + dfs(root.right,False)
            donot = dfs(root.left,True) + dfs(root.right,True)

            return max(rob,donot)
        
        
        return dfs(root,True)
