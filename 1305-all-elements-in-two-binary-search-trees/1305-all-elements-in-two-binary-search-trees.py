# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        h = defaultdict(int)
        mx = float('-inf')
        mn = float('inf')
        def dfs(root):
            nonlocal mn 
            if root is None:
                return 0
            
            h[root.val] +=1
            mn = min(mn,root.val)
            val = max(root.val,dfs(root.left),dfs(root.right))
            return val
        
        
        
        mx = max(mx, dfs(root1), dfs(root2))

        
        res = []
        for i in range(mn,mx +1):
            
            if i in h:
                val = h[i]
                for j in range(val):
                    res.append(i)
        
        return res