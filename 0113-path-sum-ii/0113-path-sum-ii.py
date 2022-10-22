# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        print(targetSum)
        res = []
        def dfs(root,curr,temp):
            
            if root is None:
            
                return root
            temp.append(root.val)
            curr += root.val
            if not root.left and not root.right:
                if curr == targetSum:
                    res.append(temp.copy())
            
            dfs(root.left,curr,temp )
            dfs(root.right,curr, temp)
            
            temp.pop()
            
            
            
        
        
        dfs(root,0,[])
        
        return res