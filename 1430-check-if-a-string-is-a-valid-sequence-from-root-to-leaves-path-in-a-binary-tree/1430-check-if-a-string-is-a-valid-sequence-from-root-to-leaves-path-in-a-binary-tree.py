# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        
        for i in range(len(arr)):
            arr[i] = str(arr[i])
            
        p = ''.join(arr)
        #print(p)
        
        @cache
        def dfs(root, path):
            nonlocal p
            if root is None:
                return root
            
        
            res = False
            #try left
            res = res or dfs(root.left, path +  str(root.val))
            
            #try right
            res = res or dfs(root.right, path + str(root.val))
            
            
            if root.right is None and root.left is None and path + str(root.val) == p:
                return True
            
            return res
    
        
        
        return dfs(root,'')