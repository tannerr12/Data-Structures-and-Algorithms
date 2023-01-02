# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return None
        
        @cache
        def dfs(i):
            
            if i == 0:
                return []
            if i == 1:
                return [TreeNode()]
            
            res = []
            
            for j in range(i):
                r = i - j  -1
                left = dfs(j)
                right = dfs(r)
            
                
                for t1 in left:
                    for t2 in right:
                        res.append(TreeNode(0,t1,t2))
            
            return res
        
        
        return dfs(n)

            