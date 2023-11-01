# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        s = defaultdict(int)
        def dfs(root):
            
            if not root:
                return [[],0]
            
            s[root.val] += 1
            dfs(root.left)
            
            dfs(root.right)
            
        
        dfs(root)
        
        mx = max(s.values())
        
        arr = []
        
        for key in s:
            if s[key] == mx:
                arr.append(key)
                
        
        return arr