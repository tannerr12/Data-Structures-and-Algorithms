# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        #divide and conquer 
        
        #we start with a sorted list from 1 -> N than we loop over each number and 
        #divide each left and right and repeat if nums is empty we return None
        #the left result becomes our left tree and the right result is our right tree
        #our root is I 
        
        def dfs(nums):
            
            if not nums:
                return [None]

            res = []
            
            for i in range(len(nums)):
        
                left = dfs(nums[:i])
                right = dfs(nums[i+1:])
                
                for t1 in left:
                    for t2 in right:
                        
                        res.append(TreeNode(nums[i], t1,t2))
            
            
            return res
        
        return dfs(list(range(1,n+1)))