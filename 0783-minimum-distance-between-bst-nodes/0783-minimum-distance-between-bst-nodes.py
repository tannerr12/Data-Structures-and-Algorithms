# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root,parent):
            
            if root is None:
                return float('inf')
            
            res = float('inf')
            
            for val in parent:
                res = min(res, abs(root.val - val))
            parent.append(root.val)
            
            if root.left:

                res = min(res, abs(root.val - root.left.val), dfs(root.left,parent))
               
            if root.right:
                res = min(res, abs(root.val-root.right.val),dfs(root.right,parent))
                
            
            
            return res
        
        return dfs(root,[])