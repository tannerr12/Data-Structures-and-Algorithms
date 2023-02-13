"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        
        q.append(root)
        res = [[root.val]]
        while q:
            ls = []
            for i in range(len(q)):
                
                node = q.popleft()
                if node.children:
                    for child in node.children:
                        ls.append(child.val)
                        q.append(child)
            if ls:
                res.append(ls.copy())
            
            
        
        return res