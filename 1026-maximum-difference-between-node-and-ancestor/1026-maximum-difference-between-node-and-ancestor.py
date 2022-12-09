# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        res = 0


        def dfs(root,s,l):
            nonlocal res
            
            if root is None:
                return root
            
            res = max(res,abs(root.val - s), abs(root.val - l))
            
            s = min(s,root.val)
            l = max(l,root.val)
            dfs(root.left,s,l)
            dfs(root.right,s,l)
            
        
        
        dfs(root,root.val,root.val)
        
        return res