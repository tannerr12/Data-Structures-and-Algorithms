# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:

        res = 0
        
        def dfs(root):
            if not root or root.val == p or root.val == q:
                return root
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            if l and r:
                return root
            else:
                return l or r
                        
        
        
        
        def find(root,val):
            
            if not root:
                return float('inf')
            
            if root.val == val:
                return 0
            return 1 + min(find(root.left,val), find(root.right,val))
            
        lca = dfs(root)
        return find(lca,p) + find(lca,q)
    
    
    
    
