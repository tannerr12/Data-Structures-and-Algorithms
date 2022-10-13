"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if root is None:
            return root
        q = deque()
        
        q.append(root)
        
            
        while q:
            count = len(q)
            for i in range(len(q)):
                
                node = q.popleft()
                count -=1
                if count != 0:
                    node.next = q[0]
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                
        
        
        return root
                
            