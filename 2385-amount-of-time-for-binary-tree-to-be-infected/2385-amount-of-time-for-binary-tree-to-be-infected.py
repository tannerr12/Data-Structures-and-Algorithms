# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        #need full depth both sides
        #need depth of target
        
        
        adj = defaultdict(list)
        
        def dfs(root):
            
            if not root:
                return
            
            if root.right:
                adj[root.val].append(root.right.val)
                adj[root.right.val].append(root.val)
                dfs(root.right)
            if root.left:
                adj[root.val].append(root.left.val)
                adj[root.left.val].append(root.val)
                dfs(root.left)
        
        
        dfs(root)
        
        #print(adj)
        
        #find deepest path starting at start
        
        q = deque()
        q.append(start)
        seen = set()
        seen.add(start)
        depth = 0
        while q:
            
            for i in range(len(q)):
            
                node = q.popleft()
                
                for val in adj[node]:
                    if val in seen:
                        continue
                    seen.add(val)
                    q.append(val)

            depth += 1
            
        
        return depth -1
            
            
            