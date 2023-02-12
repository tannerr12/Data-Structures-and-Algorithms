"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
    
        visit = {}
       
        def dfs(n):
            if n is None:
                return n
            if n in visit:
                return visit[n]
        
            v = Node(n.val)
            visit[n] = v
            for x in n.neighbors:
                
                v.neighbors.append(dfs(x))
                
            return v
                
         
    
        return dfs(node)
      