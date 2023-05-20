# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        @cache
        def dfs(root):
            
            if root is None:
                return (0,0)
            
            rob,donot = 0,0
            left = dfs(root.left)
            right = dfs(root.right)
            
            rob = root.val + left[1] + right[1]
            donot = max(left) + max(right)

            return [rob,donot]
        
        
        return max(dfs(root))
