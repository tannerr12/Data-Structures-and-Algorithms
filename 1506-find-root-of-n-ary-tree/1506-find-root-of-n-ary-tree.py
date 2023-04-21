"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        
        seen = set()
        
        for node in tree:
            
            for child in node.children:
                seen.add(child.val)
                
        
        for node in tree:
            
            if node and node.val not in seen:
                return node
                