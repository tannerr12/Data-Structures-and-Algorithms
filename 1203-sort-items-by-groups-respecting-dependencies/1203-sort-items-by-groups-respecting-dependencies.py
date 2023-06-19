class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        
        adj = defaultdict(list)
        grouping = defaultdict(set)
        sameGroup = defaultdict(set)
        for i in range(n):
            beforeItems[i] = set(beforeItems[i])
            grouping[group[i]].add(i)
                    
        
        #print(beforeItems)
        #define the ordering for each groups internals first
        grop = {}
        
        
        for val in grouping:
            adj = defaultdict(set)
            outdegree = defaultdict(int)
            for v in grouping[val]:
                for i in beforeItems[v]:
                    if i in grouping[val]:
                        adj[i].add(v)
                        outdegree[v] += 1
            
            q = deque()
            for v in grouping[val]:
                if outdegree[v] == 0:
                    q.append(v)
                
            if len(q) == 0:
                return []
            seen = set()
            res = []
            while q:
                
                for i in range(len(q)):
                    node = q.popleft()
                    if node in seen:
                        return []
                    res.append(node)
                    seen.add(node)
                    for x in adj[node]:
                        outdegree[x] -=1
                        
                        if outdegree[x] == 0:
                            q.append(x)
                        
            
            grop[val] = res
            
        #print(grop[-1])
         
        #handle non same group requirements
        #put all the -1 groups into there own groups?
        
        adj = defaultdict(set)
        outdegree = defaultdict(set)
        for val in grouping:
            if val == -1:
                continue
            for v in grouping[val]:
                for i in beforeItems[v]:
                    if i not in grouping[val]:
                        if group[i] == -1:
                            adj[-i-2].add(val)
                            outdegree[val].add(-i-2)
                        else:
                            adj[group[i]].add(val)
                            outdegree[val].add(group[i])
                        
        #add -1 groups
        
        for val in grouping[-1]:
            for i in beforeItems[val]:
                    if group[i] == -1:
                        adj[-i-2].add(-val-2)
                        outdegree[-val-2].add(-i-2)
                    else:
                        adj[group[i]].add(-val-2)
                        outdegree[-val-2].add(group[i])
         
        
        q = deque()
        for v in grouping:
            if v == -1:
                continue
            if len(outdegree[v]) == 0:
                q.append(v)
        added = set()
        for v in grouping[-1]:
            if len(outdegree[-v-2]) == 0:
                q.append(-v-2)
                added.add(-v-2)
        if len(q) == 0:
            return []
        seen = set()
        res = []
        idx = 0
        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node in seen:
                    return []
                res.append(node)
                seen.add(node)
            
                
                for x in adj[node]:
                    outdegree[x].remove(node)

                    if len(outdegree[x]) == 0:
                        q.append(x)

        
        #print(res)
        #grop[val] = res
        ans = []
 
        for i in range(len(res)):
            if res[i] < 0:
                ans.append(-res[i]-2)
              
            else:
                for val in grop[res[i]]:
                    ans.append(val)
        
        if len(ans) != n:
            return []
        return ans
        
            
                
        
           
            
                
                
                
            
        
        
        
        
            
            