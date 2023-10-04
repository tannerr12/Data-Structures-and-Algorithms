# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        
        ansIdx = 0
        ans = [-1] * len(queries)
        mx = -1
        
        for i in range(len(queries)):
            queries[i] = [queries[i], i]
        
        queries.sort()
        
        def dfs(root):
            nonlocal mx,ansIdx
            if root is None:
                return None
            
            
            
            dfs(root.left)
            
            
            while ansIdx < len(queries) and root.val >= queries[ansIdx][0]:
                if queries[ansIdx][0] == root.val:
                    ans[queries[ansIdx][1]] = [root.val,root.val]    
                else:    
                    ans[queries[ansIdx][1]] = [mx, root.val]
                ansIdx += 1    
                
            mx = max(root.val, mx)    
            dfs(root.right)
            
        
        
        dfs(root)
        
        while ansIdx < len(queries):
            ans[queries[ansIdx][1]] = [mx, -1]
            ansIdx += 1
        
        return ans
            
            
        