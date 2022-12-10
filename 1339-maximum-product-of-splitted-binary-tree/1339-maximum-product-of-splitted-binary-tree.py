# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(root):
            
            if root is None:
                return 0
            
            
            root.val = root.val + dfs(root.left) + dfs(root.right)
            
            
            return root.val
    
    
        
        dfs(root)
        s = root.val
        
        def findMax(root,s):
            
            if root is None:
                return 0
            
            val = max(root.val * (s - root.val), findMax(root.left,s), findMax(root.right,s))
            
            
            return val
            
            
        return findMax(root,s) % (10**9 +7)
        
        
        print(root)