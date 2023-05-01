# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        vals = []
        def dfsSum(root):
            
            if not root:
                return
                
            dfsSum(root.left)
            vals.append(root.val)
            dfsSum(root.right)
            
            
        
        dfsSum(root)
        mp = defaultdict(int)
        
        run = 0
        for i in range(len(vals)-1,-1,-1):
            v = vals[i]
            run += v
            mp[v] = run
            
        
        
        #print(mp)
        
        def dfs(root):
            
            if root is None:
                return
            
            
            dfs(root.left)
            dfs(root.right)
            
            root.val = mp[root.val]
            
            
        
        dfs(root)
        return root