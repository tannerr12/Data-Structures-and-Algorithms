"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        
        rnode = Node()
        def dfs(node,ncopy):
            
            if node is None:
                return

            ncopy.val = node.val
            
            for child in node.children:
                ncopy.children.append(Node(child.val))
                dfs(child, ncopy.children[-1])
            
            return ncopy
        
        
        
        
        return dfs(root,rnode)
        
            
            