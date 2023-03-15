# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        #bfs layer by layer tagging nodes in order and counting how many nodes per layer we see to verify the tree is correct
        
        q = deque()
        q.append((root,0))
        #what layer are we on?
        level = 0
        gap = 0
        while q:
            #how many nodes are we expecting
            nodes = 2 ** level
            
            #tag the nodes with ids
            num = 0
            last = -1
            
            #return false if 2 layers have gaps
            if gap:
                return False
            for i in range(len(q)):
                
                node,val = q.popleft()
                
                nodes -=1
                #check diff between nodes
                if abs(val - last) > 1:
                    return False
                last = val
                
                if node.left:
                    q.append((node.left,num))
                #increment id of nodes regardless
                num +=1
                if node.right:
                    q.append((node.right, num))
                num +=1
                
                #if we have a right and not a left auto fail
                if node.right and not node.left:
                    return False
                
            #we found a gap
            if nodes > 0:
                gap += 1
            #new level
            level +=1

        return True
                
                
                