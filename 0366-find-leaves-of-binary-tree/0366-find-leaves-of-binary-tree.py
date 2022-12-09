# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        dp = defaultdict(list)
        #print(dp)
        def dfs(root):
            
            if root is None:
                return 0
            
            depth = 0
            depth = max(depth, dfs(root.left), dfs(root.right))
            
            
            dp[depth].append(root.val)
            
            
            return depth + 1
        
        
        dfs(root)
        

        return dp.values()
            