"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        
      
        def dfs(node):
            
            if node is None:
                return node

            ncopy = Node(node.val)
            
            for child in node.children:
                ncopy.children.append(dfs(child))
            
            return ncopy
        
        
        
        
        return dfs(root)
        
            
            