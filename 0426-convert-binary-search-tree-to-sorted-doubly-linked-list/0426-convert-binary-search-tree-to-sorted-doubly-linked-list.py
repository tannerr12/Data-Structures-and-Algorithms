"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        arr = []
        def pLL(n):
            idx = 0
            nt = n

             
            n = nt 
            idx = 0
            while n and idx < 20:
                print(n.val)
                n= n.left
                idx +=1
                
        arr = []
        mn =Node(float('inf'))
        mx = Node(float('-inf'))
        def dfs(root,par):
            nonlocal mn
            nonlocal mx
            if root is None:
                return 
            
            
            if root.val < mn.val:
                mn = root
            if root.val > mx.val:
                mx = root
            prev = dfs(root.left,root)
            arr.append([root.val, root])
            nxt = dfs(root.right,root)
            
   
            return root
        
        dfs(root,-1)
        
        arr.sort()
        #print(arr)
        
        #mx.right = mn
        #mn.left = mx
        for i in range(len(arr)):
            l,r = i - 1,i + 1
            if r >= len(arr):
                r = 0
            arr[i][1].right = arr[r][1]
            if l < 0:
                l = len(arr)-1
            arr[i][1].left = arr[l][1]
            
        
        return mn
            
            
        #pLL(mn)
        
        #return mn
        
        