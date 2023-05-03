# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, end: int) -> int:
        
        adj = defaultdict(list)
        start = None
        
        def dfs(root):
            nonlocal start
            if not root:
                return 
            
            if root.val == p:
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
        
        
        q = deque([start])
        layer = 0
        seen = set()
        seen.add(start)
        while q:
            
            for i in range(len(q)):
                
                node = q.popleft()
                
                if node.val == end:
                    return layer
                
                for x in adj[node]:
                    if x not in seen:
                        seen.add(x)
                        q.append(x)
            layer +=1
                    