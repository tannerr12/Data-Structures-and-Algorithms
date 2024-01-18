# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        
        
        arr = []
        
        def dfs(node):
            
            if node is None:
                return 0
            
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
   
        
        
        dfs(root)
        
        #print(arr)
        '''
        def search(node):
            
            if node is None:
                return 
        '''
        r = bisect_right(arr, target)
        l = r - 1
        
        ans = []
        while len(ans) < k:
            
            if l >= 0 and r < len(arr):
                if abs(arr[l] - target) <= abs(arr[r] - target):
                    ans.append(arr[l])
                    l-=1
                else:
                    ans.append(arr[r])
                    r += 1
            elif l >= 0:
                ans.append(arr[l])
                l-=1
            else:
                ans.append(arr[r])
                r += 1
        
        
        return ans
            