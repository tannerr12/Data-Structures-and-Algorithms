# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        adj = defaultdict(list)
        leafs = []
        
        def dfs(root):
            
            if root is None:
                return None
            
            if root.left:
                dfs(root.left)
                adj[root].append(root.left)
                adj[root.left].append(root)
            if root.right:
                dfs(root.right)
                adj[root].append(root.right)
                adj[root.right].append(root)
            
            if not root.left and not root.right:
                leafs.append(root)
            
        
        dfs(root)
        leafset = set(leafs)
        #print(adj)

        res = 0
        q= deque()
#        print(leafs)
        for val in leafs:
            level =0
            q= deque()
            q.append((val,None))
            while q:
                
                if level == distance + 1:
                    break
                for i in range(len(q)):
                    
                    node,par = q.popleft()
                    

                    if level > 0 and level <= distance and node in leafset:
                        res +=1
                        
                    for x in adj[node]:
                        if x == par:
                            continue
                        
                        q.append((x,node))
                    
                        
                    
                level += 1
            
            
        return res // 2