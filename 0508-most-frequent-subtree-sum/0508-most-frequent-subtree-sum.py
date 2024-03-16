# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        mp = defaultdict(int)
        
        def dfs(node):
            
            if node is None:
                return 0
            
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            mp[left + right + node.val] += 1
            
            return left + right + node.val
        
        
        dfs(root)
        
        #print(mp)
        mx = max(mp.values())
        
        arr = []
        
        for key,val in mp.items():
            if val == mx:
                arr.append(key)
        
        return arr
            