# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        res = 0
        
        h = defaultdict(int)
        h[targetSum] = 1
        
        
        def dfs(root,temp):
            nonlocal res
            if root is None:
                return 0
            
            temp += root.val 
            res += h[temp]
            h[temp+targetSum] +=1
            
            dfs(root.left,temp)
            dfs(root.right,temp)
            
            
            h[temp+targetSum] -=1
            
        
        
        dfs(root,0)
        
        
        return res
            