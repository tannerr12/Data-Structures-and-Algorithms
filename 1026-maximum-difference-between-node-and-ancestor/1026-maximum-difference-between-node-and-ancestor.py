# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        def dfs(root,parent):
            nonlocal res
            if root is None:
                return root
            
            for val in parent:
                res = max(res, abs(val - root.val))
            
            parent.append(root.val)
            dfs(root.left,parent)
            dfs(root.right,parent)
            
            parent.pop()
        
        
        dfs(root,[])
        
        return res