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
            
  
            vals = []
            
            for val in root.children:
                vals.append(dfs(val) + 1)
                
            vals.sort()
            if len(vals) >= 2:
                res = max(res, vals[-1] + vals[-2])
            elif len(vals) == 1:
                res = max(res, vals[-1])
            else:
                return 0
            return vals[-1]
        
        dfs(root)
        
        return res
            