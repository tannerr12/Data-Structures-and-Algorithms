# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root):
            nonlocal res
            if root is None:
                return -1,0
            
            val,total = root.val, 1
            r = 1
            
            x,y1 = dfs(root.left)
            if x == val:
                total += y1
                r = max(r, 1 + y1)    
            
            x,y2 = dfs(root.right)
            if x == val:
                total += y2
                r = max(r, 1 + y2)
            
            res = max(res, total)
            return val, r
        
        dfs(root)

        
        return res - 1 if res > 0 else 0