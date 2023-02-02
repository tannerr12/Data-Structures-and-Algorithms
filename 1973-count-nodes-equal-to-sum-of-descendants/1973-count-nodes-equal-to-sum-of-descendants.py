# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(root):
            nonlocal res
            if root is None:
                return 0
            
            
            current = dfs(root.left) + dfs(root.right)
            
            
            if current == root.val:
                res +=1
            
            return current + root.val
        
        
        dfs(root)
        return res
            