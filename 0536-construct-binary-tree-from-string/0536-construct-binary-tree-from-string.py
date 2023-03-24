# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        
        
        def dfs(A):
            if len(A) == 0:
                return None
            if '(' not in A:
                return TreeNode(int(A))
            
            
            v = ''
            idx = 0
            while A[idx] != '(':
                v += A[idx]
                idx +=1
            tree = TreeNode(int(v))
            
            stack = ['(']
            mid = idx + 1
            #find left 
            while stack:
                if A[mid] == ')':
                    stack.pop()
                elif A[mid] == '(':
                    stack.append('(')
                
                mid +=1
            #left
            tree.left = dfs(A[idx+1:mid-1])
            tree.right = dfs(A[mid+1:-1])
            
            return tree
        
        return dfs(s)
            
            
            