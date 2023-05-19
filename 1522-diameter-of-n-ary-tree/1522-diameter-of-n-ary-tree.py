"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        res = 0
        
        def dfs(root):
            nonlocal res
            
            if root is None:
                return 0
            
            great1,great2 = 0,0
            for val in root.children:
                v = dfs(val) + 1
                
                if v >= great1:
                    great2 = great1
                    great1 = v
                elif v > great2 and v < great1:
                    great2 = v
                
   
            res = max(res, great1 + great2)

            return great1
        
        dfs(root)
        
        return res
            