# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        
        if root.left is None and root.right is None:
            return root.val
        adj = defaultdict(list)
        leafs = set()
        def dfs(root,par):
            if not root:
                return
            
            if par:
                adj[par].append(root.val)
                adj[root.val].append(par)
            
            if root.left is None and root.right is None:
                leafs.add(root.val)
            if root.left:
                dfs(root.left, root.val)
            if root.right:
                dfs(root.right, root.val)
        
        dfs(root,0)
        #print(adj)
        q = deque()
        q.append(k)
        seen = set()
        seen.add(k)
        level = 0
      
        dist = [0] * len(adj)
        
        while q:
            
            for i in range(len(q)):
                
                node = q.popleft()
                if node in leafs:
                    return node
                
                for x in adj[node]:
                    
                    if x in seen:
                        continue
                    
                    seen.add(x)
                    q.append(x)
                    