# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root.left is None and root.right is None:
            return root
        
        def countLeaves(node):
            
            q = deque([node])
            total = 0
            d = 0
            while q:
                total = len(q)    
                for i in range(len(q)):
                    
                    n = q.popleft()
                    
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                d += 1
            
            return [total,d]
        
        leaves,d = countLeaves(root)
        
        def dfs(node,depth):
            nonlocal leaves,d
            if node is None:
                return [0,None]
            
            if node.left == None and node.right == None:
                if depth == d:
                    if leaves > 1:
                        return [1,None]
                    return [1,node]
                return [0,None]
            
            res = 0
            
            res1,n1 = dfs(node.left,depth + 1)
            res2,n2 = dfs(node.right,depth + 1)
            
            res = res1 + res2
            if n1:
                return [res, n1]
            elif n2:
                return [res, n2]
            elif res == leaves:
                return [res, node]
            else:
                return [res, None]
            
            
        
        ans = dfs(root,1)
        return ans[1]