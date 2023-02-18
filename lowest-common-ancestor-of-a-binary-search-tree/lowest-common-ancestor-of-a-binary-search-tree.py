# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def search(r):
 
            v = r.val
            
            if p.val > v and q.val > v:
                return search(r.right)
            elif p.val < v and q.val < v:
                return search(r.left)
            else:
                return r

           
            
            
        
        
     
        return search(root)
     
            