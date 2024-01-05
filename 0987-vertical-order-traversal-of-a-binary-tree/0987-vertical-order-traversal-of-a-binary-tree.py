# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        mp = defaultdict(lambda: defaultdict(list))
        def dfs(root, r, c):
            
            if not root:
                return
            
            mp[c][r].append(root.val)
            dfs(root.left, r + 1, c -1)
            dfs(root.right, r + 1, c + 1)
            
        
        dfs(root,0,0)
        #print(mp)
        ans = []
        
        for c in sorted(mp):
            arr = []
            for r in sorted(mp[c]):
                for val in sorted(mp[c][r]):
                    arr.append(val)
            ans.append(arr)
        
        return ans
            