# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        
        q = deque([[root, None]])
        parMap = {}
        parMap[root] = None
        dist = 0
        depth = defaultdict(list)
        while q:
            
            for i in range(len(q)):
                
                node,par = q.popleft()
                parMap[node] = par
                depth[dist].append([node, par])
                if node.left:
                    q.append([node.left, node])
                if node.right:
                    q.append([node.right, node])
                
                
            
            dist += 1
            
        
        dist -=1
        
        q = deque(depth[dist])
        seen = set()
        while q:
            if len(q) == 1:
                return q[0][0]
            
            for i in range(len(q)):
                node,par = q.popleft()
                if par not in seen:
                    q.append([par, parMap[par]])
                    
                seen.add(par)
                
                
                
                

            
        
        
        