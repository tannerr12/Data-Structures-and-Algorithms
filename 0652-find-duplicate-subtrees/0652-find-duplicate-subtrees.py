# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        seqMap = defaultdict(list)
        def dfs(root):
            
            if root is None:
                return 'N'
            
            seq = ''
            seq += dfs(root.left)
            seq += dfs(root.right)
            
        
            seq = str(root.val) + ',' + seq
            seqMap[seq].append(root)
            
            return seq
        
        dfs(root)
        #print(seqMap)
        
        res = []
        for key,val in seqMap.items():
            if len(val) > 1:
                res.append(val[0])
        
        
        return res