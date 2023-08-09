# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        
        
        adj = defaultdict(list)
        
        
        def dfs(root):
            
            if root is None:
                return root
            
            if root.left:
                dfs(root.left)
                adj[root.val].append(root.left.val)
                adj[root.left.val].append(root.val)
            if root.right:
                dfs(root.right)
                adj[root.val].append(root.right.val)
                adj[root.right.val].append(root.val)
            
        
        dfs(root)
        
     
        def search(root,par):
            
            res = 0
            for val in adj[root]:
                if val == x or val == par:
                    continue
                res += search(val,root) + 1
            
            return res
        
        
        ans = 0
        for val in adj[x]:
            ans = max(ans, search(val,None))
        
        return ans >= n // 2
    
        
        
            
                
            