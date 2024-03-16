class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        #we either end at our start node or we go back
        #if its a cycle it does not matter where you start 
        #cycles must be fully contained they cannot introduce non cycle elements
        #strongly connected components must be grouped
        #strongly connected components of size 2 can be placed in patches
        #but any size larger must be the full solution
        
        #cycle is either forward only in which it will end with the last node referencing the previous node
        
        #or cycle is cyclic where all the nodes create a loop
        
        #cycle = 3 + nodes
        #non cycle = 2 nodes
        
        #first we need to group all non cyclic loops by their size we can find the head bychecking non favorites
        #second once we know non cyclic we can check 
        
        #we either use 1 single cycle or peice 
        
        adj = defaultdict(list)
        
        favPairs = set()
        for i in range(len(favorite)):    
            adj[favorite[i]].append(i)
            
            if i == favorite[favorite[i]]:
                favPairs.add((min(i,favorite[i]), max(i, favorite[i])))
            
        
        favMap = defaultdict(int)
        
        #print(adj)
        seen = set()
        def dfs(cur,par):
            seen.add(cur)
            res = 0
            for val in adj[cur]:
                if val == par:
                    continue
                
                res = max(res, dfs(val,par) + 1)
            
            return res
        
        for x,y in favPairs:
            
            best1 = dfs(x,y)
            best2 = dfs(y,x)    
            favMap[(x,y)] = best1 + best2
        
        
        #print(favMap)
        
        ans = 0
        for key,val in favMap.items():
            ans += 2 + val
        
        mp = defaultdict(int)
        
        @cache
        def dfsCycle(node,count):
            
            if node in mp:
                if node not in s:
                    return float('-inf')
                return -mp[node]
            
            s.add(node)
            mp[node] = count
            
            res = float('-inf')
            res = max(res, dfsCycle(favorite[node], count + 1) + 1)
            
           
            return res
            
        for i in range(len(favorite)):
            if i not in seen:
                #check for largest cycle
                s = set()
                ans = max(ans, dfsCycle(i,0))
                #mp = defaultdict(int)
                
        return ans
        
        
            
        
        
        
        
    