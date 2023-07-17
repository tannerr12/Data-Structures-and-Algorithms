# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = None
        def dfs(node):
            nonlocal ans
            if node is None:
                return [None, None]
            
            l1,r1 = dfs(node.left)
            l2,r2 = dfs(node.right)
            l, r = None,None
            if node.val == p.val:
                l = True
            if node.val == q.val:
                r = True
            l = l1 or l2 or l
            r = r1 or r2 or r
            if l and r and not ans:
                ans = node
            return [l,r]
            
            
        
        dfs(root)
        
        return ans
            