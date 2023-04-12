# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        
        adj = defaultdict(list)
        start = None
        def dfs(root):
            nonlocal start
            if not root:
                return None
            
            if root == target:
                start = root
            
            if root.left:
                
                adj[root].append(root.left)
                adj[root.left].append(root)
                dfs(root.left)
                
                
            if root.right:
                
                adj[root].append(root.right)
                adj[root.right].append(root)
                dfs(root.right)    
            
            
        dfs(root)    

        q = deque()
        q.append([start,None])
        
        
        layer = 0
        
        res = []
        
        while q:
            
            for i in range(len(q)):
                
                node,par = q.popleft()
                
                if layer == k:
                    res.append(node.val)
                
                else:
                    
                    for val in adj[node]:
                        if val == par:
                            continue
                        
                        q.append([val,node])
        
            layer +=1
            
        
        return res