# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        cnt = defaultdict(int)
        seqMap = {}
        res = []
        def dfs(root):
            
            if root is None:
                return 0
            
            seq = (dfs(root.left), root.val, dfs(root.right))
            #when we see a new sequence we assign a unique id to it
            if seq not in seqMap:
                seqMap[seq] = len(seqMap) + 1
            
            #we grab the id assigned to this sequence
            id = seqMap[seq]
            #increament the count of this sequences id
            cnt[id] +=1
            if cnt[id] == 2:
                res.append(root)
    
            #we return the id
            return id
        
        dfs(root)
        #print(seqMap)
        

        
        return res