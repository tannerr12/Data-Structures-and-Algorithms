class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        
        dict1,ans,res = defaultdict(set), [],[]
        #seperate weighted edges from negative weighted edges
        for i,j,w in edges:
            if w != -1:
                dict1[i].add((j,w))
                dict1[j].add((i,w))
                res.append([i,j,w])
            else:
                ans.append((i,j))
                

        def dfs(src,des):
            dist = [2 * 10 ** 9 for _ in range(n)]
            
            dist[src] = 0
            
            stack,res = [(src,0)], []
            
            while stack:
                
                node,val = heappop(stack)
                
                for neighbor,weight in dict1[node]:
                    if dist[neighbor] > weight + val:
                        dist[neighbor] = weight + val
                        heappush(stack, (neighbor, weight + val))
            
            return dist
        
        #first search it without negative edges to see if there is a shortest path from source to dest
        #less than our target if so return []
        if dfs(source,destination)[destination] < target: return []
        
        i,m = 0, len(ans)
        #we will loop over all of our negative weighted edges and mark them as 1s
        #we add the edges 1 by 1 and see if our shortest path is the target
        while i < m and dfs(source, destination)[destination] > target:
            a,b = ans[i]
            i += 1
            dict1[a].add((b,1))
            dict1[b].add((a,1))
        
            #if we can get to the destination with this new edge we can make it = to the remainder of our target - our                  current cost
            if dfs(source,destination)[destination] <= target:
                #add this value = target - curr cost + 1 to make the dist == target and break early
                res.append([a,b,1+target-dfs(source,destination)[destination]])
                break
        
            
            #otherwise we just set this edge cost to 1
            res.append([a,b,1])
            
        #check if after adding edges our cost is > target since we are forced to add all the edges > 0
        if dfs(source,destination)[destination] > target: return []
        
        #do this if we broke early set the rest of the edges to max number since we dont need them
        #and they should be used as barriers to make sure the best path is elsewhere
        while i < m:
            a,b = ans[i]
            res.append([a,b,2*10**9])
            i+=1
            
        return res