# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        #Working with an array instead of pointers made this problem far easier to solve
        def dfs(A,parent):
            #return element since we went down to 1
            if len(A) == 1:
                return TreeNode(A[0])
            
            #nothing
            if len(A) ==0:
                return None
            
            mid = 0
            
            #find last lower element
            for i in range(1,len(A)):
            
                if A[i] > A[0]:
                    break
                mid = i           
            #assign node to first element
            t = TreeNode(A[0])
            
            #lower elements
            t.left = dfs(A[1:mid+1],A[0])
          
            #higher elements
            t.right = dfs(A[mid+1:],A[0])
            
            #return Tree
            return t
        
        return dfs(preorder, preorder[0])
            
            
            