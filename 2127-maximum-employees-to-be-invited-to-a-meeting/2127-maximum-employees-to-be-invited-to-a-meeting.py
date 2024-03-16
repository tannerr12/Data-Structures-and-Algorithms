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
        
       
        
        def dfsCycle(node, count, node_to_count, visited):
            if node in node_to_count:
                # Cycle detected. Return the cycle length.
                return count - node_to_count[node]
            if node in visited:
                # Node is already visited and not part of a cycle we're currently exploring.
                return 0

            # Mark the node as visited with its count.
            node_to_count[node] = count
            visited.add(node)

            # Recursively visit the favorite node.
            cycle_length = dfsCycle(favorite[node], count + 1, node_to_count, visited)

            # Once done, remove the node from the current path (but not from visited to avoid re-exploration).
            #del node_to_count[node]

            return cycle_length

        max_cycle_length = 0
        visited = set()

        for i in range(len(favorite)):
            if i not in visited:
                node_to_count = {}
                cycle_length = dfsCycle(i, 0, node_to_count, visited)
                max_cycle_length = max(max_cycle_length, cycle_length)

        # The rest of your logic for handling pairs and paths leading to them would follow here.
        # Return the maximum of max_cycle_length and the best sum of paths leading to two-person cycles.

      
        return max(ans,max_cycle_length) 
        
        
            
        
        
        
        
    