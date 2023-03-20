# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        
        def dfs(A,parent):
            
            if len(A) == 1:
                return TreeNode(A[0])
            if len(A) ==0:
                return None
            
            mid = 0
            
            for i in range(1,len(A)):
            
                if A[i] > A[0]:
                    break
                mid = i           
            
            t = TreeNode(A[0])
        
            t.left = dfs(A[1:mid+1],A[0])
          
            t.right = dfs(A[mid+1:],A[0])
            
            return t
        
        return dfs(preorder, preorder[0])
            
            
            