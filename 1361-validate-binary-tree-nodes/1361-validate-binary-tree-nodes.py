class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        #each node should only be seen once
        #every node needs to be seen
        #we can start at the node that is not seen in left or right
        #if more than 1 node is not in left or right we return False
        #if no node is not seen it is invalid
        
        nodes = set([i for i in range(n)])

        for val in leftChild:

            if val in nodes:
                nodes.remove(val)
            
        
        for val in rightChild:
           
            if val in nodes:
                nodes.remove(val)
                
        

        if len(nodes) > 1 or len(nodes) == 0:
            return False
        
        q = deque()
        for val in nodes:
            q.append(val)
            
        seen = set()
        while q:
            
            node = q.popleft()
            if node in seen:
                return False
            seen.add(node)
            
            if leftChild[node] != -1:
                q.append(leftChild[node])
            
            if rightChild[node] != -1:
                q.append(rightChild[node])
            
            
        
        return len(seen) == n
            
        
        
        return True
    
    
    
        #0,1,2,3
        
        #2      #0
        #       1
        #3,-1
        #
            