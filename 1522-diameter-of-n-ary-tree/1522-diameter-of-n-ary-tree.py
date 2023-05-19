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
            
            mxdepth = 0
            for val in root.children:
                v = dfs(val) + 1
                res = max(res, mxdepth + v)
                mxdepth = max(mxdepth, v)
  
            return mxdepth
        
        dfs(root)
        
        return res
            