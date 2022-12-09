# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        



        def dfs(root,s,l):

            if root is None:
                return 0
            
            res = max(abs(root.val - s), abs(root.val - l))
            s = min(s,root.val)
            l = max(l,root.val)
            res = max(res,dfs(root.left,s,l),dfs(root.right,s,l))
            
            
            return res
            
        
        
        return dfs(root,root.val,root.val)
        
     