# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = float('-inf')
        res = float('inf')
        def dfs(root):
            nonlocal prev
            nonlocal res
            if root is None:
                return float('inf')
                    
            
            dfs(root.left)
            res = min(res, abs(root.val - prev))
            prev = root.val
                
            dfs(root.right)
                
            
            
            return res
        
        return dfs(root)