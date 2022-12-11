# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        h = root.val
        
        def dfs(root):
            nonlocal h
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)
            #eliminate 0s
            l = max(l,0)
            r = max(r,0)
            
            
            #triangle we can choose both left and right to include the root
            h = max(h,root.val + l + r)
            
            
            #left or right path only choose the largest and add the root
            return root.val + max(l,r)
        
        
        dfs(root)
        return h