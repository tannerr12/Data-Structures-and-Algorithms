"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        org = node.val
        while node.parent:
            node = node.parent
        
        ans = None
        def dfs(node):
            nonlocal ans,org
            
            if not node:
                return None
            
            if (ans == None or ans.val > node.val) and node.val > org:
                ans = node
                
            if node.val > org:
                dfs(node.left)
            else:
                dfs(node.right)
            
            return 
        
        dfs(node)
        
        return ans